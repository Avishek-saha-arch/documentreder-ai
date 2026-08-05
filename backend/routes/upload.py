from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from services.file_service import save_uploaded_file
from services.document_service import create_document_record

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

    return {
        "success": True,
        "document_id": document.id,
        "filename": file.filename,
        "stored_filename": stored_filename,
        "status": document.status,
        "message": "File uploaded successfully"
    }