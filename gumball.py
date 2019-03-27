"""Gumball animation game stuff.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame
from pygame.locals import * # you can skip the modulename. portion and simply use functionname() just like Python's built in functions
from sys import exit
import animation
import random

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, YELLOW]

class Gumball:
    def __init__(self, x = 0, y = 0, color = RED):
        self.x = x
        self.y = y
        self.color = color

    def move_up_layer():
        pass

    def move_down_layer():
        pass

class Quarter(Gumball):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

class Surprise(Quarter):
    pass

# class Mouse(object):
#     for event in pygame.event.get():
#         if event.type == MOUSEBUTTONDOWN:
#             print("Test")

# def gumball_animation(time, t_start, layers):
#     t_since = time - t_start
#
#     if  0 < t_since < 150:
#         pass
#
#     return layers

def surprise_animation():
    pass

class Layers:
    def __init__(self, *images):
        self.layers = []
        for image in images:
            self.layers.append(image)

    def insert(self, obj, index):
        self.layers.insert(index, obj)

def main():
    pygame.init()
    time = 0

    # set screen
    screen = pygame.display.set_mode((1080, 980))
    pygame.display.set_caption("Gumball Surprise")

    # time stuff
    clock = pygame.time.Clock()

    #initialize layers (gumball machine images)
    machine_l1 = pygame.image.load('gumball_layer_1.png')
    size1 = machine_l1.get_size()
    machine_l1 = pygame.transform.scale(machine_l1, (int(size1[0]*.8), int(size1[1]*.8)))
    machine_l2 = pygame.image.load('gumball_layer_2.png')
    size2 = machine_l2.get_size()
    machine_l2 = pygame.transform.scale(machine_l2, (int(size2[0]*.8), int(size2[1]*.8)))
    machine_l3 = pygame.image.load('gumball_layer_3.png')
    size3 = machine_l3.get_size()
    machine_l3 = pygame.transform.scale(machine_l3, (int(size3[0]*.8), int(size3[1]*.8)))
    print(machine_l3.get_size())
    layers = [(machine_l1, 407, 70), (machine_l2, 372, 312), (machine_l3, 508, 370)]


    # game loop
    done = False
    gumball_animation_playing = False
    surprise_animation_playing = False
    while not done:

        #get input: exit game, check for click
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                done = True
            if event.type == MOUSEBUTTONDOWN: #TODO: change to specific clicking area
                gumball_animation_playing = True
                t_start = time
                gumball = Gumball(color = random.choice(colors))
                layers.insert(1, (gumball, 0, 0))

        screen.fill(BLACK)

        # if gumball_animation_playing:
        #     layers = gumball_animation(time, t_start, layers, gumball)

        for layer in layers:
            if isinstance(layer[0], pygame.Surface):
                screen.blit(layer[0], (layer[1],layer[2]))
            if isinstance(layer[0], Gumball):
                pygame.draw.circle(screen, layer[0].color, (layer[0].x, layer[0].y), 10)

        # maintain frame rate
        clock.tick(30)
        time += 1

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.display.quit()
    pygame.quit()
    exit()






# set background
# background = pygame.Surface(screenrect.size).convert()
# background.fill(BLACK)
# screen.blit(background, (0,0))
# pygame.draw.ellipse(background, GREEN, (300, 250, 40, 80), 1)
# pygame.display.update()


# sprite stuff
# all_sprites = pygame.sprite.RenderUpdates()





# clear sprites
# all_sprites.clear(screen,background)

# update all_sprites
# all_sprites.update()

# redraw sprites
# dirty = all_sprites.draw(screen)
# pygame.display.update(dirty)

# pygame.draw.ellipse(DISPLAYSURF, GREEN, (300, 250, 40, 80), 1)
