import pygame as pg
from pygame.locals import *

pg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

runnig = True
while runnig:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runnig = False

        elif event.type == QUIT:
            runnig = False


    screen.fill([255,255,255])
    surf = pg.Surface([50,50])
    surf.fill([0,0,0])
    rect = surf.get_rect()
    screen.blit(surf, [(SCREEN_WIDTH-surf.get_width())/2, (SCREEN_HEIGHT-surf.get_height())/2])
    pg.display.flip()

pg.quit()
