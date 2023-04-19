from typing import List, Literal
from pydantic import BaseModel

__all__ = ["Item", "Craft", "Potion", "PotionFields"]


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    cost: int
    items: List[Item]


class Potion(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    effect: str
    rarity: int
    craft: Craft


PotionFields = Literal["id", "name", "description", "effect", "rarity", "craft"]
