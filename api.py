from fastapi import FastAPI
from random_identity import Random_Identity

app = FastAPI()

@app.get("/")
async def all():
    data = Random_Identity().to_json()
    return data

