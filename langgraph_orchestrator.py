# langgraph_orchestrator.py

from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph
from langgraph.graph import StateGraph, END

# --------------------------------------------------
# IMPORT YOUR EXISTING LOGIC (NO REWRITE)
# --------------------------------------------------

from classifier_agent import classify_ticket
from entity_agent import extract_entities
from summary_agent import summarize_ticket
from qa_agent import validate_response


# --------------------------------------------------
# 1️⃣ SHARED STATE DEFINITION (CORE AGENTIC PART)
# --------------------------------------------------

class TicketState(TypedDict):
    text: str
    category: str
    entities: List[Dict[str, Any]]
    summary: str
    validated: bool
    confidence: float
    retries: int


# --------------------------------------------------
# 2️⃣ AGENT NODES (WRAPPERS ONLY)
# --------------------------------------------------

def classification_node(state: TicketState) -> TicketState:
    category = classify_ticket(state["text"])
    state["category"] = category
    return state


def entity_node(state: TicketState) -> TicketState:
    state["entities"] = extract_entities(state["text"])
    return state


def summary_node(state: TicketState) -> TicketState:
    state["summary"] = summarize_ticket(
        state["category"],
        state["entities"]
    )
    return state


def qa_node(state: TicketState) -> TicketState:
    qa_result = validate_response(
        state["category"],
        state["summary"]
    )

    state["validated"] = qa_result["valid"]
    state["confidence"] = qa_result["confidence"]
    state["retries"] += 1

    return state


# --------------------------------------------------
# 3️⃣ DECISION LOGIC (THIS MAKES IT AGENTIC)
# --------------------------------------------------

def should_retry(state: TicketState) -> bool:
    return not state["validated"] and state["retries"] < 2


# --------------------------------------------------
# 4️⃣ LANGGRAPH ORCHESTRATION
# --------------------------------------------------

graph = StateGraph(TicketState)

# Register agent nodes
graph.add_node("classify", classification_node)
graph.add_node("entities", entity_node)
graph.add_node("summary", summary_node)
graph.add_node("qa", qa_node)

# Entry point
graph.set_entry_point("classify")

# Normal flow
graph.add_edge("classify", "entities")
graph.add_edge("entities", "summary")
graph.add_edge("summary", "qa")

# Conditional retry loop
graph.add_conditional_edges(
    "qa",
    should_retry,
    {
        True: "classify",
        False: END
    }
)

# Compile the agentic app
app = graph.compile()


# --------------------------------------------------
# 5️⃣ LOCAL TEST RUN
# --------------------------------------------------

if __name__ == "__main__":
    ticket_text = """
    My savings account 123456789012 is frozen after multiple failed login attempts.
    PAN number ABCDE1234F is linked to this account.
    I tried contacting the Hyderabad branch.
    """

    initial_state: TicketState = {
        "text": ticket_text,
        "category": "",
        "entities": [],
        "summary": "",
        "validated": False,
        "confidence": 0.0,
        "retries": 0
    }

    result = app.invoke(initial_state)

    print("\n======================")
    print("FINAL RESULTS")
    print("======================")
    print("CATEGORY:", result["category"])
    print("ENTITIES:", result["entities"])
    print("SUMMARY:", result["summary"])
    print("VALIDATED:", result["validated"])
    print("CONFIDENCE:", result["confidence"])
