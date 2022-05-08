from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def do():
    return 3

