import pygame as pg
from pygame.locals import *
from Classes.sound_manager import *
from constants import *
sounds = Sounds()


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.image.load("images/jet.png").convert()
        self.surf.set_colorkey([255,255,255], RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
            sounds[Sound.MOVE_UP].play()
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            sounds[Sound.MOVE_DOWN].play()
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
