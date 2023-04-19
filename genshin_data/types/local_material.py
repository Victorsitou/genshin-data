from typing import List, Literal
from pydantic import BaseModel

__all__ = ["LocalMaterial", "LocalMaterialFields"]


class LocalMaterial(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    source: List[str]
    location: str


LocalMaterialFields = Literal["id", "name", "description", "source", "location"]
