from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = ["Item", "Craft", "TalentLvlUpMaterial", "TalentLvlUpMaterialFields"]


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    cost: int
    items: List[Item]


class TalentLvlUpMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    location: Optional[str]
    rarity: int
    craft: Optional[Craft]
    domain: Optional[str]
    days: Optional[List[str]]


TalentLvlUpMaterialFields = Literal[
    "id",
    "name",
    "description",
    "source",
    "location",
    "rarity",
    "craft",
    "domain",
    "days",
]
