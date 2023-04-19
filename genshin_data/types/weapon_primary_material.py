from typing import List, Optional, Literal
from pydantic import BaseModel


class Item(BaseModel):
    _id: int
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    cost: int
    items: List[Item]


class WeaponPrimaryMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    location: str
    rarity: int
    craft: Optional[Craft]
    domain: str
    days: List[str]


WeaponPrimaryMaterialFields = Literal[
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
