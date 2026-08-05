from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from services.file_service import save_uploaded_file
from services.document_service import create_document_record
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

    # Check file extension
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    # Save the uploaded file
    stored_filename = save_uploaded_file(file)

    # Create a document record in the database
    document = create_document_record(
        original_filename=file.filename,
        stored_filename=stored_filename
    )

    # Create an OCR processing job
    job = create_job(document.id)
    print("========== DEBUG ==========")
    print("Document ID:", document.id)
    print("Job ID:", job.id)
    print("Job Status:", job.status)
    print("===========================")

    # Return response
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