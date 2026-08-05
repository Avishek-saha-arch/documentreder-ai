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