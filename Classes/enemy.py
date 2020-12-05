import pygame as pg
from pygame.locals import *
import random as r
from constants import *


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pg.image.load("images/missile.png").convert()
        self.surf.set_colorkey([255,255,255], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=[
                SCREEN_WIDTH + 20,
                r.randint(0, SCREEN_HEIGHT - 10)
            ])
        self.speed = r.randint(1, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
