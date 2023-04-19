from enum import Enum

__all__ = ("Language", "Folder")


class Language(str, Enum):
    english = "english"
    spanish = "spanish"
    japanese = "japanese"
    chinese_simplified = "chinese-simplified"
    chinese_traditional = "chinese-traditional"
    french = "french"
    german = "german"
    indonesian = "indonesian"
    italian = "italian"
    korean = "korean"
    portuguese = "portuguese"
    russian = "russian"
    thai = "thai"
    turkish = "turkish"
    vietnamese = "vietnamese"


class Folder(str, Enum):
    achievements = "achievements"
    artifacts = "artifacts"
    bait = "bait"
    character_exp_material = "character_exp_material"
    characters = "characters"
    common_materials = "common_materials"
    domains = "domains"
    elemental_stone_materials = "elemental_stone_materials"
    fish = "fish"
    fishing_rod = "fishing_rod"
    furnishing = "furnishing"
    food = "food"
    ingredients = "ingredients"
    jewels_materials = "jewels_materials"
    local_materials = "local_materials"
    potions = "potions"
    talent_lvl_up_materials = "talent_lvl_up_materials"
    tcg_action = "tcg_action"
    tcg_characters = "tcg_characters"
    tcg_monsters = "tcg_monsters"
    weapon_enhancement_material = "weapon_enhancement_material"
    weapon_primary_materials = "weapon_primary_materials"
    weapon_secondary_materials = "weapon_secondary_materials"
    weapons = "weapons"
