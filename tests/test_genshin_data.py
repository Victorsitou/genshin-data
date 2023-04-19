import pytest

import genshin_data


@pytest.mark.asyncio
class TestGenshinData:
    @pytest.fixture(autouse=True)
    def data(self):
        self.genshin_data = genshin_data.GenshinData(genshin_data.Language.spanish)

    async def test_class(self):
        assert self.genshin_data.language == genshin_data.Language.spanish

    async def test_characters(self):
        await self.genshin_data.characters()

        await self.genshin_data.characters(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.characters(["invalid"])  # type: ignore

    async def test_weapons(self):
        await self.genshin_data.weapons()

        await self.genshin_data.weapons(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.weapons(["invalid"])  # type: ignore

    async def test_artifacts(self):
        await self.genshin_data.artifacts()

        await self.genshin_data.artifacts(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.artifacts(["invalid"])  # type: ignore

    async def test_common_materials(self):
        await self.genshin_data.common_materials()

        await self.genshin_data.common_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.common_materials(["invalid"])  # type: ignore

    async def test_elemental_stone_materials(self):
        await self.genshin_data.elemental_stone_materials()

        await self.genshin_data.elemental_stone_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.elemental_stone_materials(["invalid"])  # type: ignore

    async def test_food(self):
        await self.genshin_data.food()

        await self.genshin_data.food(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.food(["invalid"])  # type: ignore

    async def test_ingredients(self):
        await self.genshin_data.ingredients()

        await self.genshin_data.ingredients(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.ingredients(["invalid"])  # type: ignore

    async def test_jewel_materials(self):
        await self.genshin_data.jewels_materials()

        await self.genshin_data.jewels_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.jewels_materials(["invalid"])  # type: ignore

    async def test_local_materials(self):
        await self.genshin_data.local_materials()

        await self.genshin_data.local_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.local_materials(["invalid"])  # type: ignore

    async def test_potions(self):
        await self.genshin_data.potions()

        await self.genshin_data.potions(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.potions(["invalid"])  # type: ignore

    async def test_talent_lvl_up_materials(self):
        await self.genshin_data.talent_lvl_up_materials()

        await self.genshin_data.talent_lvl_up_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.talent_lvl_up_materials(["invalid"])  # type: ignore

    async def test_weapon_primary_materials(self):
        await self.genshin_data.weapon_primary_materials()

        await self.genshin_data.weapon_primary_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.weapon_primary_materials(["invalid"])  # type: ignore

    async def test_weapon_secondary_materials(self):
        await self.genshin_data.weapon_secondary_materials()

        await self.genshin_data.weapon_secondary_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.weapon_secondary_materials(["invalid"])  # type: ignore

    async def test_fish(self):
        await self.genshin_data.fish()

        await self.genshin_data.fish(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.fish(["invalid"])  # type: ignore

    async def test_fishing_rods(self):
        await self.genshin_data.fishing_rods()

        await self.genshin_data.fishing_rods(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.fishing_rods(["invalid"])  # type: ignore

    async def test_baits(self):
        await self.genshin_data.baits()

        await self.genshin_data.baits(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.baits(["invalid"])  # type: ignore

    async def test_character_exp_materials(self):
        await self.genshin_data.character_exp_materials()

        await self.genshin_data.character_exp_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.character_exp_materials(["invalid"])  # type: ignore

    async def test_weapon_exp_materials(self):
        await self.genshin_data.weapon_exp_materials()

        await self.genshin_data.weapon_exp_materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.weapon_exp_materials(["invalid"])  # type: ignore

    async def test_materials(self):
        await self.genshin_data.materials()

        await self.genshin_data.materials(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.materials(["invalid"])  # type: ignore

    async def test_achievements(self):
        await self.genshin_data.achievements()

        await self.genshin_data.achievements(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.achievements(["invalid"])  # type: ignore

    async def test_furnishings(self):
        await self.genshin_data.furnishings()

        await self.genshin_data.furnishings(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.furnishings(["invalid"])  # type: ignore

    async def test_domains(self):
        await self.genshin_data.domains()

        await self.genshin_data.domains(["characters"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.domains(["invalid"])  # type: ignore

    async def test_tcg_characters(self):
        await self.genshin_data.tcg_characters()

        await self.genshin_data.tcg_characters(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.tcg_characters(["invalid"])  # type: ignore

    async def test_tcg_actions(self):
        await self.genshin_data.tcg_actions()

        await self.genshin_data.tcg_actions(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.tcg_actions(["invalid"])  # type: ignore

    async def test_tcg_monsters(self):
        await self.genshin_data.tcg_monsters()

        await self.genshin_data.tcg_monsters(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.tcg_monsters(["invalid"])  # type: ignore

    async def test_tcg_cards(self):
        await self.genshin_data.tcg_cards()

        await self.genshin_data.tcg_cards(["name"])

        with pytest.raises((ValueError, AttributeError)):
            await self.genshin_data.tcg_cards(["invalid"])  # type: ignore
