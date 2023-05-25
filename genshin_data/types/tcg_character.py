from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = [
    "SkillPoint",
    "Entity",
    "CharacterCardSkill",
    "Attributes",
    "TCGCharacterCard",
    "TCGCharacterCardFields",
]


class SkillPoint(BaseModel):
    _id: int
    id: str
    type: str
    count: int


class Entity(BaseModel):
    _id: int
    id: str
    name: str


class CharacterCardSkill(BaseModel):
    id: str
    name: str
    desc: str
    skillTag: List[str]
    points: List[SkillPoint]


class Attributes(BaseModel):
    hp: int
    card_type: str
    energy: int
    element: str
    weapon: str
    faction: List[str]
    talent_card: Optional[Entity]
    source: str
    character: Optional[Entity]


class TCGCharacterCard(BaseModel):
    _id: int
    id: str
    name: str
    attributes: Attributes
    skills: List[CharacterCardSkill]


TCGCharacterCardFields = Literal["id", "name", "attributes", "skills"]
