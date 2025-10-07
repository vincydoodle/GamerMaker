# Description

GamerMaker is simple library that helps make games using [Pygame](https://www.pygame.org/). You can use it for your own games, or just look at the code. It is meant to be a library to simplify the job of using pygame, especially for learning. If you find any problems, report them [here](https://github.com/vincydoodle/GamerMaker/issues)

### How to install
Simply run the following command:
```commandline
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ gamermaker
```

### Links
[Github](https://github.com/vincydoodle/GamerMaker)

[PyPI Test](https://test.pypi.org/project/gamermaker/)

# How to use
### Making a Window

In order to make a game in Pygame, you would probably have a setup like this:

```python
import pygame.display

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Window")
pygame.display.set_icon(pygame.image.load("PATH/TO/ICON.png"))

running = True
while running:
    # Gameloop
```

However, in GamerMaker it compacts it for you:
```python
import gamermaker

def update():
    # Update Code

def draw():
    # Draw Code

gamermaker.create((800, 600), "Game Window", gamermaker.image.load("PATH/TO/ICON.png"), on_update = update, on_draw = draw)
```

### Keybinds
In Pygame, if you want to add a keybind you add it directly to the gameloop. In GamerMaker however, the gameloop is done internally. To add a keybind you can:
1. Add your own code to your update function: 
```python
def update():
    for event in gamermaker.event.get():
        if event.type == gamermaker.KEYDOWN:
            if event.key == gamermaker.K_SPACE:
                print("Space Was Pressed")
```

2. Use GamerMaker's built in function:
```python
gamermaker.add_keybinding(gamermaker.K_SPACE, lambda: print("Space Was Pressed"))

# You can also remove them
gamermaker.remove_keybinding(gamermaker.K_SPACE)
```

### Window Handling

In GamerMaker, there are various window handling functions:
```python
gamermaker.reopen_window() # Closes and then reopens the window

gamermaker.close_window() # Closes the window

gamermaker.edit_window_name("Hello, World") # Changes the current window title to the given one

gamermaker.edit_window_icon(gamermaker.image.load("PATH/TO/NEW/ICON.png")) # Changes the current window icon to the given one
```

### Window Dataclasses

GamerMaker uses dataclasses to store information about windows. It looks like this:
```python
@dataclass
class WindowConfig:
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
```
In GamerMaker, there is a function for getting and manually changing the dataclass:
```python
Dataclass = gamermaker.get_current_config() # Gets the dataclass of the current window

Dataclass.size = (900, 700) # Example of editing the config
gamermaker.close_window() # Closes the current window
gamermaker.create_from_config(Dataclass) # Opens the modified window
```