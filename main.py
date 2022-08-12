from uuid import UUID

from fastapi import FastAPI

from src.simple_day.service import get_user_by_id, list_users, add_user
from src.simple_day.model import UserReq, ActionReq

app = FastAPI()


@app.get("/user/{user_uuid}")
def get_user(user_uuid: UUID):
    return get_user_by_id(user_uuid)


@app.get("/user/list")
def list_user():
    return list_users()

@app.post("/user")
def create_user(user: UserReq):
    return add_user(user)


