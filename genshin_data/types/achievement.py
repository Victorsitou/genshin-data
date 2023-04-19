from typing import List, Literal
from pydantic import BaseModel

__all__ = ["Achievement", "AchievementCategory", "AchievementCategoryFields"]


class Achievement(BaseModel):
    id: int
    name: str
    desc: str
    reward: int
    hidden: bool
    order: int


class AchievementCategory(BaseModel):
    _id: int
    id: str
    name: str
    order: int
    achievements: List[Achievement]


AchievementCategoryFields = Literal["id", "name", "order", "achievements"]
