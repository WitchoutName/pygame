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
pg.font.init()
font = pg.font.SysFont('Comic Sans MS', 60)
clock = pg.time.Clock()
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
player = Player()
bg = pg.image.load("images/nebula.jpg").convert()

groups = Groups()
for group in Group:
    groups[group] = pg.sprite.Group()
groups[Group.DEFAULT].add(player)

events = Events()
events[Event.ADDENEMY] = pg.USEREVENT + 1
pg.time.set_timer(events[Event.ADDENEMY], 500)
events[Event.ADDCLOUD] = pg.USEREVENT + 2
#pg.time.set_timer(events[Event.ADDCLOUD], 1000)

pg.mixer.music.load("sound/Sky_dodge_theme.ogg")
pg.mixer.music.set_volume(0.01)
pg.mixer.music.play(loops=-1)

sounds = Sounds()
sound_paths = ["sound/Jet_up.ogg", "sound/Jet_down.ogg", "sound/Boom.ogg"]
for x, sound in enumerate(Sound):
    sounds[sound] = pg.mixer.Sound(sound_paths[x])

for sound in sounds:
    sound.set_volume(0.01)

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

        #elif event.type == events[Event.ADDCLOUD]:
        #    Groups()[Group.CLOUDS].add(Cloud())

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    groups[Group.ENEMIES].update()
    groups[Group.CLOUDS].update()
    groups[Group.ROCKETS].update()

    screen.blit(bg, [0,0])
    for enemy in groups[Group.ENEMIES]:
        if pg.sprite.spritecollideany(enemy, groups[Group.ROCKETS]):
            enemy.kill()
            player.score += 1

    for group in groups:
        for entity in group:
            screen.blit(entity.surf, entity.rect)

    screen.blit(player.surf, player.rect)
    screen.blit(font.render(f"SCORE: {player.score}", False, (45, 235, 3)), [5, SCREEN_HEIGHT - 90])
    if pg.sprite.spritecollideany(player, groups[Group.ENEMIES]):
        player.kill()
        sounds[Sound.MOVE_UP].stop()
        sounds[Sound.MOVE_DOWN].stop()
        sounds[Sound.COLLISION].play()
        pg.time.delay(500)
        running = False

    pg.display.flip()
    clock.tick(240)

pg.mixer.music.stop()
pg.mixer.quit()
pg.quit()
