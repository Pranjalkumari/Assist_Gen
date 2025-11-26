#  AI Customer Support Bot  
A hybrid Customer Support System built using **FastAPI**, **Google Gemini (Generative AI)**, and a **custom HTML/CSS frontend**.  
The bot answers queries using a **Verified FAQ Knowledge Base**, and if an answer is not available, it intelligently generates a response using Gemini AI.

---

##  Features

### 1. FAQ-Based Answers (Highest Priority)**
The bot first checks a curated `faqs.json` file and responds strictly from the verified knowledge base.

### 2. AI-Generated Answers (Fallback)**
If no FAQ matches:
- Gemini (`gemini-2.5-flash`) generates a helpful response.
- The bot clearly marks it with **"(AI Generated)"** as required.

### 3. Session Support**
Every user session maintains:
- Conversation history  
- User queries  
- Bot responses  

Stored using a lightweight file-based SQLite/database module.

### 4. Modern Frontend UI**
Beautiful chat interface built using:
- HTML  
- CSS  
- JavaScript  

Includes:
- Smooth chat animation  
- User & bot bubbles  
- Escalation highlighting  
- Scroll-follow  
- Mobile responsive layout

### 5. Clean Backend Architecture**
- FastAPI routes  
- Structured endpoints  
- Modular DB functions  
- Safe Google Gemini integration  
- Separate `faqs.json` for maintainability

---

## 📂 Project Structure

AI-bol/
│── main.py # FastAPI backend + Gemini logic
│── database.py # Session storage and history handling
│── faqs.json # Verified FAQ dataset
│── index.html # Frontend UI
│── README.md # Documentation
│── requirements.txt # Python dependencies
└── ...


---

## 🛠 Tech Stack

### **Backend:**
- Python 3.10+
- FastAPI
- Uvicorn
- Google Gemini API (`google-generativeai`)

### **Frontend:**
- HTML
- CSS
- JavaScript

### **Database:**
- Simple JSON/SQLite session history (custom)





