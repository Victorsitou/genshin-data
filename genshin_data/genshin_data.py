import json
import os
import sys
import asyncio
from typing import List, Union, TypeVar, Type, Optional, Any, Dict
from pydantic import BaseModel

from .types import Language, Folder
from .types.character import CharacterFields, Character
from .types.weapon import WeaponFields, Weapon
from .types.artifact import ArtifactFields, Artifact
from .types.common_material import CommonMaterialFields, CommonMaterial
from .types.elemental_stone_materials import (
    ElementalStoneMaterialFields,
    ElementalStoneMaterial,
)
from .types.food import FoodFields, Food
from .types.ingredient import IngredientsFields, Ingredients
from .types.jewel_material import JewelMaterialFields, JewelMaterial
from .types.local_material import LocalMaterialFields, LocalMaterial
from .types.potion import PotionFields, Potion
from .types.talent_lvl_up_material import TalentLvlUpMaterialFields, TalentLvlUpMaterial
from .types.weapon_primary_material import (
    WeaponPrimaryMaterialFields,
    WeaponPrimaryMaterial,
)
from .types.weapon_secondary_material import (
    WeaponSecondaryMaterialFields,
    WeaponSecondaryMaterial,
)
from .types.fishing import (
    FishFields,
    Fish,
    FishingRodFields,
    FishingRod,
    BaitFields,
    Bait,
)
from .types.exp import ExpMaterialFields, ExpMaterial
from .types.achievement import AchievementCategoryFields, AchievementCategory
from .types.furnishing import FurnishingFields, Furnishing
from .types.domain import DomainsFields, Domains
from .types.tcg_character import TCGCharacterCardFields, TCGCharacterCard
from .types.tcg_action import TCGActionCardFields, TCGActionCard
from .types.tcg_monster import TCGMonsterCardFields, TCGMonsterCard

AnyFields = Union[
    CharacterFields,
    WeaponFields,
    ArtifactFields,
    CommonMaterialFields,
    ElementalStoneMaterialFields,
    FoodFields,
    IngredientsFields,
    JewelMaterialFields,
    LocalMaterialFields,
    PotionFields,
    TalentLvlUpMaterialFields,
    WeaponPrimaryMaterialFields,
    WeaponSecondaryMaterialFields,
    FishFields,
    FishingRodFields,
    BaitFields,
    ExpMaterialFields,
    AchievementCategoryFields,
    FurnishingFields,
    DomainsFields,
    TCGCharacterCardFields,
    TCGActionCardFields,
    TCGMonsterCardFields,
]

AnyMaterialFields = Union[
    CommonMaterialFields,
    ElementalStoneMaterialFields,
    JewelMaterialFields,
    LocalMaterialFields,
    PotionFields,
    TalentLvlUpMaterialFields,
    WeaponPrimaryMaterialFields,
    WeaponSecondaryMaterialFields,
    ExpMaterialFields,
]

AnyMaterial = Union[
    CommonMaterial,
    ElementalStoneMaterial,
    JewelMaterial,
    LocalMaterial,
    Potion,
    TalentLvlUpMaterial,
    WeaponPrimaryMaterial,
    WeaponSecondaryMaterial,
    ExpMaterial,
]

AnyTCGCardFields = Union[
    TCGCharacterCardFields, TCGActionCardFields, TCGMonsterCardFields
]
AnyTCGCard = Union[TCGCharacterCard, TCGActionCard, TCGMonsterCard]

T = TypeVar("T", bound=BaseModel)
# TODO: better way to get path?
PATH = os.path.join(os.path.dirname(sys.modules[__name__].__file__))


