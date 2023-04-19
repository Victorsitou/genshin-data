from typing import Optional, Literal

from pydantic import BaseModel

__all__ = ["ArtifactSet", "Artifact", "ArtifactFields"]


class ArtifactSet(BaseModel):
    _id: int
    id: str
    name: str
    description: Optional[str]


class Artifact(BaseModel):
    _id: int
    id: str
    name: str
    min_rarity: int
    max_rarity: int
    flower: Optional[ArtifactSet]
    plume: Optional[ArtifactSet]
    sands: Optional[ArtifactSet]
    goblet: Optional[ArtifactSet]
    circlet: Optional[ArtifactSet]
    one_pc: Optional[str]
    two_pc: Optional[str]
    four_pc: Optional[str]


ArtifactFields = Literal[
    "id",
    "name",
    "min_rarity",
    "max_rarity",
    "flower",
    "plume",
    "sands",
    "goblet",
    "circlet",
    "one_pc",
    "two_pc",
    "four_pc",
]
