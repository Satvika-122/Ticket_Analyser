# app.py
import streamlit as st
from langgraph_orchestrator import app as agent_app
from db import init_db, insert_ticket, fetch_all_tickets

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="AI Ticket Analyzer", layout="centered")

# Initialize database (creates tickets.db if not exists)
init_db()

st.title("🧠 AI Ticket Analyzer (Agentic AI)")
st.write("Paste a customer support ticket below to analyze it using an agentic AI system.")

# -------------------------
# Input
# -------------------------
ticket_text = st.text_area(
    "Support Ticket",
    height=200,
    placeholder="Example: My account is frozen after multiple failed login attempts..."
)

# -------------------------
# Analyze Button
# -------------------------
if st.button("Analyze Ticket"):
    if not ticket_text.strip():
        st.warning("Please enter a ticket.")
    else:
        with st.spinner("Analyzing with agentic workflow..."):
            result = agent_app.invoke({
                "text": ticket_text,
                "category": "",
                "entities": [],
                "summary": "",
                "validated": False,
                "confidence": 0.0,
                "retries": 0
            })

        # -------------------------
        # Store result in DB
        # -------------------------
        insert_ticket(
            ticket_text=ticket_text,
            category=result["category"],
            entities=result["entities"],
            summary=result["summary"],
            validated=result["validated"],
            confidence=result["confidence"]
        )

        st.success("Analysis Complete")

        # -------------------------
        # Display Results
        # -------------------------
        st.subheader("📌 Category")
        st.write(result["category"])

        st.subheader("🔍 Extracted Entities")
        st.json(result["entities"])

        st.subheader("📝 Summary")
        st.write(result["summary"])

        st.subheader("✅ Validation")
        st.write(f"Valid: {result['validated']}")
        st.write(f"Confidence: {result['confidence']}")

# -------------------------
# Stored Tickets Section
# -------------------------
st.divider()
st.subheader("📦 Stored Tickets (Demo History)")

rows = fetch_all_tickets()

if rows:
    for row in rows:
        st.markdown(f"""
        **Ticket ID:** {row[0]}  
        **Category:** {row[2]}  
        **Summary:** {row[4]}  
        **Validated:** {bool(row[5])}  
        **Confidence:** {row[6]}
        """)
else:
    st.info("No tickets stored yet.")
