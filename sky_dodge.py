import pygame as pg
from pygame.locals import *
import random as r

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.image.load("images/jet.png").convert()
        self.surf.set_colorkey([255,255,255], RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
            sounds["move_up"].play()
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            sounds["move_down"].play()
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



pg.init()
clock = pg.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
player = Player()
groups = {}
groups["enemies"] = pg.sprite.Group()
groups["clouds"] = pg.sprite.Group()
groups["all"] = pg.sprite.Group()
groups["all"].add(player)
events = {}
events["ADDENEMY"] = pg.USEREVENT + 1
pg.time.set_timer(events["ADDENEMY"], 150)
events["ADDCLOUD"] = pg.USEREVENT + 1
pg.time.set_timer(events["ADDCLOUD"], 1000)
pg.mixer.music.load("sound/Sky_dodge_theme.ogg")
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(loops=-1)
sounds = {}
sounds["move_up"] = pg.mixer.Sound("sound/Jet_up.ogg")
sounds["move_down"] = pg.mixer.Sound("sound/Jet_down.ogg")
sounds["collision"] = pg.mixer.Sound("sound/Boom.ogg")

for sound in sounds:
    sounds[sound].set_volume(0.1)


runnig = True
while runnig:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                runnig = False

        elif event.type == QUIT:
            runnig = False

        elif event.type == events["ADDENEMY"]:
            groups["enemies"].add(Enemy())

        elif event.type == events["ADDCLOUD"]:
            groups["clouds"].add(Cloud())

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    groups["enemies"].update()
    groups["clouds"].update()

    screen.fill([135, 206, 250])

    for group in groups:
        for entity in groups[group]:
            screen.blit(entity.surf, entity.rect)

    screen.blit(player.surf, player.rect)
    if pg.sprite.spritecollideany(player, groups["enemies"]):
        player.kill()
        sounds["move_up"].stop()
        sounds["move_down"].stop()
        sounds["collision"].play()
        pg.time.delay(500)
        runnig = False

    pg.display.flip()
    clock.tick(120)

pg.mixer.music.stop()
pg.mixer.quit()
pg.quit()
