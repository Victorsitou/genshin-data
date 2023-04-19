from typing import List, Optional, Literal
from pydantic import BaseModel

from .character import PartialCharacter

__all__ = ["Ingredient", "FoodResult", "Food", "FoodFields"]


class Ingredient(BaseModel):
    id: str
    name: str
    amount: int


class _FoodResult(BaseModel):
    _id: int
    name: str
    description: str
    effect: str
    character: Optional[PartialCharacter]


class FoodResult(BaseModel):
    normal: _FoodResult
    delicious: _FoodResult
    suspicious: _FoodResult
    special: Optional[_FoodResult]


class Food(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    ingredients: List[Ingredient]
    dish_type: str
    results: FoodResult
    rarity: int


FoodFields = Literal[
    "id",
    "name",
    "description",
    "ingredients",
    "dish_type",
    "results",
    "rarity",
]
