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
    cost: Optional[int]
    materials: List[AscensionMaterial]


class WeaponRefinement(BaseModel):
    refinement: int
    desc: str


class RawWeaponRefinement(BaseModel):
    template: str
    params: List[List[str]]
    name: str  # NOTE: https://github.com/dvaJi/genshin-data/pull/17


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
    refinement_raw: RawWeaponRefinement
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
    "refinement_raw",
    "refinements",
]
