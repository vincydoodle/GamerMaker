from src.gamermaker.keys import *
from dataclasses import dataclass
import pygame
from typing import Callable, Tuple

# Making Variables
screen = None
keybinds = {}
running = False
pygame.mixer.init()
pygame.init()

@dataclass
class TempConfig:
    size: Tuple[float, float]
    name: str = "Game Window"
    icon: pygame.Surface = None
    depth: int = 0
    display: int = 0
    vsync: int = 0
    fullscreen: bool = False
    resizable: bool = False
    double_buffer: bool = False
    hwsurface: bool = False
    opengl: bool = False
    noframe: bool = False
    on_update: Callable = None
    on_draw: Callable = None
    fps: int = 60

# Gameloop Function

def _gameloop(on_update: Callable, on_draw: Callable, fps: int):
    global running
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Runs keybinds from the add_keybinding() function
            elif event.type == pygame.KEYDOWN and event.key in keybinds:
                keybinds[event.key]()

        # User-provided update logic
        if on_update:
            on_update()

        # Drawing logic
        if on_draw:
            on_draw(screen)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


# Creates the Game
def create(size: tuple[float, float], name: str = "Game Window", icon: pygame.Surface = None, on_update: callable = None,
           on_draw: callable = None, depth: int = 0, display: int = 0, vsync: int = 0,
           fullscreen: bool = False, resizable: bool = False, double_buffer: bool = False,
           hwsurface: bool = False, opengl: bool = False, noframe: bool = False, *, fps=60, **kwargs):

    # Initializations
    global screen
    global running
    global keybinds
    pygame.init()

    # Set Flags
    flags = 0
    if fullscreen:
        flags |= pygame.FULLSCREEN
    if resizable:
        flags |= pygame.RESIZABLE
    if double_buffer:
        flags |= pygame.DOUBLEBUF
    if hwsurface:
        flags |= pygame.HWSURFACE
    if opengl:
        flags |= pygame.OPENGL
    if noframe:
        flags |= pygame.NOFRAME

    # Make the window
    screen = pygame.display.set_mode(size=size, flags=flags, depth=depth, display=display, vsync=vsync)
    pygame.display.set_caption(name)
    if icon is not None:
        pygame.display.set_icon(icon)

    # Save the config
    TempConfig.size = size
    TempConfig.name = name
    TempConfig.icon = icon
    TempConfig.depth = depth
    TempConfig.display = display
    TempConfig.vsync = vsync
    TempConfig.fullscreen = fullscreen
    TempConfig.resizable = resizable
    TempConfig.double_buffer = double_buffer
    TempConfig.hwsurface = hwsurface
    TempConfig.opengl = opengl
    TempConfig.noframe = noframe
    TempConfig.on_update = on_update
    TempConfig.on_draw = on_draw
    TempConfig.fps = fps

    # Run the Gameloop
    _gameloop(on_update, on_draw, fps)

# Closes then reopens the window
def reopen_window():
    global running
    global keybinds
    global screen
    pygame.quit()
    pygame.init()

    if screen is None:
        import colorama
        print(f"{colorama.Fore.RED}The window has not been made!")
        exit(1)
    else:

        # Get Config
        size = TempConfig.size
        name = TempConfig.name
        icon = TempConfig.icon
        depth = TempConfig.depth
        display = TempConfig.display
        vsync = TempConfig.vsync
        fullscreen = TempConfig.fullscreen
        resizable = TempConfig.resizable
        double_buffer = TempConfig.double_buffer
        hwsurface = TempConfig.hwsurface
        opengl = TempConfig.opengl
        noframe = TempConfig.noframe
        on_update = TempConfig.on_update
        on_draw = TempConfig.on_draw
        fps = TempConfig.fps

        # Set Flags
        flags = 0
        if fullscreen:
            flags |= pygame.FULLSCREEN
        if resizable:
            flags |= pygame.RESIZABLE
        if double_buffer:
            flags |= pygame.DOUBLEBUF
        if hwsurface:
            flags |= pygame.HWSURFACE
        if opengl:
            flags |= pygame.OPENGL
        if noframe:
            flags |= pygame.NOFRAME

        # Make the window
        screen = pygame.display.set_mode(size=size, flags=flags, depth=depth, display=display, vsync=vsync)
        pygame.display.set_caption(name)
        if icon is not None:
            pygame.display.set_icon(icon)

        # Run the gameloop
        _gameloop(on_update, on_draw, fps)

# Returns the dataclass of the current window
def get_current_config():
    global screen
    if screen is None:
        import colorama
        print(f"{colorama.Fore.RED}The window has not been made!")
        exit(1)
    else:
        return TempConfig

# Makes a window from a provided dataclass
def create_from_config(dataclass):
    global running, keybinds, screen

    # Extract values from the config dataclass
    size = dataclass.size
    name = dataclass.name
    icon = dataclass.icon
    depth = dataclass.depth
    display = dataclass.display
    vsync = dataclass.vsync
    fullscreen = dataclass.fullscreen
    resizable = dataclass.resizable
    double_buffer = dataclass.double_buffer
    hwsurface = dataclass.hwsurface
    opengl = dataclass.opengl
    noframe = dataclass.noframe
    on_update = dataclass.on_update
    on_draw = dataclass.on_draw
    fps = dataclass.fps

    # Initialize Pygame
    pygame.init()

    # Set Flags
    flags = 0
    if fullscreen: flags |= pygame.FULLSCREEN
    if resizable: flags |= pygame.RESIZABLE
    if double_buffer: flags |= pygame.DOUBLEBUF
    if hwsurface: flags |= pygame.HWSURFACE
    if opengl: flags |= pygame.OPENGL
    if noframe: flags |= pygame.NOFRAME

    # Make the window
    screen = pygame.display.set_mode(size=size, flags=flags, depth=depth, display=display, vsync=vsync)
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)

    # Save back to config
    dataclass.size = size
    dataclass.name = name
    dataclass.icon = icon
    dataclass.depth = depth
    dataclass.display = display
    dataclass.vsync = vsync
    dataclass.fullscreen = fullscreen
    dataclass.resizable = resizable
    dataclass.double_buffer = double_buffer
    dataclass.hwsurface = hwsurface
    dataclass.opengl = opengl
    dataclass.noframe = noframe
    dataclass.on_update = on_update
    dataclass.on_draw = on_draw
    dataclass.fps = fps

    # Run the gameloop
    _gameloop(on_update, on_draw, fps)

# Edits the current window's title
def change_name(name: str):
    pygame.display.set_caption(name)
    TempConfig.name = name

# Edits the current window's icon
def change_icon(icon: pygame.Surface):
    pygame.display.set_icon(icon)
    TempConfig.icon = icon

# Closes the current window so that a new one can be made
def end():
    global running
    running = False
    pygame.quit()