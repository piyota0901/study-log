from fastapi import FastAPI

from app.db import initialize
from app.routers import subjects

initialize.initialize_db()

app = FastAPI()
app.include_router(subjects.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
