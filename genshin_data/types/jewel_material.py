from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["Item", "Craft", "JewelMaterial", "JewelMaterialFields"]


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    cost: int
    items: List[Item]


class JewelMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    rarity: int
    craft: Optional[Craft]
    convert: Optional[List[List[Item]]]


JewelMaterialFields = Literal[
    "id",
    "name",
    "description",
    "source",
    "rarity",
    "craft",
    "convert",
]
