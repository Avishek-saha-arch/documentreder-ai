from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from database.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    original_filename = Column(String)

    stored_filename = Column(String)

    document_type = Column(String, default="unknown")

    status = Column(String, default="uploaded")

    raw_text = Column(Text, nullable=True)

    extracted_data = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

class ProcessingJob(Base):
    __tablename__ = "processing_jobs"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    job_type = Column(String)

    status = Column(
        String,
        default="pending"
    )

    started_at = Column(
        DateTime,
        nullable=True
    )

    finished_at = Column(
        DateTime,
        nullable=True
    )

    error_message = Column(
        Text,
        nullable=True
    )

    document = relationship("Document")