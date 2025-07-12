# world/mygame/__init__.py

import settings
import typing
from .Items import VespadianItem, item_table  # data used below to add items to the World
from .Locations import VespadianLocation, locationTable  # same as above
from .Options import VespadianOptions
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class MyGameSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("MyGame.sfc")


class VespadianWorld(World):
    """Assemble your party of adventurers, delve dungeons, defeat monsters, collect loot, and travel to the distant past to defeat the Dread Sorcerer Ephemeris."""
    game = "Vespadian"  # name of the game/world
    options_dataclass = VespadianOptions  # options the player can set
    options: VespadianOptions  # typing hints for option results
    settings: typing.ClassVar[MyGameSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = locationTable

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "weapons": {"sword", "lance"},
    }