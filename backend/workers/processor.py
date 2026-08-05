import time

from services.worker_service import get_pending_job
from services.job_service import update_job_status

print("🚀 Worker Started")

while True:

    job = get_pending_job()

    if job:

        print(f"Processing Job #{job.id}")

        update_job_status(job.id, "running")

        print(f"Job {job.id} is now RUNNING")

        # Temporary fake OCR
        time.sleep(3)

        update_job_status(job.id, "completed")

        print(f"Job {job.id} COMPLETED")

    else:

        print("No pending jobs")

    time.sleep(5)