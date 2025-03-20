from sqlalchemy import Column, ForeignKey, Integer, String
from api.db import Base
from sqlalchemy.orm import relationship


class Task(Base):
  __tablename__ = "tasks"
  # Column; カラム
  
  id = Column(Integer, primary_key=True)
  title = Column(String(1024))
  
  done = relationship("Done", back_populates = "task", cascade = "delete")
  
class Done(Base):
  __tablename__ = "dones"
  
  id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
  task = relationship("Task", back_populates="done")