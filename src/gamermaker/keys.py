from src.gamermaker.game import *
from pygame.key import *
from pygame.constants import *

# Adds Keybinds
def add_keybinding(key: int, action: callable):
    """
    Adds or updates a keybinding.

    Args:
        key: The Pygame key constant, like pygame.K_SPACE.
        action: The function to be called when the key is pressed.
    """
    keybinds[key] = action

# Removes Keybinds
def remove_keybinding(key: int):
    del keybinds[key]