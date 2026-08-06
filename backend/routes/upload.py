from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from services.file_service import save_uploaded_file
from services.document_service import (
    create_document_record,
    get_all_documents,
    get_document,
)
from services.job_service import create_job

router = APIRouter()

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg"
}


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    stored_filename = save_uploaded_file(file)

    document = create_document_record(
        original_filename=file.filename,
        stored_filename=stored_filename
    )

    job = create_job(document.id)

    print("========== DEBUG ==========")
    print("Document ID:", document.id)
    print("Job ID:", job.id)
    print("Job Status:", job.status)
    print("===========================")

    return {
        "success": True,
        "document_id": document.id,
        "job_id": job.id,
        "filename": file.filename,
        "stored_filename": stored_filename,
        "document_status": document.status,
        "job_status": job.status,
        "message": "Upload successful. OCR job created."
    }


@router.get("/documents/")
def list_documents():
    return get_all_documents()


@router.get("/documents/{document_id}")
def document_details(document_id: int):

    document = get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document