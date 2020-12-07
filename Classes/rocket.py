import pygame as pg
from pygame.locals import *
import random as r
from constants import *


class Rocket(pg.sprite.Sprite):
    def __init__(self, dir, speed, center):
        super(Rocket, self).__init__()
        self.surf = img = pg.image.load("images/missile.png").convert()
        self.surf.set_colorkey([255,255,255], RLEACCEL)
        self.speed = speed
        self.dir = dir
        self.rect = self.surf.get_rect(center=center)

    def update(self):
        self.rect.move_ip(0, self.dir * self.speed)
        if self.rect.bottom < 0:
            self.kill()
