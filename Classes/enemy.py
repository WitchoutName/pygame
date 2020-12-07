import pygame as pg
from pygame.locals import *
import random as r
from constants import *


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        img = pg.image.load("images/ship2.png").convert()
        self.surf = pg.transform.scale(img, [80,96])
        self.surf.set_colorkey([0,0,0], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=[
                r.randint(0, SCREEN_WIDTH - 10),
                60
            ])

    def update(self):
        self.rect.move_ip(r.randint(-5,5),1)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
