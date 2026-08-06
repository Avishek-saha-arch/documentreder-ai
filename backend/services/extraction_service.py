import json

from database.database import SessionLocal
from database.models import Document


def save_raw_text(document_id: int, text: str):
    """
    Save OCR text into the document record.
    """

    db = SessionLocal()

    try:
        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document is None:
            print(f"Document {document_id} not found.")
            return False

        document.raw_text = text
        db.commit()

        print(f"Saved OCR text for Document {document_id}")

        return True

    finally:
        db.close()


def save_extracted_data(document_id: int, data):
    """
    Save AI extracted JSON into the document record.
    """

    db = SessionLocal()

    try:
        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document is None:
            print(f"Document {document_id} not found.")
            return False

        document.extracted_data = json.dumps(data, indent=2)

        db.commit()

        print(f"Saved extracted data for Document {document_id}")

        return True

    finally:
        db.close()