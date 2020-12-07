import pygame as pg
from pygame.locals import *
from Classes.sound_manager import *
from Classes.group_manager import *
from Classes.rocket import Rocket
from constants import *

sounds = Sounds()
groups = Groups()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        img = pg.image.load("images/ship1.png").convert()
        self.surf = pg.transform.scale(img, [80,120])
        self.surf.set_colorkey([0,0,0])
        self.rect = self.surf.get_rect(center=[SCREEN_WIDTH/2, SCREEN_HEIGHT - 50])
        self.time_to_shoot = 25
        self.time_now = 0
        self.score = 0

    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.move_ip(-7, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(7, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if self.time_now != self.time_to_shoot:
            self.time_now += 1
        else:
            groups[Group.ROCKETS].add(Rocket(-1, 5, [self.rect.center[0], SCREEN_HEIGHT - 150]))
            self.time_now = 0