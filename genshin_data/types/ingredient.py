from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["Item", "Recipe", "Ingredients", "IngredientsFields"]


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Recipe(BaseModel):
    _id: int
    id: str
    name: str


class Ingredients(BaseModel):
    _id: int
    id: str
    name: str
    description: Optional[str]  # TODO: https://github.com/dvaJi/genshin-data/issues/15
    processing: Optional[List[Item]]
    recipes: Optional[List[Recipe]]
    source: Optional[List[str]]


IngredientsFields = Literal[
    "id",
    "name",
    "description",
    "processing",
    "recipes",
    "source",
]