# TODO: docstrings
# TODO: proper testing for pydantic validation
class GenshinData:
    def __init__(self, language: Language) -> None:
        self._language = language

    @property
    def language(self) -> Language:
        return self._language

    @language.setter
    def language(self, language: Language) -> None:
        self._language = language

    async def findByFolder(
        self, folder: Folder, select: Optional[List[AnyFields]], model: Type[T]
    ) -> List[T]:
        results = (
            json.load(
                open(
                    f"{PATH}/min/data_{self._language.value}.min.json",
                    "r",
                    encoding="utf-8",
                )
            )
        )[folder.value]

        r_models: List[Union[T, BaseModel]] = []
        for result in results:
            try:
                o = model.parse_obj(result)
                if result:
                    r_models.append(self._select_props([o], select)[0])
                else:
                    r_models.append(o)
            except Exception as e:
                print(result)
                raise e

        return r_models

    async def characters(
        self, select: Optional[List[CharacterFields]] = None
    ) -> List[Character]:
        return await self.findByFolder(Folder.characters, select, Character)

    async def weapons(
        self, select: Optional[List[WeaponFields]] = None
    ) -> List[Weapon]:
        return await self.findByFolder(Folder.weapons, select, Weapon)

    async def artifacts(
        self, select: Optional[List[ArtifactFields]] = None
    ) -> List[Artifact]:
        return await self.findByFolder(Folder.artifacts, select, Artifact)

    async def common_materials(
        self, select: Optional[List[CommonMaterialFields]] = None
    ) -> List[CommonMaterial]:
        return await self.findByFolder(Folder.common_materials, select, CommonMaterial)

    async def elemental_stone_materials(
        self, select: Optional[List[ElementalStoneMaterialFields]] = None
    ) -> List[ElementalStoneMaterial]:
        return await self.findByFolder(
            Folder.elemental_stone_materials, select, ElementalStoneMaterial
        )

    async def food(self, select: Optional[List[FoodFields]] = None) -> List[Food]:
        return await self.findByFolder(Folder.food, select, Food)

    async def ingredients(
        self, select: Optional[List[IngredientsFields]] = None
    ) -> List[Ingredients]:
        return await self.findByFolder(Folder.ingredients, select, Ingredients)

    async def jewels_materials(
        self, select: Optional[List[JewelMaterialFields]] = None
    ) -> List[JewelMaterial]:
        return await self.findByFolder(Folder.jewels_materials, select, JewelMaterial)

    async def local_materials(
        self, select: Optional[List[LocalMaterialFields]] = None
    ) -> List[LocalMaterial]:
        return await self.findByFolder(Folder.local_materials, select, LocalMaterial)

    async def potions(
        self, select: Optional[List[PotionFields]] = None
    ) -> List[Potion]:
        return await self.findByFolder(Folder.potions, select, Potion)

    async def talent_lvl_up_materials(
        self, select: Optional[List[TalentLvlUpMaterialFields]] = None
    ) -> List[TalentLvlUpMaterial]:
        return await self.findByFolder(
            Folder.talent_lvl_up_materials, select, TalentLvlUpMaterial
        )

    async def weapon_primary_materials(
        self, select: Optional[List[WeaponPrimaryMaterialFields]] = None
    ) -> List[WeaponPrimaryMaterial]:
        return await self.findByFolder(
            Folder.weapon_primary_materials, select, WeaponPrimaryMaterial
        )

    async def weapon_secondary_materials(
        self, select: Optional[List[WeaponSecondaryMaterialFields]] = None
    ) -> List[WeaponSecondaryMaterial]:
        return await self.findByFolder(
            Folder.weapon_secondary_materials, select, WeaponSecondaryMaterial
        )

    async def fish(self, select: Optional[List[FishFields]] = None) -> List[Fish]:
        return await self.findByFolder(Folder.fish, select, Fish)

    async def fishing_rods(
        self, select: Optional[List[FishingRodFields]] = None
    ) -> List[FishingRod]:
        return await self.findByFolder(Folder.fishing_rod, select, FishingRod)

    async def baits(self, select: Optional[List[BaitFields]] = None) -> List[Bait]:
        return await self.findByFolder(Folder.bait, select, Bait)

    async def character_exp_materials(
        self, select: Optional[List[ExpMaterialFields]] = None
    ) -> List[ExpMaterial]:
        return await self.findByFolder(
            Folder.character_exp_material, select, ExpMaterial
        )

    async def weapon_exp_materials(
        self, select: Optional[List[ExpMaterialFields]] = None
    ) -> List[ExpMaterial]:
        return await self.findByFolder(
            Folder.weapon_enhancement_material, select, ExpMaterial
        )

    async def materials(
        self, select: Optional[List[AnyMaterialFields]] = None
    ) -> List[AnyMaterial]:
        # TODO: improve this?
        r = asyncio.gather(
            self.common_materials(select),
            self.elemental_stone_materials(select),
            self.jewels_materials(select),
            self.local_materials(select),
            self.potions(select),
            self.talent_lvl_up_materials(select),
            self.weapon_primary_materials(select),
            self.weapon_secondary_materials(select),
            self.character_exp_materials(select),
            self.weapon_exp_materials(select),
        )

        while not r.done():
            await asyncio.sleep(0.1)

        return r.result()

    async def achievements(
        self, select: Optional[List[AchievementCategoryFields]] = None
    ) -> List[AchievementCategory]:
        return await self.findByFolder(Folder.achievements, select, AchievementCategory)

    async def furnishings(
        self, select: Optional[List[FurnishingFields]] = None
    ) -> List[Furnishing]:
        return await self.findByFolder(Folder.furnishing, select, Furnishing)

    async def domains(
        self, select: Optional[List[DomainsFields]] = None
    ) -> List[Domains]:
        return await self.findByFolder(Folder.domains, select, Domains)

    async def tcg_characters(
        self, select: Optional[List[TCGCharacterCardFields]] = None
    ) -> List[TCGCharacterCard]:
        return await self.findByFolder(Folder.tcg_characters, select, TCGCharacterCard)

    async def tcg_actions(
        self, select: Optional[List[TCGActionCardFields]] = None
    ) -> List[TCGActionCard]:
        return await self.findByFolder(Folder.tcg_action, select, TCGActionCard)

    async def tcg_monsters(
        self, select: Optional[List[TCGMonsterCardFields]] = None
    ) -> List[TCGMonsterCard]:
        return await self.findByFolder(Folder.tcg_monsters, select, TCGMonsterCard)

    async def tcg_cards(
        self, select: Optional[List[AnyTCGCardFields]] = None
    ) -> List[AnyTCGCard]:
        r = asyncio.gather(
            self.tcg_characters(select),
            self.tcg_actions(select),
            self.tcg_monsters(select),
        )

        while not r.done():
            await asyncio.sleep(0.1)

        return r.result()

    def _select_props(
        self, results: List[Type[T]], select: Optional[List[str]]
    ) -> List[BaseModel]:
        if select is None:
            return results

        data: List[Dict[str, Any]] = []
        models: List[BaseModel] = []
        for result in results:
            try:
                data.append({prop: getattr(result, prop) for prop in select})
            except AttributeError as e:
                raise ValueError(f"Invalid property name: {e.name}")

        for d in data:
            models.append(BaseModel.construct(select, **d))

        return models
