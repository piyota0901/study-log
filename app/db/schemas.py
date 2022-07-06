import datetime
from typing import List, Optional

from pydantic import UUID4, BaseModel, Field


class SubjectBase(BaseModel):
    """サブジェクトの作成"""

    name: str = Field(max_length=32)
    category: Optional[str]


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    """サブジェクト"""

    id: UUID4
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class SubjectUpdate(SubjectBase):
    """サブジェクトの更新"""

    name: Optional[str]
