import pygame as pg
from pygame.locals import *
import random as r
from constants import *


class Cloud(pg.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pg.image.load("images/cloud.png").convert()
        self.surf.set_colorkey([0, 0, 0], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=[
                SCREEN_WIDTH + 20,
                r.randint(0, SCREEN_HEIGHT - 10)
            ])
        self.speed = r.randint(1, 150) / 100

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

