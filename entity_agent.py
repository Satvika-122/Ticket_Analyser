# entity_core.py
import re
from transformers import pipeline

# Load NER model once
_ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_custom_entities(text: str):
    entities = []

    # Account number: 10–16 digit numbers
    for match in re.findall(r"\b\d{10,16}\b", text):
        entities.append({"text": match, "type": "ACCOUNT_NUMBER"})

    # IFSC code
    for match in re.findall(r"\b[A-Z]{4}0\d{6}\b", text):
        entities.append({"text": match, "type": "IFSC_CODE"})

    # Branch name
    for match in re.findall(r"\bbranch\s+[A-Za-z]+\b", text, flags=re.IGNORECASE):
        entities.append({"text": match, "type": "BRANCH_NAME"})

    # Order ID
    for match in re.findall(r"Order ID\s*\d+", text, flags=re.IGNORECASE):
        entities.append({"text": match, "type": "ORDER_ID"})

    # Transaction ID
    for match in re.findall(r"Transaction ID\s*[A-Za-z0-9]+", text, flags=re.IGNORECASE):
        entities.append({"text": match, "type": "TRANSACTION_ID"})

    # PAN number (ABCDE1234F)
    for match in re.findall(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", text):
        entities.append({"text": match, "type": "PAN_NUMBER"})

    # UPI ID (example: name@bank)
    for match in re.findall(r"\b[\w.-]+@[\w.-]+\b", text):
        entities.append({"text": match, "type": "UPI_ID"})

    # Email
    for match in re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text):
        entities.append({"text": match, "type": "EMAIL"})

    # Phone number (10 digits)
    for match in re.findall(r"\b\d{10}\b", text):
        entities.append({"text": match, "type": "PHONE_NUMBER"})

    return entities


def extract_entities(text: str):
    """
    Extract entities using both ML-based NER and rule-based regex.
    """
    ner_entities = _ner(text)
    model_entities = [
        {"text": e["word"], "type": e["entity_group"]}
        for e in ner_entities
    ]

    custom_entities = extract_custom_entities(text)

    return model_entities + custom_entities
