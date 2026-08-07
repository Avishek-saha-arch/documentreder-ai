import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

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


def process_page(image_path):
    """
    Run OCR on a single page.
    """

    start = time.time()

    print(f"OCR -> {image_path}")

    text = extract_text(image_path)

    elapsed = time.time() - start

    print(
        f"✅ OCR finished -> {image_path} "
        f"({elapsed:.2f}s)"
    )

    return text


while True:

    job = get_pending_job()

    if job:

        print(f"\nProcessing Job #{job.id}")

        update_job_status(job.id, "running")

        try:

            pdf_path = (
                Path("uploads")
                / job.document.stored_filename
            )

            print(f"Reading PDF: {pdf_path}")

            # ==============================
            # PDF → Images
            # ==============================

            image_paths = convert_pdf_to_images(
                str(pdf_path)
            )

            print(
                f"PDF converted into {len(image_paths)} pages"
            )

            if not image_paths:
                raise ValueError(
                    "PDF conversion produced no images."
                )

            # ==============================
            # CONCURRENT OCR
            # ==============================

            ocr_start = time.time()

            full_text_parts = []

            max_workers = min(
                2,
                len(image_paths)
            )

            with ThreadPoolExecutor(
                max_workers=max_workers
            ) as executor:

                results = executor.map(
                    process_page,
                    image_paths
                )

                for text in results:
                    full_text_parts.append(text)

            full_text = "\n\n".join(
                full_text_parts
            )

            ocr_time = time.time() - ocr_start

            print("✅ OCR completed")
            print(f"⏱️ OCR took {ocr_time:.2f} seconds")

            # ==============================
            # SAVE OCR
            # ==============================

            save_raw_text(
                job.document.id,
                full_text
            )

            print("✅ OCR text saved")

            # ==============================
            # AI EXTRACTION
            # ==============================

            print("\n========== AI ==========")

            ai_start = time.time()

            extracted_data = extract_document_data(
                full_text
            )

            ai_time = time.time() - ai_start

            print(f"⏱️ AI took {ai_time:.2f} seconds")

            print("AI Returned:")
            print(extracted_data)

            # ==============================
            # SAVE AI DATA
            # ==============================

            save_extracted_data(
                job.document.id,
                extracted_data
            )

            print("AI Data Saved")

            print("========================\n")

            # ==============================
            # COMPLETE JOB
            # ==============================

            update_job_status(
                job.id,
                "completed"
            )

            print(
                "✅ OCR + AI Extraction Saved Successfully"
            )

        except Exception as e:

            print("\n❌ ERROR:")
            print(e)

            update_job_status(
                job.id,
                "failed"
            )

    else:

        print("No pending jobs")

    time.sleep(5)