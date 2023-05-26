import pygame, os
from ctypes import *

# import win32api
# pip install pywin32
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (50, 50, 50)
BLUE_LIGHT = (102, 102, 255)
LIGHT_GREY = (192, 192, 192)

TIMER = 60

COUNTER = 0

# device = win32api.EnumDisplayDevices()
# settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
# FPS = getattr(settings, 'DisplayFrequency')
FPS = 60

WIDTH = 1600
HEIGHT = 900

FONT_SIZE = int((WIDTH + HEIGHT) / 75)

font_main = pygame.font.Font(os.path.join("fonts", 'ofont.ru_Borsok.ttf'), FONT_SIZE)
font_for_game = pygame.font.Font(os.path.join("fonts", 'arial_bolditalicmt.ttf'), FONT_SIZE)
icons_font = pygame.font.Font(os.path.join("fonts", 'Aristotelica-Icons-ExtraLight-trial.ttf'),
                              int((HEIGHT + WIDTH) / 20))

ZV_ICONS = pygame.font.Font(os.path.join("fonts", 'icomoon.ttf'), 60)
