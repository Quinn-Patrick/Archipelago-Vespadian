from BaseClasses import Location

from typing import Dict, NamedTuple, Optional, Set
import typing

class VespadianLocation(Location):
    game: str = "Vespadian"

locationTable: dict = {
    #Menendel Underground Chests:
    "Menendel Underground Corridors Chest 1": 1_220,
    "Menendel Underground Corridors Chest 2": 1_221,
    "Menendel Underground Corridors Chest 3": 1_222,
    "Menendel Underground Corridors Chest 4": 1_223,
    "Menendel Underground Corridors Key Chest": 1_224, ##Blocked by tunnel key
    "Menendel Underground East Tunnel Chest 1": 1_225,
    "Menendel Underground East Tunnel Chest 2": 1_226,
    "Menendel Underground East Tunnel Chest 3": 1_227,
    "Menendel Underground East Tunnel Chest 4": 1_228,
    "Menendel Underground West Tunnel Chest 1": 1_229,
    "Menendel Underground West Tunnel Chest 2": 1_230,
    "Menendel Underground Vault Chest 1": 1_231,
    "Menendel Underground Vault Chest 2": 1_232,
    "Menendel Underground Vault Chest 3": 1_233,
    "Menendel Underground Vault Chest 4": 1_234,

    #Moonlit Shrine Chests:
    "Moonlit Shrine Antechamber Chest 1": 1_235,
    "Moonlit Shrine Antechamber Chest 2": 1_236,
    "Moonlit Shrine Antechamber Chest 3": 1_237,
    "Moonlit Shrine Antechamber Chest 4": 1_238,
    "Moonlit Shrine Antechamber Chest 5": 1_239,
    "Moonlit Shrine Antechamber Chest 6": 1_240,
    "Moonlit Shrine Antechamber Chest 7": 1_241,
    "Moonlit Shrine Antechamber Chest 8": 1_242,
    "Moonlit Shrine Antechamber Chest 9": 1_243,
    "Moonlit Shrine Antechamber Chest 10": 1_244,
    "Moonlit Shrine Mount Chest 1": 1_245,
    "Moonlit Shrine Mount Chest 2": 1_246,
    "Moonlit Shrine Mount Chest 3": 1_247,
    "Moonlit Shrine Mount Chest 4": 1_248,
    "Moonlit Shrine Mount Chest 5": 1_249,
    "Moonlit Shrine Mount Chest 6": 1_250,

    #Mole Hole Chests:
    "Mole Hole Ground Level Chest 1": 1_251,
    "Mole Hole Ground Level Chest 2": 1_252,
    "Mole Hole Ground Level Chest 3": 1_253,
    "Mole Hole Ground Level Chest 4": 1_254,
    "Mole Hole Ground Level Chest 5": 1_255,
    "Mole Hole Ground Depths Key Chest": 1_256, #Blocked by Mole Key
    "Mole Hole Ground Depths Chest 1": 1_257,
    "Rescue Ariadne": 2_442,

    #Hearthaven Chests:
    "Hearthaven South Chest": 1_215,
    "Hearthaven North Chest 1": 1_045,
    "Hearthaven North Chest 2": 1_046,
    "Hearthaven Crafting Shop Chest": 1_289,
    "Hearthaven Library Chest": 1_044,
    "Gift From Maria": 1_382,

    #Island Fortress Chests:
    "Island Fortress Keep Chest 1": 1_260,
    "Island Fortress Keep Chest 2": 1_261,
    "Island Fortress Keep Chest 3": 1_262,
    "Island Fortress Keep Chest 4": 1_263,
    "Island Fortress Keep Chest 5": 1_264,
    "Island Fortress Keep Chest 6": 1_265,
    "Island Fortress Keep Chest 7": 1_266,
    "Island Fortress Keep Chest 8": 1_267,
    "Island Fortress Keep Chest 9": 1_268,
    "Island Fortress Keep Chest 10": 1_269,
    "Island Fortress Keep Chest 11": 1_270,
    "Island Fortress Keep Chest 12": 1_271,
    "Island Fortress Keep Chest 13": 1_272,
    "Island Fortress Keep Chest 14": 1_273,
    "Island Fortress Keep Chest 15": 1_274,
    "Island Fortress Keep Chest 16": 1_281,
    "Island Fortress Basement Chest 1": 1_275,
    "Island Fortress Basement Chest 2": 1_276,
    "Island Fortress Basement Chest 3": 1_277,
    "Island Fortress Hallway Silver Key Chest": 1_385, #Blocked by Silver Key
    "Island Fortress Towers Chest 1": 1_278,
    "Island Fortress Towers Chest 2": 1_279,
    "Island Fortress Towers Chest 3": 1_259,
    "Island Fortress Towers Chest 4": 1_280, #Blocked by Fortress Key

    #Farsight Chests:
    "Farsight Inn Chest 1": 1_380,
    "Farsight Inn Chest 2": 1_381,

    #Bottomless Hole Chests:
    "Bottomless Hole B1 Chest": 1_144,
    "Bottomless Hole B3 Chest 1": 1_145,
    "Bottomless Hole B3 Chest 2": 1_146,
    "Bottomless Hole B3 Chest 3": 1_147,
    "Bottomless Hole B3 Chest 4": 1_148,
    "Bottomless Hole B3 Chest 5": 1_149,
    "Bottomless Hole B3 Chest 6": 1_150,
    "Bottomless Hole B4 Chest 1": 1_151,
    "Bottomless Hole B4 Chest 2": 1_152,
    "Bottomless Hole B4 Chest 3": 1_153,
    "Bottomless Hole B4 Chest 4": 1_154,
    "Bottomless Hole B4 Chest 5": 1_155,
    "Bottomless Hole B4 Chest 6": 1_156,
    "Bottomless Hole B4 Chest 7": 1_157,
    "Bottomless Hole B5 Chest 1": 1_143,
    "Bottomless Hole B5 Chest 2": 1_158,
    "Bottomless Hole B5 Chest 3": 1_159,
    "Bottomless Hole B5 Chest 4": 1_160,
    "Bottomless Hole B5 Chest 5": 1_161,

    #The Great Between Chests:
    "The Great Between: Web of Worlds Chest 1": 1_285,
    "The Great Between: Web of Worlds Chest 2": 1_286,
    "The Great Between: Web of Worlds Chest 3": 1_287,
    "The Great Between: Web of Worlds Chest 4": 1_288,
    "The Great Between: Isles of Thought Chest 1": 1_282,
    "The Great Between: Isles of Thought Chest 2": 1_283,
    "The Great Between: Isles of Thought Chest 3": 1_284,

    #Arva Mandia Chests:
    "Arva Mandia General Store Chest": 1_290,

    #Ancient Catacombs Chests:
    "Ancient Catacombs East Tunnel Chest 1": 1_006,
    "Ancient Catacombs East Tunnel Chest 2": 1_291,
    "Ancient Catacombs Cistern Chest 1": 1_012,
    "Ancient Catacombs Cistern Chest 2": 1_016,
    "Ancient Catacombs Cistern Chest 3": 1_014,
    "Ancient Catacombs Cistern Chest 4": 1_015,
    "Ancient Catacombs Cistern Chest 5": 1_013,
    "Ancient Catacombs Cistern Chest 6": 1_011,
    "Ancient Catacombs Cistern Chest 7": 1_010,
    "Ancient Catacombs Cistern Chest 8": 1_007,
    "Ancient Catacombs Cistern Chest 9": 1_009,
    "Ancient Catacombs Cistern Chest 10": 1_008,
    "Ancient Catacombs North Tunnel Chest 1": 1_017,
    "Ancient Catacombs North Tunnel Chest 2": 1_018,
    "Ancient Catacombs North Tunnel Chest 3": 1_019,
    "Ancient Catacombs North Tunnel Chest 4": 1_020,
    "Ancient Catacombs Artery Chest 1": 1_292,
    "Ancient Catacombs Artery Chest 2": 1_293,
    "Ancient Catacombs Artery Chest 3": 1_294,
    "Ancient Catacombs Artery Chest 4": 1_295,
    "Ancient Catacombs Artery Chest 5": 1_296,
    "Ancient Catacombs Artery Chest 6": 1_297,
    "Ancient Catacombs Artery Chest 7": 1_298,
    "Ancient Catacombs Treasury Chest": 1_390,
    "Ancient Catacombs Antechamber Chest 1": 1_002,
    "Ancient Catacombs Antechamber Chest 2": 1_003,
    "Ancient Catacombs Antechamber Chest 3": 1_005,

    #Desert Palace Chests:
    "Desert Palace Hall Chest 1": 1_299,
    "Desert Palace Hall Chest 2": 1_300,
    "Desert Palace Hall Chest 3": 1_301,
    "Desert Palace Hall Chest 4": 1_313,
    "Desert Palace West Wing Chest 1": 1_302,
    "Desert Palace West Wing Chest 2": 1_303,
    "Desert Palace Sitting Room Chest": 1_304,
    "Desert Palace North Chamber Chest 1": 1_305,
    "Desert Palace North Chamber Chest 2": 1_306,
    "Desert Palace North Chamber Chest 3": 1_307,
    "Desert Palace North Chamber Chest 4": 1_311,
    "Desert Palace South Chamber Chest 1": 1_308,
    "Desert Palace South Chamber Chest 2": 1_309,
    "Desert Palace South Chamber Chest 3": 1_310,
    "Desert Palace South Chamber Chest 4": 1_312,
    "Desert Palace Audience Chamber Chest": 1_379, #Blocked by Palace Key

    #Hideaway Chests:
    "Hideaway General Store Chest": 1_340,
    "Hideaway: Victoria's House Chest": 1_389,

    #Secret Underpass Chests:
    "Secret Underpass Atrium Chest 1": 1_314,
    "Secret Underpass Atrium Chest 2": 1_315,
    "Secret Underpass Atrium Chest 3": 1_316,
    "Secret Underpass Atrium Chest 4": 1_317,
    "Secret Underpass Atrium Chest 5": 1_318,
    "Secret Underpass Atrium Chest 6": 1_319,
    "Secret Underpass Atrium Chest 7": 1_320,
    "Secret Underpass Corridors Chest 1": 1_326,
    "Secret Underpass Corridors Chest 2": 1_321,
    "Secret Underpass Corridors Chest 3": 1_322,
    "Secret Underpass Corridors Chest 4": 1_323,
    "Secret Underpass Corridors Chest 5": 1_324,
    "Secret Underpass Tunnel Chest": 1_325,
    "Secret Grove Chest": 1_327,

    #Waterfall Temple Chests:
    "Waterfall Temple East Wing Chest": 1_330,
    "Waterfall Temple East Sanctum Chest": 1_328,
    "Waterfall Temple North Court Chest": 1_331,
    "Waterfall Temple Waterway Chest 1": 1_332,
    "Waterfall Temple Waterway Chest 2": 1_333,
    "Waterfall Temple Waterway Chest 3": 1_334,
    "Waterfall Temple Waterway Chest 4": 1_335,
    "Waterfall Temple Altar Chest": 1_329, #Blocked by Waterfall Key

    #Starcrossed Citadel Chests:
    "Starcrossed Citadel Outer Wall Chest 1": 1_355, #Blocked by Waning Gibbous
    "Starcrossed Citadel Outer Wall Chest 2": 1_356, #Blocked by Waning Gibbous
    "Starcrossed Citadel Outer Wall Chest 3": 1_357,
    "Starcrossed Citadel Outer Wall Chest 4": 1_358,
    "Starcrossed Citadel Outer Wall Chest 5": 1_358,
    "Starcrossed Citadel Outer Wall Chest 6": 1_360,
    "Starcrossed Citadel Outer Wall Chest 7": 1_361,
    "Starcrossed Citadel Outer Wall Chest 8": 1_362,
    "Starcrossed Citadel Outer Wall Chest 9": 1_336, #Greater Green Dragon Chest
    "Starcrossed Citadel Outer Wall Chest 10": 1_354, #Blocked by Waning Gibbous + Gold Key (Greater Yellow Dragon)
    "Starcrossed Citadel Stronghold Chest 1": 1_363,
    "Starcrossed Citadel Stronghold Chest 2": 1_364,
    "Starcrossed Citadel Stronghold Chest 3": 1_365,
    "Starcrossed Citadel Chapel Chest 1": 1_368,
    "Starcrossed Citadel Chapel Chest 1": 1_369,
    "Starcrossed Citadel Chapel Chest 1": 1_370,
    "Starcrossed Citadel Chapel Chest 1": 1_371,
    "Starcrossed Citadel Chapel Chest 1": 1_372,

    #Starcrossed Citadel 2 Chests (Blocked by Waning Gibbous):
    "Starcrossed Citadel North Chamber Chest 1": 1_337,
    "Starcrossed Citadel North Chamber Chest 2": 1_338,
    "Starcrossed Citadel North Chamber Chest 3": 1_339,
    "Starcrossed Citadel Labyrinth Chest 1": 1_366,
    "Starcrossed Citadel Labyrinth Chest 2": 1_367,
    "Starcrossed Citadel Garden Chest": 1_353,
    "Starcrossed Citadel Second Floor Hallway Chest": 1_373,
    "Starcrossed Citadel Conservatory Chest": 1_374,
    "Starcrossed Citadel Living Quarters Chest 1": 1_346, #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 2": 1_341, #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 3": 1_342, #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 4": 1_343, #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 5": 1_344, #Greater Purple Dragon Chests
    "Starcrossed Citadel Living Quarters Chest 6": 1_345, #Greater Purple Dragon Chests
    "Starcrossed Citadel Crypt Chest 1": 1_375,
    "Starcrossed Citadel Crypt Chest 2": 1_376,
    "Starcrossed Citadel Crypt Chest 3": 1_377,
    "Starcrossed Citadel Crypt Chest 4": 1_378,
    "Starcrossed Citadel Cavern Chest 1": 1_347, #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 2": 1_348, #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 3": 1_349, #Greater Black Dragon Chests
    "Starcrossed Citadel Cavern Chest 4": 1_350, #Greater Black Dragon Chests

    #Starcrossed Citadel 3 Chests (Blocked by Waning Gibbous + Gold Key)
    "Starcrossed Citadel Chamber of Fire Chest 1": 1_351, #Greater White Dragon Chest
    "Starcrossed Citadel Chamber of Fire Chest 2": 1_352, #Greater Red Dragon Chest

}