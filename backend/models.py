from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String)
    experience = Column(String)
    salary = Column(String)
    job_type = Column(String)  # Full-time / Part-time / Remote
    employer_id = Column(Integer, ForeignKey("users.id"))
