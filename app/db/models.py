from datetime import datetime

from sqlalchemy import Column, DateTime, String, Text

from .database import Base


class Subject(Base):
    """サブジェクト"""

    __tablename__ = "subjects"
    id = Column(String(128), primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    category = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


if __name__ == "__main__":
    pass
