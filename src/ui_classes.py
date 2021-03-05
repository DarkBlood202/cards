import pygame as pg
from pygame.locals import *

from ui_functions import draw_text_centered

class Button():
    def __init__(self, x, y, width, height, color_primary, color_hover, text="", border_radius=10):
        self.rect = pg.Rect(x, y, width, height)
        self.color_primary = color_primary
        self.color_hover = color_hover
        self.color = self.color_primary
        self.text = text
        self.border_radius = border_radius
        self.is_active = False

    def on_active(self, x, y):
        if self.rect.collidepoint((x, y)):
            self.color = self.color_hover
            self.is_active = True
        else:
            self.color = self.color_primary
            self.is_active = False

    def draw(self, surface, font=None, color=None):
        pg.draw.rect(surface, self.color, self.rect, border_radius=self.border_radius)
        draw_text_centered(self.text, font, color, surface, self.rect.centerx, self.rect.centery)

class MenuButton():
    pass