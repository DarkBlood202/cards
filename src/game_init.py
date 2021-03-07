import pygame as pg
import sys

from pygame.locals import *

from settings import *
from classes import *
from sprites import *
from functions import EXIT_GAME
from ui_classes import *
from ui_functions import *
from constants import *

pg.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

clock = pg.time.Clock()

font = pg.font.SysFont(None, 20)

def main_menu():
    btn_1 = Button(50, 100, 100, 50, Palette.IMP_RED.value, Palette.CINNABAR.value, text="Start")
    btn_2 = Button(50, 170, 100, 30, Palette.CEL_BLUE.value, Palette.G_B_CRAYOLA.value, text="Rules")
    btn_3 = Button(50, 220, 100, 30, Palette.CEL_BLUE.value, Palette.G_B_CRAYOLA.value, text="Options")
    btn_4 = Button(50, 270, 100, 30, Palette.CEL_BLUE.value, Palette.G_B_CRAYOLA.value, text="Exit")

    # Initializes click state variable for buttons
    click = False

    while True:
        mx, my = pg.mouse.get_pos()
        
        screen.fill((0,0,0))
        draw_text("Main Menu", font, (255, 255, 255), screen, 16, 16)

        btn_1.on_active(mx, my)
        btn_2.on_active(mx, my)
        btn_3.on_active(mx, my)
        btn_4.on_active(mx, my)

        if click:
            if btn_1.is_active:
                game()
            elif btn_2.is_active:
                rules()
            elif btn_3.is_active:
                options()
            elif btn_4.is_active:
                EXIT_GAME()

        btn_1.draw(screen, font, Palette.GHOST_WHITE.value)
        btn_2.draw(screen, font, Palette.GHOST_WHITE.value)
        btn_3.draw(screen, font, Palette.GHOST_WHITE.value)
        btn_4.draw(screen, font, Palette.GHOST_WHITE.value)

        # Restarts clicked state next frame unless you click again
        click = False

        for event in pg.event.get():
            if event.type == QUIT:
                EXIT_GAME()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    EXIT_GAME()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        clock.tick(FPS)

def game():
    running = True
    click = False

    myCards = pg.sprite.Group()

    while running:
        mx, my = pg.mouse.get_pos()

        screen.fill((0,0,0))
        draw_text("Game", font, (255, 255, 255), screen, 16, 16)

        if click:
            CardSprite(mx, my).add(myCards)

        # drawing
        myCards.draw(screen)

        click = False
        
        for event in pg.event.get():
            if event.type == QUIT:
                EXIT_GAME()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myCards.empty()
                    running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
        clock.tick(FPS)

def rules():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text("Ruleset & How to play", font, (255, 255, 255), screen, 16, 16)

        for event in pg.event.get():
            if event.type == QUIT:
                EXIT_GAME()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        clock.tick(FPS)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text("Options", font, (255, 255, 255), screen, 16, 16)        

        for event in pg.event.get():
            if event.type == QUIT:
                EXIT_GAME()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        clock.tick(FPS)

main_menu()