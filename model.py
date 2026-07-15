from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    time_limit = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)


