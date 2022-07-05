import uuid
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pydantic import Field, UUID4
from typing import List, Optional


class SubjectCreate(BaseModel):
    """サブジェクトの作成"""

    name: str
    description: Optional[str]
    category: Optional[List[str]]


class SubjectUpdate(BaseModel):
    """サブジェクトの更新"""

    name: Optional[str]
    description: Optional[str]
    category: Optional[List[str]]


router = APIRouter(prefix="/subjects", tags=["subjects"])

# フェイクDB
fake_subject_db = {}


@router.get("/list")
def read_subjects():
    """全サブジェクトを返す"""
    return fake_subject_db


@router.post("/create")
def create_subject(subject: SubjectCreate):
    """サブジェクトを作成する"""
    fake_subject_db[str(uuid.uuid4())] = subject.dict()
    return subject


@router.put("/update/{subject_id}", response_model=SubjectUpdate)
def update_subject(subject_id: str, subject: SubjectUpdate):
    """サブジェクトを更新する"""
    org_subject_data = fake_subject_db[subject_id]
    org_subject = SubjectCreate(**org_subject_data)

    update_data = subject.dict(exclude_unset=True)
    updated_subject = org_subject.copy(update=update_data)
    fake_subject_db[subject_id] = jsonable_encoder(updated_subject)
    return updated_subject
