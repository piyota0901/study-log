from datetime import datetime, timedelta
from typing import Dict

from app.db.schemas import JWTMeta
from jose import jwt

JWT_SUBJECT = "access"
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def create_jwt_token(jwt_content: Dict[str, str], expire_delta: timedelta) -> str:
    """JWTを作成する

    Args:
        jwt_content (Dict[str, str]): claim

    Returns:
        str: JWT
    """
    to_encode = jwt_content.copy()
    expire = datetime.utcnow() + expire_delta
    to_encode.update(JWTMeta(exp=expire, sub=JWT_SUBJECT).dict())
    return jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
