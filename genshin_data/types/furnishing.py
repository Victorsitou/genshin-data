from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["FurnitureCategory", "FurnitureRecipe", "Furnishing", "FurnishingFields"]


class FurnitureCategory(BaseModel):
    # NOTE: https://github.com/dvaJi/genshin-data/pull/17
    id: str
    category: str
    type: Optional[str]


class FurnitureRecipe(BaseModel):
    # NOTE: https://github.com/dvaJi/genshin-data/pull/17
    _id: int
    id: str
    name: str
    amount: str


class Furnishing(BaseModel):
    _id: int
    id: str
    originalId: Optional[int]  # NOTE: https://github.com/dvaJi/genshin-data/issues/14
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
