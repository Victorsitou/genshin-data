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
    description: Optional[str]  # TODO: es opcional para "Pescado Seco", reportar.
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
