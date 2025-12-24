# classifier_core.py
from transformers import pipeline

# Load model once
_classifier = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def classify_ticket(text: str) -> str:
    """
    Classify a customer support ticket into a predefined category.
    """
    prompt = f"""
Classify the following customer support ticket into one of these category:
Payment Issue
Account Issue
Technical Issue
Delivery Issue
Other

Ticket:
{text}

Answer with only the category name.
"""
    result = _classifier(prompt, max_length=5)
    return result[0]["generated_text"].strip()
