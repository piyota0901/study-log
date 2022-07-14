from uuid import uuid4

from app.auth.security import get_password_hash
from app.db import cruds, models, schemas
from app.db.database import get_db
from app.db.schemas import UserForLogin
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


def add_user(user: schemas.UserCreate, db: Session):
    new_user = models.User(
        id=str(uuid4()),
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        hashed_password=get_password_hash(password=user.password),
        disabled=True,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return db.query(models.User).filter_by(id=new_user.id).first()


@router.get("/login", response_model=schemas.TokenData)
def login(user: UserForLogin, db: Session = Depends(get_db)):
    pass


@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ユーザー作成

    Args:
        user (schemas.UserCreate): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).
    """
    return add_user(user=user, db=db)
