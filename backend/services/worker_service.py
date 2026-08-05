from sqlalchemy.orm import joinedload

from database.database import SessionLocal
from database.models import ProcessingJob


def get_pending_job():

    db = SessionLocal()

    job = (
        db.query(ProcessingJob)
        .options(joinedload(ProcessingJob.document))
        .filter(ProcessingJob.status == "pending")
        .first()
    )

    if job:
        db.expunge(job)
        if job.document:
            db.expunge(job.document)

    db.close()

    return job