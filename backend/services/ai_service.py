import json
import ollama


def extract_document_data(raw_text: str):
    """
    Extract structured information from OCR text using Ollama (Gemma 3).
    """

    # Limit text for faster inference
    raw_text = raw_text[:2500]

    prompt = f"""
You are an expert AI document parser.

Analyze the OCR text below.

Return ONLY a valid JSON object.

Rules:
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT use ```json.
- If information is missing, return null.
- Return ONLY JSON.

Return this exact structure:

{{
    "document_type": null,
    "recipient_name": null,
    "organization": null,
    "issuer": null,
    "course": null,
    "invoice_number": null,
    "amount": null,
    "date": null,
    "summary": null
}}

OCR TEXT:

{raw_text}
"""

    print("\n========== AI ==========")
    print("Sending request to Gemma...")

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    print("Response received!")

    content = response["message"]["content"].strip()

    # Remove markdown if the model returns it
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        data = json.loads(content)

        print("JSON parsed successfully!")

        return data

    except Exception as e:

        print("\n❌ Invalid JSON returned by Gemma")
        print("--------------------------------")
        print(content)
        print("--------------------------------")
        print(e)

        return {
            "document_type": "Unknown",
            "recipient_name": None,
            "organization": None,
            "issuer": None,
            "course": None,
            "invoice_number": None,
            "amount": None,
            "date": None,
            "summary": content
        }