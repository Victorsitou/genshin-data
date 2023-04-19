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


class WeaponSecondaryMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    rarity: int
    craft: Optional[Craft]


WeaponSecondaryMaterialFields = Literal[
    "id",
    "name",
    "description",
    "source",
    "rarity",
    "craft",
]
