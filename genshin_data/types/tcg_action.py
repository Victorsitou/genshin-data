from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = [
    "ActionCardSkill",
    "Entity",
    "Attributes",
    "TCGActionCard",
    "TCGActionCardFields",
]


class ActionCardSkill(BaseModel):
    name: str
    desc: str


class Entity(BaseModel):
    _id: int
    id: str
    name: str
    rarity: Optional[int]  # TODO: issue


class Attributes(BaseModel):
    cost: int
    cost_type: Optional[str]  # TODO: issue
    card_type: str
    source: Optional[List[str]]  # TODO: issue
    artifact: Optional[Entity]
    character: Optional[Entity]
    food: Optional[Entity]
    weapon: Optional[Entity]
    tags: Optional[List[str]]  # TODO: issue


class TCGActionCard(BaseModel):
    _id: int
    id: str
    name: str
    title: str
    desc: str
    attributes: Attributes
    skills: List[ActionCardSkill]


TCGActionCardFields = Literal["id", "name", "title", "desc", "attributes", "skills"]
