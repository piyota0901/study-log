from .database import engine
from .models import Base


def initialize_db():
    Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine, checkfirst=True)


if __name__ == "__main__":
    initialize_db()
