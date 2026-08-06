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


def get_all_documents():

    db = SessionLocal()

    documents = db.query(Document).all()

    db.close()

    return documents


def get_document(document_id):

    db = SessionLocal()

    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    db.close()

    return document