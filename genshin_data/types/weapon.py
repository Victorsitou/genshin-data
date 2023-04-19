from typing import List, Optional, Literal
from pydantic import BaseModel


class AscensionMaterial(BaseModel):
    _id: int
    id: str
    name: str
    amount: int
    rarity: int


class WeaponAscension(BaseModel):
    ascension: int
    level: int
    cost: Optional[int]  # NOTE: https://github.com/dvaJi/genshin-data/issues/10
    materials: List[AscensionMaterial]


class WeaponRefinement(BaseModel):
    refinement: int
    desc: str


class StatLevel(BaseModel):
    ascension: int
    level: int
    primary: int
    secondary: Optional[int]


class WeaponStat(BaseModel):
    primary: str
    secondary: Optional[str]
    levels: List[StatLevel]


class Weapon(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    rarity: int
    type: str
    domain: str
    passive: str
    bonus: str
    stats: WeaponStat
    ascensions: List[WeaponAscension]
    refinements: List[WeaponRefinement]


WeaponFields = Literal[
    "id",
    "name",
    "description",
    "rarity",
    "type",
    "domain",
    "passive",
    "bonus",
    "stats",
    "ascensions",
    "refinements",
]
