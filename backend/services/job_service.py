from datetime import datetime

from database.database import SessionLocal
from database.models import ProcessingJob


def create_job(document_id, job_type="OCR"):

    db = SessionLocal()

    job = ProcessingJob(
        document_id=document_id,
        job_type=job_type,
        status="pending"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    print(f"✅ Created Job: {job.id}, Status: {job.status}")

    db.close()

    return job


def update_job_status(job_id, status):

    db = SessionLocal()

    job = (
        db.query(ProcessingJob)
        .filter(ProcessingJob.id == job_id)
        .first()
    )

    if job:

        job.status = status

        if status == "running":
            job.started_at = datetime.utcnow()

        elif status in ("completed", "failed"):
            job.finished_at = datetime.utcnow()

        db.commit()
        db.refresh(job)

    db.close()