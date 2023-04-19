from typing import Literal
from pydantic import BaseModel

__all__ = ["ExpMaterial", "ExpMaterialFields"]


class ExpMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    rarity: int
    exp: int


ExpMaterialFields = Literal[
    "id",
    "name",
    "description",
    "rarity",
    "exp",
]
