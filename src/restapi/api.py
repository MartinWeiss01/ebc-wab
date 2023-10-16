from typing import Union, Annotated

from fastapi import FastAPI

from models import Pet
from uuid import UUID

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pet/")
def get_pets() -> list[Pet]:
    return None

@app.get("/pet/{id}")
def get_pets(pet: Annotated[UUID, Path()] -> Pet:
    return None