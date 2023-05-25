from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = [
    "ActionCardSkill",
    "Entity",
    "Attributes",
    "TCGActionCard",
    "TCGActionCardFields",
]


class Energy(BaseModel):
    _id: int
    id: str
    type: str
    count: int


class ActionCardSkill(BaseModel):
    name: str
    desc: str


class Entity(BaseModel):
    _id: int
    id: str
    name: str
    rarity: int


class Attributes(BaseModel):
    cost: int
    cost_type: Optional[str]  # TODO: https://github.com/dvaJi/genshin-data/issues/16
    card_type: str
    energy: List[Energy]
    source: Optional[str]  # TODO: https://github.com/dvaJi/genshin-data/issues/16
    artifact: Optional[Entity]
    character: Optional[Entity]
    food: Optional[Entity]
    weapon: Optional[Entity]
    tags: Optional[List[str]]  # TODO: https://github.com/dvaJi/genshin-data/issues/16


class TCGActionCard(BaseModel):
    _id: int
    id: str
    name: str
    title: str
    desc: str
    in_play_description: str
    attributes: Attributes
    skills: List[ActionCardSkill]


TCGActionCardFields = Literal[
    "id", "name", "title", "desc", "in_play_description", "attributes", "skills"
]
