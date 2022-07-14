from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """パスワード検証

    Args:
        plain_password (str): 平文のパスワード
        hashed_password (str): ハッシュ化されたパスワード

    Returns:
        bool: パスワード検証結果
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """パスワードをハッシュ化して返す

    Args:
        password (str): パスワード

    Returns:
        str: ハッシュ化したパスワード
    """
    return pwd_context.hash(secret=password)
