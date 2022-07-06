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
    update_data = subject.dict(exclude_unset=True)
    print(update_data)
    obj = (
        db.query(models.Subject)
        .filter(models.Subject.id == subject_id)
        .update(update_data)
    )
    print(obj)
    # print("orm_subject: ", orm_subject)
    # org_subject = schemas.Subject.from_orm(orm_subject)
    # print("subject: ", org_subject)

    # update_subject = org_subject.copy(update=update_data)
    # print("update subject: ", update_subject)

    # 更新
    db.commit()
    return obj
