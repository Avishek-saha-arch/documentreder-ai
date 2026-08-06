from fastapi import APIRouter

from services.document_service import (
    get_all_documents,
    get_document,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/")
def documents():

    docs = get_all_documents()

    return [
        {
            "id": d.id,
            "original_filename": d.original_filename,
            "status": d.status,
            "document_type": d.document_type,
            "created_at": d.created_at
        }
        for d in docs
    ]


@router.get("/{document_id}")
def document(document_id: int):

    d = get_document(document_id)

    if d is None:
        return {"error": "Document not found"}

    return {
        "id": d.id,
        "original_filename": d.original_filename,
        "stored_filename": d.stored_filename,
        "status": d.status,
        "document_type": d.document_type,
        "raw_text": d.raw_text,
        "extracted_data": d.extracted_data,   # ← Make sure this exists
        "created_at": d.created_at
    }