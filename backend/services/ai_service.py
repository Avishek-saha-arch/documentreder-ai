import json
import ollama


def extract_document_data(raw_text: str):
    """
    Extract dynamic structured information from OCR text using Ollama.
    """

    # Limit OCR text for faster AI processing
    raw_text = raw_text[:5000]

    prompt = f"""
You are an expert AI document understanding system.

Analyze the OCR text below and extract the important information from it.

Your job is to understand WHAT KIND OF DOCUMENT this is and then
extract the information that is actually relevant to that document.

The document can be ANYTHING, including:

- Certificate
- Invoice
- Resume
- Application Form
- Government Form
- ID Document
- Study Notes
- Report
- Letter
- Contract
- Receipt
- Research Paper
- Question Paper
- Medical Document
- Business Document
- Or any other document

IMPORTANT RULES:

1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. Do NOT return ```json.
4. Do NOT explain your answer.
5. Do NOT invent information.
6. If information is not present, do not create a field for it.
7. Create fields dynamically based on the actual document.
8. Extract all important information that can reasonably be identified.
9. Preserve important numbers, names, dates, amounts, titles and identifiers.
10. Keep the summary concise.
11. The "fields" object can contain any keys that are relevant to the document.
12. If the document has lists, arrays may be used.
13. If the document contains tables, represent important table information using arrays of objects when appropriate.

Return exactly this overall structure:

{{
    "document_type": "type of document",
    "fields": {{
        "field_name": "value"
    }},
    "summary": "short summary of the document"
}}

OCR TEXT:

{raw_text}
"""

    print("\n========== AI ==========")
    print("Sending document to Gemma...")

    try:

        response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json",
        options={
            "temperature": 0
        }
)

        print("Response received!")

        content = response["message"]["content"].strip()

        # Remove markdown fences if the model accidentally returns them
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        print("\nAI RESPONSE:")
        print(content)

        # Try to parse JSON directly
        try:
            data = json.loads(content)

        except json.JSONDecodeError:

            # Sometimes the model puts extra text before/after JSON.
            # Try to locate the JSON object.
            start = content.find("{")
            end = content.rfind("}")

            if start == -1 or end == -1:
                raise ValueError("No JSON object found in AI response.")

            json_text = content[start:end + 1]

            data = json.loads(json_text)

        # Make sure the basic structure exists
        if not isinstance(data, dict):
            raise ValueError("AI response is not a JSON object.")

        if "document_type" not in data:
            data["document_type"] = "Unknown"

        if "fields" not in data:
            data["fields"] = {}

        if "summary" not in data:
            data["summary"] = ""

        print("\n✅ JSON parsed successfully!")

        print("\nDocument Type:")
        print(data["document_type"])

        print("\nExtracted Fields:")
        print(json.dumps(data["fields"], indent=2))

        return data

    except Exception as e:

        print("\n❌ AI EXTRACTION ERROR")
        print("----------------------")
        print(str(e))
        print("----------------------")

        raise