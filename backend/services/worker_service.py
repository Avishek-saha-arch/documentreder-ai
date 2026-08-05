from database.database import SessionLocal
from database.models import ProcessingJob


def get_pending_job():

    db = SessionLocal()

    jobs = db.query(ProcessingJob).all()

    print("\n========== WORKER DATABASE ==========")
    print("Total Jobs:", len(jobs))

    for job in jobs:
        print(
            f"Job ID={job.id}, "
            f"Document={job.document_id}, "
            f"Status={job.status}"
        )

    print("=====================================\n")

    job = (
        db.query(ProcessingJob)
        .filter(ProcessingJob.status == "pending")
        .first()
    )

    db.close()

    return job