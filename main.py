from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

@app.post("/user/")
def set_user(user: User):
    return {"key": user}

@app.get("/user/{user_id}")
def main(user_id: int):
    user = {
        "id": 2,
        "username": "Mike"
    }
    return {"key": user}
