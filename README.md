# AI Customer Support Bot

## Objective
Simulates customer support interactions using AI for FAQs and escalation scenarios.

## Features
- REST API using FastAPI
- Contextual memory (SQLite)
- FAQ-based answering via LLM (OpenAI)
- Automatic Escalation simulation

## Setup
1. `pip install -r requirements.txt`
2. `export OPENAI_API_KEY='your-key-here'`
3. `uvicorn main:app --reload`