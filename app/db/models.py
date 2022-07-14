from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Task(Base):
    """タスク"""

    __tablename__ = "Tasks"
    id = Column(String(128), primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    category = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class User(Base):
    """ユーザー"""

    __tablename__ = "users"

    id = Column(String(128), primary_key=True)
    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    email = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


if __name__ == "__main__":
    pass
