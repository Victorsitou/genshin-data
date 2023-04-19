from typing import List, Literal
from pydantic import BaseModel

__all__ = [
    "Item",
    "DomainType",
    "Domains",
    "DomainsFields",
]


class Item(BaseModel):
    day: str
    ids: List[str]


class DomainType(BaseModel):
    domainName: str
    rotation: List[Item]


class Domains(BaseModel):
    characters: List[DomainType]
    weapons: List[DomainType]


DomainsFields = Literal[
    "characters",
    "weapons",
]
