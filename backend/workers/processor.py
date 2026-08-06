import time
from pathlib import Path

from services.worker_service import get_pending_job
from services.job_service import update_job_status
from services.pdf_service import convert_pdf_to_images
from services.ocr_service import extract_text
from services.extraction_service import (
    save_raw_text,
    save_extracted_data,
)
from services.ai_service import extract_document_data

print("🚀 Worker Started")

while True:

    job = get_pending_job()

    if job:

        print(f"\nProcessing Job #{job.id}")

        update_job_status(job.id, "running")

        try:

            pdf_path = Path("uploads") / job.document.stored_filename

            print(f"Reading PDF: {pdf_path}")

            # Convert PDF into images
            image_paths = convert_pdf_to_images(str(pdf_path))

            full_text = ""

            # OCR each page
            for image in image_paths:

                print(f"OCR -> {image}")

                text = extract_text(image)

                full_text += text + "\n\n"

            # Save OCR text
            save_raw_text(
                job.document.id,
                full_text
            )

           # AI Extraction
            print("\n========== AI ==========")

            extracted_data = extract_document_data(
                full_text
            )

            print("AI Returned:")
            print(extracted_data)

            # Save AI extracted JSON
            save_extracted_data(
                job.document.id,
                extracted_data
            )

            print("AI Data Saved")

            print("========================\n")
            # Mark job as completed
            update_job_status(
                job.id,
                "completed"
            )

            print("✅ OCR + AI Extraction Saved Successfully")

        except Exception as e:

            print("❌ ERROR:", e)

            update_job_status(
                job.id,
                "failed"
            )

    else:

        print("No pending jobs")

    time.sleep(5)