from pathlib import Path
import shutil
import uuid

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_uploaded_file(file):

    extension = Path(file.filename).suffix

    stored_filename = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / stored_filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return stored_filename