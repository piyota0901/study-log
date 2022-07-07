from typing import List
from unicodedata import category
from uuid import uuid4

from app.db import models, schemas
from sqlalchemy.orm import Session


def select_subject_all(db: Session) -> List[schemas.Subject]:
    """全subjectを取得する

    Args:
        db (Session): dbセッション

    Returns:
        List[schemas.Subject]: サブジェクト
    """
    return db.query(models.Subject).all()


def select_subject_by_id(subject_id: str, db: Session) -> schemas.Subject:
    """指定IDのsubjectを取得する

    Args:
        db (Session): _description_

    Returns:
        schemas.Subject: _description_
    """
    return db.query(models.Subject).filter_by(id=subject_id).first()


def add_subject(subject: schemas.SubjectCreate, db: Session) -> schemas.Subject:
    """subjectを登録する

    Args:
        subject (schemas.SubjectCreate): subject
        db (Session): dbセッション

    Returns:
        schemas.Subject: サブジェクト
    """
    new_subject = models.Subject(
        id=str(uuid4()),
        name=subject.name,
        category=subject.category,
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return db.query(models.Subject).filter_by(id=new_subject.id).first()


def update_subject(
    subject_id: str, subject: schemas.SubjectUpdate, db: Session
) -> schemas.Subject:
    """サブジェクトを更新する

    Args:
        subject_id (str): _description_
        db (Session): _description_

    Returns:
        schemas.Subject: _description_
    """
    db_subject = select_subject_by_id(subject_id=subject_id, db=db)
    update_data = subject.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_subject, key, value)
    # 更新
    db.commit()
    db.flush(db_subject)

    return db_subject
