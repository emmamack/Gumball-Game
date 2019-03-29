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

class Quarter():
    def __init__(self, image_name, x = 0, y = 0):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)

class Machine_layer:
    def __init__(self, image_name, x = 0, y = 0):
        self.image = pygame.image.load(image_name)
        self.x = x
        self.y = y
    def scale_img(self, amt):
        size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(size[0]*amt), int(size[1]*amt)))

#THIS ISN'T CURRENTLY BEING USED CAUSE IT MIGHT BE REDUNDANT
class Layers:
    def __init__(self, *images):
        self.layers = []
        for image in images:
            self.layers.append(image)

    def insert(self, obj, index):
        self.layers.insert(index, obj)

def get_index(layers, cl):
    for ind in range(len(layers)):
        if isinstance(layers[ind], cl):
            return ind

class Surprise(Quarter):
    pass

# class Mouse(object):
#     for event in pygame.event.get():
#         if event.type == MOUSEBUTTONDOWN:
#             print("Test")

def gumball_animation(time, t_start, layers):
    t_since = time - t_start
    gumball = layers[get_index(layers, Gumball)]

    if  0 < t_since < 150:
        gumball.x += 5
        gumball.y += 5

    return layers

def surprise_animation():
    pass

def main():
    pygame.init()
    time = 0

    # set screen
    screen = pygame.display.set_mode((1080, 980))
    pygame.display.set_caption("Gumball Surprise")

    # time stuff
    clock = pygame.time.Clock()

    #import quarter image and set position
    this_quarter = Quarter('quarter.png')
    this_dark_quarter2 = Quarter('gumball_quarter_dark2.png')



    #initialize and resize gumball machine layers
    machine_l1 = Machine_layer('gumball_layer_1.png', 407, 70)
    machine_l2 = Machine_layer('gumball_layer_2.png', 373, 312)
    machine_l3 = Machine_layer('gumball_layer_3.png', 508, 370)
    machine_l4 = Machine_layer('gumball_layer_4.png', 523, 392)
    layers = [machine_l1, machine_l2, machine_l3, machine_l4]
    for layer in layers:
        layer.scale_img(.8)


    # game loop
    done = False
    gumball_animation_playing = False
    surprise_animation_playing = False

    while not done:
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        print(mouse_pos_x,mouse_pos_y)
        #get input: exit game, check for click
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                done = True
            if event.type == MOUSEBUTTONDOWN: #TODO: change to specific clicking area
                gumball_animation_playing = True
                t_start = time
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                gumball = Gumball(color = random.choice(colors))
                layers.insert(1, gumball)


        screen.fill(BLACK)

        if gumball_animation_playing:
            layers = gumball_animation(time, t_start, layers)

        for layer in layers:
            if isinstance(layer, Machine_layer) or isinstance(layer, Quarter):
                screen.blit(layer.image, (layer.x,layer.y))
            if isinstance(layer, Gumball):
                pygame.draw.circle(screen, layer.color, (layer.x, layer.y), 10)
        if not gumball_animation_playing:
            if int(mouse_pos_x) in range(527,588) and int(mouse_pos_y) in range(394,411):
                screen.blit(this_dark_quarter2.image,(mouse_pos_x-15,mouse_pos_y-15))
            else:
                screen.blit(this_quarter.image,(mouse_pos_x-15,mouse_pos_y-15))

        # maintain frame rate
        clock.tick(30)
        time += 1

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.display.quit()
    pygame.quit()
    exit()
