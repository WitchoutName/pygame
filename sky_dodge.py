import pygame as pg
from pygame.locals import *
from Classes.sound_manager import *
from Classes.group_manager import *
from Classes.event_manager import *
from Classes.player import Player
from Classes.enemy import Enemy
from Classes.cloud import Cloud
from constants import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
player = Player()

groups = Groups()
for group in Group:
    groups[group] = pg.sprite.Group()
groups[Group.DEFAULT].add(player)

events = Events()
events[Event.ADDENEMY] = pg.USEREVENT + 1
pg.time.set_timer(events[Event.ADDENEMY], 200)
events[Event.ADDCLOUD] = pg.USEREVENT + 2
pg.time.set_timer(events[Event.ADDCLOUD], 1000)

pg.mixer.music.load("sound/Sky_dodge_theme.ogg")
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(loops=-1)

sounds = Sounds()
sound_paths = ["sound/Jet_up.ogg", "sound/Jet_down.ogg", "sound/Boom.ogg"]
for x, sound in enumerate(Sound):
    sounds[sound] = pg.mixer.Sound(sound_paths[x])

for sound in sounds:
    sound.set_volume(0.1)


running = True
while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == events[Event.ADDENEMY]:
            Groups()[Group.ENEMIES].add(Enemy())

        elif event.type == events[Event.ADDCLOUD]:
            Groups()[Group.CLOUDS].add(Cloud())

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    Groups()[Group.ENEMIES].update()
    Groups()[Group.CLOUDS].update()

    screen.fill([135, 206, 250])

    for group in groups:
        for entity in group:
            screen.blit(entity.surf, entity.rect)

    screen.blit(player.surf, player.rect)
    if pg.sprite.spritecollideany(player, groups[Group.ENEMIES]):
        player.kill()
        sounds[Sound.MOVE_UP].stop()
        sounds[Sound.MOVE_DOWN].stop()
        sounds[Sound.COLLISION].play()
        pg.time.delay(500)
        running = False

    pg.display.flip()
    clock.tick(120)

pg.mixer.music.stop()
pg.mixer.quit()
pg.quit()
