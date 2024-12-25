from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Item(Base):
    __tablename__ = "todo_items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, default=None, nullable=True)
    completed = Column(Boolean, default=False)
