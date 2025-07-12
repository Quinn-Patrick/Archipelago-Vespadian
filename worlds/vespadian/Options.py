from dataclasses import dataclass
from Options import NamedRange, Choice, Range, Toggle, DefaultOnToggle, PerGameCommonOptions, StartInventoryPool, OptionGroup

class RequireLockpicking(Toggle):
    """
    Toggle whether logic can require a lock to be picked by a thief.
    With this option, all accessible locked doors enter logic upon
    rescuing Ariadne and gaining access to the Adventurer's Guild.
    """
    display_name = "Require Lockpicking"

@dataclass
class VespadianOptions(PerGameCommonOptions):
    require_lockpicking: RequireLockpicking