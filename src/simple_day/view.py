from uuid import UUID

from fastapi import APIRouter

from .service import get_habit_by_user, get_habits, add_habit
from .schema import SimpleHabit

router = APIRouter()


@router.get("/habits/{user_uuid}")
def get_user(user_uuid: UUID):
    return get_habit_by_user(user_uuid)


@router.get("/habits")
def list_habits():
    return get_habits()


@router.post("/habits")
def create_user(user: SimpleHabit):
    return add_habit(user)
