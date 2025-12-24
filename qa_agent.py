# qa_core.py

# -------------------------
# Category keyword checks
# -------------------------
CATEGORY_KEYWORDS = {
    "Payment Issue": ["payment", "transaction"],
    "Account Issue": ["account", "identity"],
    "Technical Issue": ["technical", "error", "issue"],
    "Delivery Issue": ["delivery", "shipment", "order"]
}

GENERIC_FALLBACK = "customer reports an issue requiring assistance"


def validate_response(category: str, summary: str):
    """
    Validate classification and entity-driven summary output.
    Returns validity flag and confidence score.
    """
    category = category.strip()
    summary = summary.strip().lower()

    confidence = 0.3
    valid = False

    # 1️⃣ Reject generic fallback summary
    if GENERIC_FALLBACK in summary:
        return {
            "valid": False,
            "confidence": 0.3
        }

    # 2️⃣ Category alignment
    keywords = CATEGORY_KEYWORDS.get(category, [])
    category_match = any(k in summary for k in keywords)

    if category_match:
        confidence += 0.4
        valid = True

    # 3️⃣ Entity concept presence (implicit)
    if any(k in summary for k in ["associated", "related", "linked"]):
        confidence += 0.3

    confidence = min(round(confidence, 2), 1.0)

    return {
        "valid": valid,
        "confidence": confidence
    }
