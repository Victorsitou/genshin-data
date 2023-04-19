from typing import List, Literal
from pydantic import BaseModel

__all__ = ["ElementalStoneMaterial", "ElementalStoneMaterialFields"]


class ElementalStoneMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    rarity: int


ElementalStoneMaterialFields = Literal["id", "name", "description", "source", "rarity"]
