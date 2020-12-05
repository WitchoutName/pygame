import pygame as pg

pg.init()

screen = pg.display.set_mode([500, 500])

runnig = True
while runnig:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runnig = False

    screen.fill([45,123,57])
    pg.draw.circle(screen, [45,54,45], [250,250], 75)
    pg.display.flip()

pg.quit()