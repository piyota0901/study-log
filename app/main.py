from fastapi import FastAPI
from app.routers import subjects

app = FastAPI()
app.include_router(subjects.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
