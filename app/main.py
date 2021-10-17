
from fastapi import FastAPI

from app.core.db import create_db_and_tables
from app.hero.app import hero

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(hero, prefix="/heroes", tags=["Heroes"])


