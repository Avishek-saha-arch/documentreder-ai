from sqlalchemy import Column, Integer, Text, ForeignKey
from database.database import Base


class Extraction(Base):
    __tablename__ = "extractions"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(Integer, ForeignKey("documents.id"))

    extracted_text = Column(Text)