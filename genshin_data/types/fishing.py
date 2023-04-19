from typing import List, Literal
from pydantic import BaseModel

__all__ = [
    "CraftItem",
    "Craft",
    "FishBait",
    "Fish",
    "FishingRod",
    "Bait",
    "FishFields",
    "FishingRodFields",
    "BaitFields",
]


class CraftItem(BaseModel):
    id: str
    name: str
    amount: int


class Craft(BaseModel):
    items: List[CraftItem]
    result: int


class FishBait(BaseModel):
    id: str
    name: str
    rarity: int


class Fish(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    rarity: int
    source: List[str]
    bait: FishBait


class FishingRod(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    rarity: int
    source: List[str]


class Bait(BaseModel):
    _id: int
    id: str
    name: str
    description: str
    rarity: int
    craft: Craft
    fish: List[FishBait]


FishFields = Literal[
    "id",
    "name",
    "description",
    "rarity",
    "source",
    "bait",
]

FishingRodFields = Literal[
    "id",
    "name",
    "description",
    "rarity",
    "source",
]

BaitFields = Literal[
    "id",
    "name",
    "description",
    "rarity",
    "craft",
    "fish",
]
