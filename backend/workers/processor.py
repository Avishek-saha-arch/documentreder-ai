import time
from pathlib import Path

from services.worker_service import get_pending_job
from services.job_service import update_job_status
from services.pdf_service import convert_pdf_to_images
from services.ocr_service import extract_text
from services.extraction_service import save_raw_text

print("🚀 Worker Started")

while True:

    job = get_pending_job()

    if job:

        print(f"\nProcessing Job #{job.id}")

        update_job_status(job.id, "running")

        try:

            pdf_path = Path("uploads") / job.document.stored_filename

            print(f"Reading PDF: {pdf_path}")

            image_paths = convert_pdf_to_images(str(pdf_path))

            full_text = ""

            for image in image_paths:

                print(f"OCR -> {image}")

                text = extract_text(image)

                full_text += text + "\n\n"

            save_raw_text(job.document.id, full_text)

            update_job_status(job.id, "completed")

            print("✅ OCR Saved Successfully")

        except Exception as e:

            print("ERROR:", e)

            update_job_status(job.id, "failed")

    else:

        print("No pending jobs")

    time.sleep(5)