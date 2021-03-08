import pygame as pg
from pygame.locals import *

class CardSprite(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((80, 112))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x,y))

        self.is_active = False
        self.offset = [0, 0]


    def on_active(self, x, y):
        if self.rect.collidepoint((x, y)):
            self.is_active = True
        else:
            self.is_active = False

    