import json
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import google.generativeai as genai
from database import init_db, get_history, update_history

# Initialize App and DB
app = FastAPI()
init_db()

# --- CONFIGURATION ---
# PASTE YOUR WORKING GOOGLE API KEY HERE
GOOGLE_API_KEY = "AIzaSyC8GdfaB3_bwlwu4h_7yv-y2ODWZyw5zxQ"

genai.configure(api_key=GOOGLE_API_KEY)

# Use the model that worked for you (likely gemini-1.5-flash or gemini-2.5-flash)
model = genai.GenerativeModel('gemini-2.5-flash')

# Load FAQs
with open("faqs.json", "r") as f:
    faqs = json.load(f)

# Create a clean text block of FAQs for the AI to read
faq_text = "\n".join([f"Q: {item['question']}\nA: {item['answer']}" for item in faqs])

class ChatRequest(BaseModel):
    session_id: str
    query: str

# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     with open("index.html", "r") as f:
#         return f.read()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    # 1. Retrieve Context
    history = get_history(req.session_id)
    
    # 2. Format History
    conversation_log = ""
    for msg in history:
        role = "User" if msg['role'] == "user" else "Bot"
        conversation_log += f"{role}: {msg['content']}\n"

    # 3. Prepare the Hybrid System Prompt
    # This instructs the AI to prioritize FAQs but fall back to general knowledge
    full_prompt = f"""
    You are a helpful customer support assistant.
    
    Verified Knowledge Base (Priority):
    {faq_text}

    Instructions:
    1. First, check the 'Verified Knowledge Base' above. If the answer is there, use it strictly.
    2. If the answer is NOT in the Knowledge Base, use your own general knowledge to answer the user politely and helpfully.
    3. If you use general knowledge, add the phrase "(AI Generated)" at the end of your response so the user knows.
    
    Conversation History:
    {conversation_log}

    User's Question: {req.query}
    """

    # 4. Call Gemini
    try:
        response = model.generate_content(full_prompt)
        bot_reply = response.text.strip()
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

    # 5. Save Session & Return
    update_history(req.session_id, "user", req.query)
    update_history(req.session_id, "assistant", bot_reply)

    return {
        "response": bot_reply,
        "session_id": req.session_id
    }