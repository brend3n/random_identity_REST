from typing import Optional
from fastapi import FastAPI
#from random_identity import Random_Identity, BackgroundTasks
from random_identity import Random_Identity
import json
from time import sleep
app = FastAPI()

def get_identity():
    data = json.dumps(Random_Identity.to_string())
    return data

@app.get("/")
# async def all(background_tasks: BackgroundTasks):
async def all():
    # background_tasks.add_task(get_identity)
    data = Random_Identity().to_string()
    
    return data

