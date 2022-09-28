from datetime import datetime
from pydantic import BaseModel, UUID4


class SimpleHabit(BaseModel):
    user: UUID4
    date: datetime
    action: str
    entity: str
    measurement_value: int | float
    measurement: str
    feel: int
    complete: bool

