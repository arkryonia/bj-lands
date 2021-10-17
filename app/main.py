
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local contribs
from app.core.db import create_db_and_tables

# import routes
from app.bj.router import bj

app = FastAPI()

origins = [
    "http://localhost:8080",
    "https://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(bj, prefix="/bj", tags=["Benin Lands"])
