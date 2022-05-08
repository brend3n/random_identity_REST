from typing import Optional
from fastapi import FastAPI

# TODO: import random_identity class


app = FastAPI()


@app.get("/")
def all():
    return

