from app.db import cruds, schemas
from app.db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/subjects", tags=["subjects"])


@router.get("/list")
def read_subject_all(db: Session = Depends(get_db)):
    """全サブジェクトを返す"""
    return cruds.select_subject_all(db=db)


@router.get("/{subject_id}")
def read_subject_by_id(subject_id: str, db: Session = Depends(get_db)):
    """指定IDのサブジェクトを返す"""
    return cruds.select_subject_by_id(subject_id=subject_id, db=db)


@router.post("/create")
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    """サブジェクトを作成する"""
    return cruds.add_subject(subject=subject, db=db)


@router.put("/update/{subject_id}", response_model=schemas.Subject)
def update_subject(
    subject_id: str, subject: schemas.SubjectUpdate, db: Session = Depends(get_db)
):
    return cruds.update_subject(subject_id=subject_id, subject=subject, db=db)
