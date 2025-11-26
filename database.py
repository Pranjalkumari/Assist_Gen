import sqlite3
import json

DB_NAME = "sessions.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions 
                 (session_id TEXT PRIMARY KEY, history TEXT)''')
    conn.commit()
    conn.close()

def get_history(session_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT history FROM sessions WHERE session_id=?", (session_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return []

def update_history(session_id, role, content):
    history = get_history(session_id)
    history.append({"role": role, "content": content})
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO sessions (session_id, history) VALUES (?, ?)", 
              (session_id, json.dumps(history)))
    conn.commit()
    conn.close()