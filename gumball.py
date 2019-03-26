"""Gumball animation game stuff.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame
from pygame.locals import * # you can skip the modulename. portion and simply use functionname() just like Python's built in functions
from sys import exit

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

class Gumball:#encodes game state
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move_up_layer():
        pass

    def move_down_layer():
        pass

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
        screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Gumball Surprise")

        # set background
        # background = pygame.Surface(screenrect.size).convert()
        # background.fill(BLACK)
        # screen.blit(background, (0,0))
        # pygame.draw.ellipse(background, GREEN, (300, 250, 40, 80), 1)
        # pygame.display.update()


        # sprite stuff
        # all_sprites = pygame.sprite.RenderUpdates()

        # time stuff
        clock = pygame.time.Clock()

        # game loop
        done = False
        while not done:

            #get input: exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    done = True

            screen.fill(BLACK)
            pygame.draw.ellipse(screen, GREEN, (300, 250, 40, 80), 1)

            # clear sprites
            # all_sprites.clear(screen,background)

            # update all_sprites
            # all_sprites.update()

            # redraw sprites
            # dirty = all_sprites.draw(screen)
            # pygame.display.update(dirty)

            # pygame.draw.ellipse(DISPLAYSURF, GREEN, (300, 250, 40, 80), 1)

            # maintain frame rate
            clock.tick(30)

            pygame.display.update()


    if __name__ == '__main__':
        main()
        pygame.display.quit()
        exit()
