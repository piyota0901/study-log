from app.db import cruds, schemas
from app.db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/list")
def read_task_all(db: Session = Depends(get_db)):
    """全タスクを返す"""
    return cruds.select_task_all(db=db)


@router.get("/{task_id}")
def read_task_by_id(task_id: str, db: Session = Depends(get_db)):
    """指定IDのタスクを返す"""
    return cruds.select_task_by_id(task_id=task_id, db=db)


@router.post("/create")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """タスクを作成する"""
    return cruds.add_task(task=task, db=db)


@router.put("/update/{task_id}", response_model=schemas.Task)
def update_task(task_id: str, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """タスクを更新する

    Args:
        task_id (str): タスクID
        task (schemas.taskUpdate): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return cruds.update_task(task_id=task_id, task=task, db=db)


@router.delete("/delete/{task_id}")
def delete_task(task_id: str, db: Session = Depends(get_db)):
    """タスクを削除する

    Args:
        task_id (str): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
    """
    return cruds.delete_task(task_id=task_id, db=db)
