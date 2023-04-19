from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["FurnitureCategory", "FurnitureRecipe", "Furnishing", "FurnishingFields"]


class FurnitureCategory(BaseModel):
    # TODO: cambié este modelo
    id: str
    category: str
    type: Optional[str]


class FurnitureRecipe(BaseModel):
    # TODO: cambié este modelo
    _id: int
    id: str
    name: str
    amount: int


class Furnishing(BaseModel):
    _id: int
    id: str
    originalId: Optional[int]  # TODO: solo aparece una vez en el JSON, issue
    name: str
    description: str
    rarity: int
    load: Optional[int]
    energy: Optional[int]
    exp: Optional[int]
    category: List[FurnitureCategory]
    recipe: Optional[List[FurnitureRecipe]]


FurnishingFields = Literal[
    "id",
    "originalId",
    "name",
    "description",
    "rarity",
    "load",
    "energy",
    "exp",
    "category",
    "recipe",
]
