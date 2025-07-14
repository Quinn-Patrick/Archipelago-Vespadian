# world/mygame/__init__.py

from typing import List
from .Items import VespadianItem, get_items_by_category, item_table, item_name_groups, event_item_table  # data used below to add items to the World
from .Locations import location_table, location_name_groups  # same as above
from .Options import VespadianOptions
from .Regions import connect_entrances, create_regions
from .Rules import set_rules
from worlds.AutoWorld import World

class VespadianWorld(World):
    """Assemble your party of adventurers, delve dungeons, defeat monsters, collect loot, and travel to the distant past to defeat the Dread Sorcerer Ephemeris."""
    game = "Vespadian"  # name of the game/world
    options_dataclass = VespadianOptions  # options the player can set
    options: VespadianOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = item_name_groups

    location_name_groups = location_name_groups
    fillers = {}
    fillers.update(get_items_by_category("Item"))
    fillers.update(get_items_by_category("Equipment"))
    fillers.update(get_items_by_category("Tome"))

    def create_items(self):
        item_pool: List[VespadianItem] = []
        non_filler_item_categories = ["Key", "Strong Equipment", "Strong Tome"]

        for name, data in item_table.items():
            if data.category not in non_filler_item_categories:
                continue
            item_pool += [self.create_item(name)]
        
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.get_location("Defeat Ephemeris", self.player).place_locked_item(self.create_item("Victory"))
        
        self.multiworld.itempool += item_pool


    def create_item(self, name: str) -> VespadianItem:
        data = item_table[name]
        return VespadianItem(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> VespadianItem:
        data = event_item_table[name]
        return VespadianItem(name, data.classification, data.code, self.player)

    def set_rules(self):
        print("Setting rules.")
        print("Connected entrances: " + str(list(self.get_entrances())))
        set_rules(self)

    def create_regions(self):
        print("Creating regions.")
        create_regions(self.multiworld, self.player, self.options)
        print("Done creating regions.")

    def connect_entrances(self):
        print("Connecting entrances.")
        connect_entrances(self.multiworld, self.player)
        print("Connected entrances: " + str(list(self.get_entrances())))
        
    def get_filler_item_name(self) -> str:
        return self.random.choices([filler for filler in self.fillers.keys()])[0]