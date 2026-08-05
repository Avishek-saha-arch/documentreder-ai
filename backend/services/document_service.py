from database.database import SessionLocal
from database.models import Document


def create_document_record(
    original_filename,
    stored_filename,
):
    db = SessionLocal()

    document = Document(
        original_filename=original_filename,
        stored_filename=stored_filename,
        status="uploaded",
        document_type="unknown",
    )

    db.add(document)
    db.commit()
    db.refresh(document)
    db.close()

    return document