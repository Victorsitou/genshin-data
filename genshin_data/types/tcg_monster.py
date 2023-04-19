from typing import List, Optional, Literal
from pydantic import BaseModel

__all__ = [
    "SkillPoint",
    "Entity",
    "MonsterCardSkill",
    "MonsterCardAttributes",
    "TCGMonsterCard",
    "TCGMonsterCardFields",
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


class MonsterCardSkill(BaseModel):
    id: str
    name: str
    desc: str
    skillTag: List[str]
    points: List[SkillPoint]


class MonsterCardAttributes(BaseModel):
    hp: int
    card_type: str
    energy: int
    element: str
    weapon: str
    faction: List[str]
    monster: Optional[Entity]


class TCGMonsterCard(BaseModel):
    _id: int
    id: str
    name: str
    attributes: MonsterCardAttributes
    skills: List[MonsterCardSkill]


TCGMonsterCardFields = Literal["id", "name", "attributes", "skills"]
