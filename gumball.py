"""Gumball animation game stuff.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame as pg
from pygame.locals import *


def main():
    pg.init()

    # set screen
    screenrect = Rect(0,0, 1080,720)
    screen = pg.display.set_mode(screenrect.size)

    # set background
    background = pg.Surface(screenrect.size).convert()
    background.fill((255, 0,0))
    screen.blit(background, (0,0))
    pg.display.update()

    # sprite stuff
    all_sprites = pg.sprite.RenderUpdates()

    # time stuff
    clock = pg.time.Clock()

    # game loop
    while 1:

        #get input: exit game
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                break

        # clear sprites
        all_sprites.clear(screen,background)

        # update all_sprites
        all_sprites.update()

        # redraw sprites
        dirty = all_sprites.draw(screen)
        pg.display.update(dirty)

        # maintain frame rate
        clock.tick(30)


if __name__ == '__main__':
    main()
