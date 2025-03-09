import uuid
from fastapi import FastAPI

app = FastAPI()


@app.get("/create")
async def create():
    request_id = str(uuid.uuid4())
    return {"request_id": request_id}

