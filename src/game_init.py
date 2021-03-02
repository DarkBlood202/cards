import pygame as pg
import sys

from pygame.locals import *

from settings import *
from classes import *
from ui_functions import *
from constants import *

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

clock = pg.time.Clock()

font = pg.font.SysFont(None, 20)

click = False

def main_menu():
    while True:
        mx, my = pg.mouse.get_pos()
        
        screen.fill((0,0,0))
        draw_text("Main Menu", font, (255, 255, 255), screen, 20, 20)

        button_1 = pg.Rect(50, 100, 200, 50)
        button_2 = pg.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()

        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pg.draw.rect(screen, Palette.IMP_RED.value, button_1, border_radius=10)
        pg.draw.rect(screen, Palette.IMP_RED.value, button_2, border_radius=10)

        click = False

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        clock.tick(FPS)

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text("Game", font, (255, 255, 255), screen, 20, 20)        

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        clock.tick(FPS)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text("Options", font, (255, 255, 255), screen, 20, 20)        

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()