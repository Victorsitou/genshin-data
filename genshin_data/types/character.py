from pydantic import BaseModel
from typing import List, Optional, Tuple, Union, Literal

__all__ = [
    "SkillAttribute",
    "Skill",
    "Passive",
    "Constellation",
    "AscensionMaterial",
    "AscendStat",
    "Ascension",
    "CharacterVoice",
    "TalentMaterial",
    "Character",
    "PartialCharacter",
    "CharacterFields",
]


class SkillAttribute(BaseModel):
    label: str
    values: List[str]


class Skill(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    info: str
    attributes: List[SkillAttribute]


class Passive(BaseModel):
    id: str
    name: str
    description: str
    level: int


class Constellation(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    level: int


class AscensionMaterial(BaseModel):
    _id: int
    id: str
    name: str
    amount: int
    rarity: int


class AscendStat(BaseModel):
    label: str
    values: List[Union[str, int]]  # NOTE: https://github.com/dvaJi/genshin-data/pull/17


class Ascension(BaseModel):
    level: Tuple[int, int]
    cost: Optional[int]
    stats: List[AscendStat]
    mat1: Optional[AscensionMaterial] = None
    mat2: Optional[AscensionMaterial] = None
    mat3: Optional[AscensionMaterial] = None
    mat4: Optional[AscensionMaterial] = None


class CharacterVoice(BaseModel):
    english: str
    chinese: str
    japanese: str
    korean: str


class TalentMaterial(BaseModel):
    level: int
    cost: int
    items: List[AscensionMaterial]


class Character(BaseModel):
    _id: int
    id: str
    name: str
    title: Optional[str]  # NOTE: https://github.com/dvaJi/genshin-data/pull/17
    description: str
    weapon_type: str
    element: str
    gender: str
    substat: str
    affiliation: str
    region: Optional[str]
    rarity: int
    birthday: Tuple[
        Optional[int], Optional[int]
    ]  # NOTE: https://github.com/dvaJi/genshin-data/pull/17
    constellation: str
    domain: str
    cv: CharacterVoice
    skills: List[Skill]
    passives: List[Passive]
    constellations: List[Constellation]
    ascension: List[Ascension]
    talent_materials: List[TalentMaterial]


class PartialCharacter(BaseModel):
    id: str
    name: str


CharacterFields = Literal[
    "id",
    "name",
    "title",
    "description",
    "weapon_type",
    "element",
    "gender",
    "substat",
    "affiliation",
    "region",
    "rarity",
    "birthday",
    "constellation",
    "domain",
    "cv",
    "skills",
    "passives",
    "constellations",
    "ascension",
    "talent_materials",
]
