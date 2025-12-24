# db.py
import sqlite3
import json

DB_NAME = "tickets.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_text TEXT,
            category TEXT,
            entities TEXT,
            summary TEXT,
            validated INTEGER,
            confidence REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_ticket(ticket_text, category, entities, summary, validated, confidence):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tickets
        (ticket_text, category, entities, summary, validated, confidence)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        ticket_text,
        category,
        json.dumps(entities),
        summary,
        int(validated),
        confidence
    ))
    conn.commit()
    conn.close()

def fetch_all_tickets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
