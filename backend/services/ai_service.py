def extract_document_data(raw_text: str):
    """
    Temporary AI extraction.
    Later this will use an LLM.
    """

    data = {
        "document_type": "Unknown",
        "summary": raw_text[:200]
    }

    return data