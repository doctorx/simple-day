from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class UserReq(BaseModel):
    id: UUID
    name: str
    active: bool

class ActionReq(BaseModel):
    id: UUID
    name: str 
    value: int | float
    measurement: str
    feel: int
    created_date: datetime
    user_uuid: UUID