from typing import List
from uuid import uuid4

from app.db import models, schemas
from sqlalchemy.orm import Session


def select_task_all(db: Session) -> List[schemas.Task]:
    """全taskを取得する

    Args:
        db (Session): dbセッション

    Returns:
        List[schemas.Task]: タスク
    """
    return db.query(models.task).all()


def select_task_by_id(task_id: str, db: Session) -> schemas.Task:
    """指定IDのtaskを取得する

    Args:
        db (Session): _description_

    Returns:
        schemas.Task: _description_
    """
    return db.query(models.task).filter_by(id=task_id).first()


def add_task(task: schemas.TaskCreate, db: Session) -> schemas.Task:
    """taskを登録する

    Args:
        task (schemas.TaskCreate): task
        db (Session): dbセッション

    Returns:
        schemas.Task: タスク
    """
    new_task = models.task(
        id=str(uuid4()),
        name=task.name,
        category=task.category,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return db.query(models.Task).filter_by(id=new_task.id).first()


def update_task(task_id: str, task: schemas.TaskUpdate, db: Session) -> schemas.Task:
    """タスクを更新する

    Args:
        task_id (str): _description_
        db (Session): _description_

    Returns:
        schemas.Task: _description_
    """
    db_task = select_task_by_id(task_id=task_id, db=db)
    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    # 更新
    db.commit()
    db.flush(db_task)

    return db_task


def delete_task(task_id: str, db: Session) -> None:
    """タスクを削除する

    Args:
        task_id (str): _description_
    """
    db_task = select_task_by_id(task_id=task_id, db=db)

    db.delete(db_task)
    db.commit()
    return None
