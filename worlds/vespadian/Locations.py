from BaseClasses import Location

from typing import Dict, NamedTuple, Optional, Set
import typing

class VespadianLocation(Location):
    game: str = "Vespadian"

class VespadianLocationData(NamedTuple):
    category: str
    code: int

def get_locations_by_category(category: str) -> Dict[str, VespadianLocationData]:
    location_dict: Dict[str, VespadianLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: dict[str, VespadianLocationData] = {
    #Menendel Underground Chests:
    "Menendel Underground Corridors Chest 1": VespadianLocationData("Menendel Underground", 1_220),
    "Menendel Underground Corridors Chest 2": VespadianLocationData("Menendel Underground", 1_221),
    "Menendel Underground Corridors Chest 3": VespadianLocationData("Menendel Underground", 1_222),
    "Menendel Underground Corridors Chest 4": VespadianLocationData("Menendel Underground", 1_223),
    "Menendel Underground Corridors Key Chest": VespadianLocationData("Menendel Underground", 1_224), ##Blocked by tunnel key
    "Menendel Underground East Tunnel Chest 1": VespadianLocationData("Menendel Underground", 1_225),
    "Menendel Underground East Tunnel Chest 2": VespadianLocationData("Menendel Underground", 1_226),
    "Menendel Underground East Tunnel Chest 3": VespadianLocationData("Menendel Underground", 1_227),
    "Menendel Underground East Tunnel Chest 4": VespadianLocationData("Menendel Underground", 1_228),
    "Menendel Underground West Tunnel Chest 1": VespadianLocationData("Menendel Underground", 1_229),
    "Menendel Underground West Tunnel Chest 2": VespadianLocationData("Menendel Underground", 1_230),
    "Menendel Underground Vault Chest 1": VespadianLocationData("Menendel Underground", 1_231),
    "Menendel Underground Vault Chest 2": VespadianLocationData("Menendel Underground", 1_232),
    "Menendel Underground Vault Chest 3": VespadianLocationData("Menendel Underground", 1_233),
    "Menendel Underground Vault Chest 4": VespadianLocationData("Menendel Underground", 1_234),

    #Moonlit Shrine Chests:
    "Moonlit Shrine Antechamber Chest 1": VespadianLocationData("Moonlit Shrine", 1_235),
    "Moonlit Shrine Antechamber Chest 2": VespadianLocationData("Moonlit Shrine", 1_236),
    "Moonlit Shrine Antechamber Chest 3": VespadianLocationData("Moonlit Shrine", 1_237),
    "Moonlit Shrine Antechamber Chest 4": VespadianLocationData("Moonlit Shrine", 1_238),
    "Moonlit Shrine Antechamber Chest 5": VespadianLocationData("Moonlit Shrine", 1_239),
    "Moonlit Shrine Antechamber Chest 6": VespadianLocationData("Moonlit Shrine", 1_240),
    "Moonlit Shrine Antechamber Chest 7": VespadianLocationData("Moonlit Shrine", 1_241),
    "Moonlit Shrine Antechamber Chest 8": VespadianLocationData("Moonlit Shrine", 1_242),
    "Moonlit Shrine Antechamber Chest 9": VespadianLocationData("Moonlit Shrine", 1_243),
    "Moonlit Shrine Antechamber Chest 10": VespadianLocationData("Moonlit Shrine", 1_244),
    "Moonlit Shrine Mount Chest 1": VespadianLocationData("Moonlit Shrine", 1_245),
    "Moonlit Shrine Mount Chest 2": VespadianLocationData("Moonlit Shrine", 1_246),
    "Moonlit Shrine Mount Chest 3": VespadianLocationData("Moonlit Shrine", 1_247),
    "Moonlit Shrine Mount Chest 4": VespadianLocationData("Moonlit Shrine", 1_248),
    "Moonlit Shrine Mount Chest 5": VespadianLocationData("Moonlit Shrine", 1_249),
    "Moonlit Shrine Mount Chest 6": VespadianLocationData("Moonlit Shrine", 1_250),

    #Mole Hole Chests:
    "Mole Hole Ground Level Chest 1": VespadianLocationData("Mole Hole", 1_251),
    "Mole Hole Ground Level Chest 2": VespadianLocationData("Mole Hole", 1_252),
    "Mole Hole Ground Level Chest 3": VespadianLocationData("Mole Hole", 1_253),
    "Mole Hole Ground Level Chest 4": VespadianLocationData("Mole Hole", 1_254),
    "Mole Hole Ground Level Chest 5": VespadianLocationData("Mole Hole", 1_255),
    "Mole Hole Ground Depths Key Chest": VespadianLocationData("Mole Hole", 1_256), #Blocked by Mole Key
    "Mole Hole Ground Depths Chest 1": VespadianLocationData("Mole Hole", 1_257),
    "Rescue Ariadne": VespadianLocationData("Mole Hole", 2_442),

    #Hearthaven Chests:
    "Hearthaven South Chest": VespadianLocationData("Hearthaven", 1_215),
    "Hearthaven North Chest 1": VespadianLocationData("Hearthaven", 1_045),
    "Hearthaven North Chest 2": VespadianLocationData("Hearthaven", 1_046),
    "Hearthaven Crafting Shop Chest": VespadianLocationData("Hearthaven", 1_289),
    "Hearthaven Library Chest": VespadianLocationData("Hearthaven", 1_044),
    "Gift From Maria": VespadianLocationData("Hearthaven", 1_382),

    #Island Fortress Chests:
    "Island Fortress Keep Chest 1": VespadianLocationData("Island Fortress", 1_260),
    "Island Fortress Keep Chest 2": VespadianLocationData("Island Fortress", 1_261),
    "Island Fortress Keep Chest 3": VespadianLocationData("Island Fortress", 1_262),
    "Island Fortress Keep Chest 4": VespadianLocationData("Island Fortress", 1_263),
    "Island Fortress Keep Chest 5": VespadianLocationData("Island Fortress", 1_264),
    "Island Fortress Keep Chest 6": VespadianLocationData("Island Fortress", 1_265),
    "Island Fortress Keep Chest 7": VespadianLocationData("Island Fortress", 1_266),
    "Island Fortress Keep Chest 8": VespadianLocationData("Island Fortress", 1_267),
    "Island Fortress Keep Chest 9": VespadianLocationData("Island Fortress", 1_268),
    "Island Fortress Keep Chest 10": VespadianLocationData("Island Fortress", 1_269),
    "Island Fortress Keep Chest 11": VespadianLocationData("Island Fortress", 1_270),
    "Island Fortress Keep Chest 12": VespadianLocationData("Island Fortress", 1_271),
    "Island Fortress Keep Chest 13": VespadianLocationData("Island Fortress", 1_272),
    "Island Fortress Keep Chest 14": VespadianLocationData("Island Fortress", 1_273),
    "Island Fortress Keep Chest 15": VespadianLocationData("Island Fortress", 1_274),
    "Island Fortress Keep Chest 16": VespadianLocationData("Island Fortress", 1_281),
    "Island Fortress Basement Chest 1": VespadianLocationData("Island Fortress", 1_275),
    "Island Fortress Basement Chest 2": VespadianLocationData("Island Fortress", 1_276),
    "Island Fortress Basement Chest 3": VespadianLocationData("Island Fortress", 1_277),
    "Island Fortress Hallway Silver Key Chest": VespadianLocationData("Island Fortress", 1_385), #Blocked by Silver Key
    "Island Fortress Towers Chest 1": VespadianLocationData("Island Fortress", 1_278),
    "Island Fortress Towers Chest 2": VespadianLocationData("Island Fortress", 1_279),
    "Island Fortress Towers Chest 3": VespadianLocationData("Island Fortress", 1_259),
    "Island Fortress Towers Chest 4": VespadianLocationData("Island Fortress", 1_280), #Blocked by Fortress Key

    #Farsight Chests:
    "Farsight Inn Chest 1": VespadianLocationData("Farsight", 1_380),
    "Farsight Inn Chest 2": VespadianLocationData("Farsight", 1_381),

    #Bottomless Hole Chests:
    "Bottomless Hole B1 Chest": VespadianLocationData("Bottomless Hole", 1_144),
    "Bottomless Hole B3 Chest 1": VespadianLocationData("Bottomless Hole", 1_145),
    "Bottomless Hole B3 Chest 2": VespadianLocationData("Bottomless Hole", 1_146),
    "Bottomless Hole B3 Chest 3": VespadianLocationData("Bottomless Hole", 1_147),
    "Bottomless Hole B3 Chest 4": VespadianLocationData("Bottomless Hole", 1_148),
    "Bottomless Hole B3 Chest 5": VespadianLocationData("Bottomless Hole", 1_149),
    "Bottomless Hole B3 Chest 6": VespadianLocationData("Bottomless Hole", 1_150),
    "Bottomless Hole B4 Chest 1": VespadianLocationData("Bottomless Hole", 1_151),
    "Bottomless Hole B4 Chest 2": VespadianLocationData("Bottomless Hole", 1_152),
    "Bottomless Hole B4 Chest 3": VespadianLocationData("Bottomless Hole", 1_153),
    "Bottomless Hole B4 Chest 4": VespadianLocationData("Bottomless Hole", 1_154),
    "Bottomless Hole B4 Chest 5": VespadianLocationData("Bottomless Hole", 1_155),
    "Bottomless Hole B4 Chest 6": VespadianLocationData("Bottomless Hole", 1_156),
    "Bottomless Hole B4 Chest 7": VespadianLocationData("Bottomless Hole", 1_157),
    "Bottomless Hole B5 Chest 1": VespadianLocationData("Bottomless Hole", 1_143),
    "Bottomless Hole B5 Chest 2": VespadianLocationData("Bottomless Hole", 1_158),
    "Bottomless Hole B5 Chest 3": VespadianLocationData("Bottomless Hole", 1_159),
    "Bottomless Hole B5 Chest 4": VespadianLocationData("Bottomless Hole", 1_160),
    "Bottomless Hole B5 Chest 5": VespadianLocationData("Bottomless Hole", 1_161),
    "Bottomless Hole Bottom Chest 1": VespadianLocationData("Bottomless Hole", 1_386), #Silver Key Blocked
    "Bottomless Hole Bottom Chest 2": VespadianLocationData("Bottomless Hole", 1_387), #Silver Key Blocked
    "Bottomless Hole Bottom Chest 3": VespadianLocationData("Bottomless Hole", 1_388), #Silver Key Blocked

    #The Great Between Chests:
    "The Great Between: Web of Worlds Chest 1": VespadianLocationData("The Great Between", 1_285),
    "The Great Between: Web of Worlds Chest 2": VespadianLocationData("The Great Between", 1_286),
    "The Great Between: Web of Worlds Chest 3": VespadianLocationData("The Great Between", 1_287),
    "The Great Between: Web of Worlds Chest 4": VespadianLocationData("The Great Between", 1_288),
    "The Great Between: Isles of Thought Chest 1": VespadianLocationData("The Great Between", 1_282),
    "The Great Between: Isles of Thought Chest 2": VespadianLocationData("The Great Between", 1_283),
    "The Great Between: Isles of Thought Chest 3": VespadianLocationData("The Great Between", 1_284),

    #Arva Mandia Chests:
    "Arva Mandia General Store Chest": VespadianLocationData("Arva Mandia", 1_290),

    #Ancient Catacombs Chests:
    "Ancient Catacombs East Tunnel Chest 1": VespadianLocationData("Ancient Catacombs", 1_006),
    "Ancient Catacombs East Tunnel Chest 2": VespadianLocationData("Ancient Catacombs", 1_291),
    "Ancient Catacombs Cistern Chest 1": VespadianLocationData("Ancient Catacombs", 1_012),
    "Ancient Catacombs Cistern Chest 2": VespadianLocationData("Ancient Catacombs", 1_016),
    "Ancient Catacombs Cistern Chest 3": VespadianLocationData("Ancient Catacombs", 1_014),
    "Ancient Catacombs Cistern Chest 4": VespadianLocationData("Ancient Catacombs", 1_015),
    "Ancient Catacombs Cistern Chest 5": VespadianLocationData("Ancient Catacombs", 1_013),
    "Ancient Catacombs Cistern Chest 6": VespadianLocationData("Ancient Catacombs", 1_011),
    "Ancient Catacombs Cistern Chest 7": VespadianLocationData("Ancient Catacombs", 1_010),
    "Ancient Catacombs Cistern Chest 8": VespadianLocationData("Ancient Catacombs", 1_007),
    "Ancient Catacombs Cistern Chest 9": VespadianLocationData("Ancient Catacombs", 1_009),
    "Ancient Catacombs Cistern Chest 10": VespadianLocationData("Ancient Catacombs", 1_008),
    "Ancient Catacombs North Tunnel Chest 1": VespadianLocationData("Ancient Catacombs", 1_017),
    "Ancient Catacombs North Tunnel Chest 2": VespadianLocationData("Ancient Catacombs", 1_018),
    "Ancient Catacombs North Tunnel Chest 3": VespadianLocationData("Ancient Catacombs", 1_019),
    "Ancient Catacombs North Tunnel Chest 4": VespadianLocationData("Ancient Catacombs", 1_020),
    "Ancient Catacombs Artery Chest 1": VespadianLocationData("Ancient Catacombs", 1_292),
    "Ancient Catacombs Artery Chest 2": VespadianLocationData("Ancient Catacombs", 1_293),
    "Ancient Catacombs Artery Chest 3": VespadianLocationData("Ancient Catacombs", 1_294),
    "Ancient Catacombs Artery Chest 4": VespadianLocationData("Ancient Catacombs", 1_295),
    "Ancient Catacombs Artery Chest 5": VespadianLocationData("Ancient Catacombs", 1_296),
    "Ancient Catacombs Artery Chest 6": VespadianLocationData("Ancient Catacombs", 1_297),
    "Ancient Catacombs Artery Chest 7": VespadianLocationData("Ancient Catacombs", 1_298),
    "Ancient Catacombs Treasury Chest": VespadianLocationData("Ancient Catacombs", 1_390),
    "Ancient Catacombs Antechamber Chest 1": VespadianLocationData("Ancient Catacombs", 1_002),
    "Ancient Catacombs Antechamber Chest 2": VespadianLocationData("Ancient Catacombs", 1_003),
    "Ancient Catacombs Antechamber Chest 3": VespadianLocationData("Ancient Catacombs", 1_005),

    #Desert Palace Chests:
    "Desert Palace Hall Chest 1": VespadianLocationData("Desert Palace", 1_299),
    "Desert Palace Hall Chest 2": VespadianLocationData("Desert Palace", 1_300),
    "Desert Palace Hall Chest 3": VespadianLocationData("Desert Palace", 1_301),
    "Desert Palace Hall Chest 4": VespadianLocationData("Desert Palace", 1_313),
    "Desert Palace West Wing Chest 1": VespadianLocationData("Desert Palace", 1_302),
    "Desert Palace West Wing Chest 2": VespadianLocationData("Desert Palace", 1_303),
    "Desert Palace Sitting Room Chest": VespadianLocationData("Desert Palace", 1_304),
    "Desert Palace North Chamber Chest 1": VespadianLocationData("Desert Palace", 1_305),
    "Desert Palace North Chamber Chest 2": VespadianLocationData("Desert Palace", 1_306),
    "Desert Palace North Chamber Chest 3": VespadianLocationData("Desert Palace", 1_307),
    "Desert Palace North Chamber Chest 4": VespadianLocationData("Desert Palace", 1_311),
    "Desert Palace South Chamber Chest 1": VespadianLocationData("Desert Palace", 1_308),
    "Desert Palace South Chamber Chest 2": VespadianLocationData("Desert Palace", 1_309),
    "Desert Palace South Chamber Chest 3": VespadianLocationData("Desert Palace", 1_310),
    "Desert Palace South Chamber Chest 4": VespadianLocationData("Desert Palace", 1_312),
    "Desert Palace Audience Chamber Chest": VespadianLocationData("Desert Palace", 1_379), #Blocked by Palace Key

    #Hideaway Chests:
    "Hideaway General Store Chest": VespadianLocationData("Hideaway", 1_340),
    "Hideaway: Victoria's House Chest": VespadianLocationData("Hideaway", 1_389),

    #Secret Underpass Chests:
    "Secret Underpass Atrium Chest 1": VespadianLocationData("Secret Underpass", 1_314),
    "Secret Underpass Atrium Chest 2": VespadianLocationData("Secret Underpass", 1_315),
    "Secret Underpass Atrium Chest 3": VespadianLocationData("Secret Underpass", 1_316),
    "Secret Underpass Atrium Chest 4": VespadianLocationData("Secret Underpass", 1_317),
    "Secret Underpass Atrium Chest 5": VespadianLocationData("Secret Underpass", 1_318),
    "Secret Underpass Atrium Chest 6": VespadianLocationData("Secret Underpass", 1_319),
    "Secret Underpass Atrium Chest 7": VespadianLocationData("Secret Underpass", 1_320),
    "Secret Underpass Corridors Chest 1": VespadianLocationData("Secret Underpass", 1_326),
    "Secret Underpass Corridors Chest 2": VespadianLocationData("Secret Underpass", 1_321),
    "Secret Underpass Corridors Chest 3": VespadianLocationData("Secret Underpass", 1_322),
    "Secret Underpass Corridors Chest 4": VespadianLocationData("Secret Underpass", 1_323),
    "Secret Underpass Corridors Chest 5": VespadianLocationData("Secret Underpass", 1_324),
    "Secret Underpass Tunnel Chest": VespadianLocationData("Secret Underpass", 1_325),
    "Secret Grove Chest": VespadianLocationData("Secret Underpass",1_327),

    #Waterfall Temple Chests:
    "Waterfall Temple East Wing Chest": VespadianLocationData("Waterfall Temple", 1_330),
    "Waterfall Temple East Sanctum Chest": VespadianLocationData("Waterfall Temple", 1_328),
    "Waterfall Temple North Court Chest": VespadianLocationData("Waterfall Temple", 1_331),
    "Waterfall Temple Waterway Chest 1": VespadianLocationData("Waterfall Temple", 1_332),
    "Waterfall Temple Waterway Chest 2": VespadianLocationData("Waterfall Temple", 1_333),
    "Waterfall Temple Waterway Chest 3": VespadianLocationData("Waterfall Temple", 1_334),
    "Waterfall Temple Waterway Chest 4": VespadianLocationData("Waterfall Temple", 1_335),
    "Waterfall Temple Altar Chest": VespadianLocationData("Waterfall Temple", 1_329), #Blocked by Waterfall Key

    #Starcrossed Citadel Chests:
    "Starcrossed Citadel Outer Wall Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_355), #Blocked by Waning Gibbous
    "Starcrossed Citadel Outer Wall Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_356), #Blocked by Waning Gibbous
    "Starcrossed Citadel Outer Wall Chest 3": VespadianLocationData("Starcrossed Citadel 1", 1_357),
    "Starcrossed Citadel Outer Wall Chest 4": VespadianLocationData("Starcrossed Citadel 1", 1_358),
    "Starcrossed Citadel Outer Wall Chest 5": VespadianLocationData("Starcrossed Citadel 1", 1_358),
    "Starcrossed Citadel Outer Wall Chest 6": VespadianLocationData("Starcrossed Citadel 1", 1_360),
    "Starcrossed Citadel Outer Wall Chest 7": VespadianLocationData("Starcrossed Citadel 1", 1_361),
    "Starcrossed Citadel Outer Wall Chest 8": VespadianLocationData("Starcrossed Citadel 1", 1_362),
    "Starcrossed Citadel Outer Wall Chest 9": VespadianLocationData("Starcrossed Citadel 1", 1_336), #Greater Green Dragon Chest
    "Starcrossed Citadel Outer Wall Chest 10": VespadianLocationData("Starcrossed Citadel 3", 1_354), #Blocked by Waning Gibbous + Gold Key (Greater Yellow Dragon)
    "Starcrossed Citadel Stronghold Chest 1": VespadianLocationData("Starcrossed Citadel 1", 1_363),
    "Starcrossed Citadel Stronghold Chest 2": VespadianLocationData("Starcrossed Citadel 1", 1_364),
    "Starcrossed Citadel Stronghold Chest 3": VespadianLocationData("Starcrossed Citadel 1", 1_365),
    "Starcrossed Citadel Chapel Chest 1": VespadianLocationData("Starcrossed Citadel 1", 1_368),
    "Starcrossed Citadel Chapel Chest 2": VespadianLocationData("Starcrossed Citadel 1", 1_369),
    "Starcrossed Citadel Chapel Chest 3": VespadianLocationData("Starcrossed Citadel 1", 1_370),
    "Starcrossed Citadel Chapel Chest 4": VespadianLocationData("Starcrossed Citadel 1", 1_371),
    "Starcrossed Citadel Chapel Chest 5": VespadianLocationData("Starcrossed Citadel 1", 1_372),

    #Starcrossed Citadel 2 Chests (Blocked by Waning Gibbous):
    "Starcrossed Citadel North Chamber Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_337),
    "Starcrossed Citadel North Chamber Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_338),
    "Starcrossed Citadel North Chamber Chest 3": VespadianLocationData("Starcrossed Citadel 2", 1_339),
    "Starcrossed Citadel Labyrinth Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_366),
    "Starcrossed Citadel Labyrinth Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_367),
    "Starcrossed Citadel Garden Chest": VespadianLocationData("Starcrossed Citadel 2", 1_353),
    "Starcrossed Citadel Second Floor Hallway Chest": VespadianLocationData("Starcrossed Citadel 2", 1_373),
    "Starcrossed Citadel Conservatory Chest": VespadianLocationData("Starcrossed Citadel 2", 1_374),
    "Starcrossed Citadel Living Quarters Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_346), #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_341), #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 3": VespadianLocationData("Starcrossed Citadel 2", 1_342), #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 4": VespadianLocationData("Starcrossed Citadel 2", 1_343), #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 5": VespadianLocationData("Starcrossed Citadel 2", 1_344), #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 6": VespadianLocationData("Starcrossed Citadel 2", 1_345), #Greater Purple Dragon Chests
    "Starcrossed Citadel Crypt Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_375),
    "Starcrossed Citadel Crypt Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_376),
    "Starcrossed Citadel Crypt Chest 3": VespadianLocationData("Starcrossed Citadel 2", 1_377),
    "Starcrossed Citadel Crypt Chest 4": VespadianLocationData("Starcrossed Citadel 2", 1_378),
    "Starcrossed Citadel Cavern Chest 1": VespadianLocationData("Starcrossed Citadel 2", 1_347), #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 2": VespadianLocationData("Starcrossed Citadel 2", 1_348), #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 3": VespadianLocationData("Starcrossed Citadel 2", 1_349), #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 4": VespadianLocationData("Starcrossed Citadel 2", 1_350), #Greater Black Dragon Chests

    #Starcrossed Citadel 3 Chests (Blocked by Waning Gibbous + Gold Key)
    "Starcrossed Citadel Chamber of Fire Chest 1": VespadianLocationData("Starcrossed Citadel 3", 1_351), #Greater White Dragon Chest
    "Starcrossed Citadel Chamber of Fire Chest 2": VespadianLocationData("Starcrossed Citadel 3", 1_352), #Greater Red Dragon Chest
    "Defeat Ephemeris": VespadianLocationData("Starcrossed Citadel 3", 3_000),

    #Astrological Observatory Chests:
    "Astrological Observatory Chest 1": VespadianLocationData("Astrological Observatory", 1_383),
    "Astrological Observatory Chest 2": VespadianLocationData("Astrological Observatory", 1_384),
    

}
event_location_table: Dict[str, VespadianLocationData] = {}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}


#Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set()
    location_name_groups[category].add(location)