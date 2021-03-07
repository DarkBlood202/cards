import pygame as pg
from pygame.locals import *

class CardSprite(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 56))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x,y))