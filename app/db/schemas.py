import datetime
from typing import List, Optional, Union

from app.db.database import Base
from pydantic import UUID4, BaseModel, Field


class TaskBase(BaseModel):
    """サブジェクトの作成"""

    name: str = Field(max_length=32)
    category: Optional[str]


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    """サブジェクト"""

    id: UUID4
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class TaskUpdate(TaskBase):
    """サブジェクトの更新"""

    name: Optional[str]


class UserCreate(BaseModel):
    """ユーザー"""

    firstname: str
    lastname: str
    email: str
    password: str


class UserInLogin(UserCreate):

    token: str


class UserForLogin(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class JWTMeta(BaseModel):
    sub: str
    exp: datetime.datetime
    nbf: Optional[str]
    iat: Optional[str]
    jti: Optional[str]
    aud: Optional[str]
    iss: Optional[str]
