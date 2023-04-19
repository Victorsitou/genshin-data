from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["Item", "Craft", "CommonMaterial", "CommonMaterialFields"]


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    cost: int
    items: List[Item]


class CommonMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    rarity: int
    craft: Optional[Craft] = None


CommonMaterialFields = Literal[
    "id",
    "name",
    "description",
    "source",
    "rarity",
    "craft",
]
