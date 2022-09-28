from typing import Dict, Any
from uuid import UUID

from src.simple_day.schema import SimpleHabit as SimpleHabitScheme
from src.simple_day.model import SimpleHabit as SimpleHabitModel


def get_habit_by_user(user_uuid: UUID) -> SimpleHabitScheme:
    ...


def add_habit(habit_model: SimpleHabitScheme) -> dict[str, Any]:
    habit_dict = habit_model.dict()
    habit_dict['user'] = str(habit_dict['user'])
    simple = SimpleHabitModel(**habit_dict)
    return simple.save()


def get_habits() -> list[SimpleHabitScheme]:
    ...
