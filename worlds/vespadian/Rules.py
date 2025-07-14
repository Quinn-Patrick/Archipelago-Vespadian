from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule

def set_rules(vespadian_world):
    multiworld = vespadian_world.multiworld
    player = vespadian_world.player
    options = vespadian_world.options

    add_rule(vespadian_world.get_location("Menendel Underground Corridors Key Chest"),
        lambda state: (
            state.has("Tunnel Key", player) or (options.require_lockpicking and state.has("Ariadne", player))
        ))

    add_rule(vespadian_world.get_location("Mole Hole Ground Depths Key Chest"),
        lambda state: (
            state.has("Mole Key", player) or (options.require_lockpicking and state.has("Ariadne", player))
        ))
    
    add_rule(vespadian_world.get_location("Island Fortress Towers Chest 4"),
        lambda state: (
            state.has("Fortress Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Gift From Maria"),
        lambda state: (
            state.has("Fortress Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Island Fortress Hallway Silver Key Chest"),
        lambda state: (
            state.has("Silver Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Bottomless Hole Bottom Chest 1"),
        lambda state: (
            state.has("Silver Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Bottomless Hole Bottom Chest 2"),
        lambda state: (
            state.has("Silver Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Bottomless Hole Bottom Chest 3"),
        lambda state: (
            state.has("Silver Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_entrance("Desert Palace"),
        lambda state: (
            state.has("Magic Mirror", player)
        ))
    
    add_rule(vespadian_world.get_location("Desert Palace Audience Chamber Chest"),
        lambda state: (
            state.has("Palace Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Waterfall Temple Altar Chest"),
        lambda state: (
            state.has("Waterfall Key", player) or options.require_lockpicking
        ))
    
    add_rule(vespadian_world.get_location("Astrological Observatory Chest 2"),
        lambda state: (
            state.has("Jupiter Token", player) or options.require_lockpicking
        ))

    add_rule(vespadian_world.get_entrance("First Continent"),
        lambda state: (
            state.has("Ariadne", player)
        ))

    add_rule(vespadian_world.get_entrance("Bottomless Hole"),
        lambda state: (
            state.has("Adventuring License", player)
        ))

    add_rule(vespadian_world.get_entrance("Wide World"),
        lambda state: (
            state.has("Silver Key", player) or options.require_lockpicking
        ))
        
    add_rule(vespadian_world.get_entrance("Waterfall Temple"),
        lambda state: (
            state.has("Nitro Powder", player)
        ))

    add_rule(vespadian_world.get_entrance("Starcrossed Citadel 1"),
        lambda state: (
            state.has("Waxing Crescent", player)
        ))

    add_rule(vespadian_world.get_entrance("Starcrossed Citadel 2"),
        lambda state: (
            state.has("Waning Gibbous", player)
        ))

    add_rule(vespadian_world.get_entrance("Starcrossed Citadel 3"),
        lambda state: (
            state.has("Gold Key", player) or options.require_lockpicking
        ))

    add_rule(vespadian_world.get_entrance("Astrological Observatory"),
        lambda state: (
            state.has("Mercury Token", player) and
            state.has("Venus Token", player) and
            state.has("Mars Token", player) and
            state.has("Saturn Token", player)
        ))

    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)