from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from database.database import Base


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