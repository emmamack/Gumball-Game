"""Gumball animation game stuff.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame
from pygame.locals import * # you can skip the modulename. portion and simply use functionname() just like Python's built in functions


class Gumball: #encodes game state
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move_up_layer():
        pass

    def move_down_layer():
        pass

class gumball_window_view

class one_gumball: #model class: encodes state of ball in the pygame
    def __init__(self,height,width,x,y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def play_gumball_animation():
        pass

    def play_prize_animation():
        pass

    def main():
        pygame.init()

        # set screen
        screenrect = Rect(0,0, 1080,720)
        screen = pygame.display.set_mode(screenrect.size)

        # set background
        background = pygame.Surface(screenrect.size).convert()
        background.fill((255, 0,0))
        screen.blit(background, (0,0))
        pygame.display.update()

        # sprite stuff
        all_sprites = pygame.sprite.RenderUpdates()

        # time stuff
        clock = pygame.time.Clock()

        # game loop
        while True:

            #get input: exit game
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    return

            # clear sprites
            all_sprites.clear(screen,background)

            # update all_sprites
            all_sprites.update()

            # redraw sprites
            dirty = all_sprites.draw(screen)
            pygame.display.update(dirty)

            # maintain frame rate
            clock.tick(30)


    if __name__ == '__main__':
        main()
