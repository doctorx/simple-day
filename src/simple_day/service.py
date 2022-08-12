from typing import Dict
from uuid import UUID, uuid4

from src.simple_day.model import UserReq, ActionReq

USERS = [UserReq(**{
                "id": "651c2476-1990-11ed-861d-0242ac120002", 
                "name": "Bob",
                "active": True
            }),
        UserReq(**{ 
                "id":"93a60546-1990-11ed-861d-0242ac120002",
                "name": "Jane",
                "active": False
            })
    ]       

def get_user_by_id(user_uuid: UUID) -> UserReq:
    for user in USERS:
        if user.id == user_uuid:
            return user

def add_user(user_model: UserReq) -> bool:
    user_model.id = str(uuid4())
    USERS.append(user_model)

def list_users() -> Dict:
    return USERS


def get_action_by_id(action_uuid: UUID) -> ActionReq:
    ...