from src.gamermaker import *
from pygame import *
from pygame import quit as quit_pygame

def quit(code: int = 0):
    quit_pygame()
    exit(code)