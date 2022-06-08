import random
from typing import List

from rpg.generics import ItemStats, EntityStats, Item
from rpg.utils import load_json_into_object


class Weapon(Item):

    def __init__(self, name: str, level: int, rarity: int, damage_stats: ItemStats):
        super().__init__(name, level, rarity)
        self.damage_stats = damage_stats


class WeaponFactory:
    """ create at init time, loads a bunch of stats from a json and then generates weapons with those stats """

    def __init__(self, weapon_class_name: str, weapon_class_config: dict):
        self.weapon_class_name: str = weapon_class_name
        self.names: List[str] = weapon_class_config["names"]
        self.multipliers: ItemStats = ItemStats()
        load_json_into_object(weapon_class_config["multipliers"], self.multipliers)
        self.default_scaling: EntityStats = EntityStats()
        load_json_into_object(weapon_class_config["scaling"], self.default_scaling)

    def generate(self, level: int, rarity: int):
        name = random.choice(self.names)
        # TODO
