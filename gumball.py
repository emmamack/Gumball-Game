"""Gumball animation game stuff.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame
from pygame.locals import * # you can skip the modulename. portion and simply use functionname() just like Python's built in functions
from sys import exit
import random
import math


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
        self.orig_image = pygame.image.load(image_name)
        self.orig_size = self.orig_image.get_size()
        self.image = pygame.image.load(image_name)
        self.current_scale = 1
        self.x = x
        self.y = y
    def scale(self, amt, centered = False):
        scale_amt = self.current_scale*amt
        self.image = pygame.transform.scale(
            self.orig_image, (int(self.orig_size[0]*scale_amt), int(self.orig_size[1]*scale_amt)))

        if centered:
            current_size = self.image.get_size()
            self.x -= current_size[0]*(amt - 1)/2
            self.y -= current_size[1]*(amt - 1)/2

        self.current_scale = self.current_scale*amt


def get_index(layers, cl, last = False):
    indices = []
    for ind in range(len(layers)):
        if isinstance(layers[ind], cl):
            if not last:
                return ind
            indices.append(ind)
    return indices[-1]

class Surprise(Machine_layer):
    pass

def gumball_animation(time, t_start, layers):
    t_since = time - t_start
    gumball_ind = get_index(layers, Gumball)
    gumball = layers[gumball_ind]


    speed = 6
    slope = 0.2087
    width = 127

    #knob!
    if t_since == 0:
        angle = 90
        disp_ind = get_index(layers, Machine_layer, last = True)
        dispenser = layers[disp_ind]
        dispense = pygame.transform.rotate(dispenser.image, angle)
        dispenser.image = dispense
        dispenser.x  = 537
        dispenser.y = 380

        gumball.x, gumball.y = 483, 473

    if t_since == int(5.1*width/speed):
        return layers, False, True

    if t_since == int(width/speed) or t_since == int(3*width/speed):
        layers.pop(gumball_ind)
        layers.insert(gumball_ind + 1, gumball)
    if t_since == int(2*width/speed) or t_since == int(4*width/speed):
        layers.pop(gumball_ind)
        layers.insert(gumball_ind - 1, gumball)

    if  (0 < t_since < int(width/speed) or int(2*width/speed) < t_since < int(3*width/speed)
                or int(4*width/speed) < t_since < int(4.4*width/speed)):
        gumball.x += speed
        gumball.y += math.ceil(speed*slope)
    if (int(width/speed) < t_since < int(2*width/speed)
                or int(3*width/speed) < t_since < int(4*width/speed)):
        gumball.x -= speed
        gumball.y += math.ceil(speed*slope)
    if int(4.4*width/speed) < t_since < int(5.1*width/speed):
        gumball.y += speed

    return layers, True, False


def get_dir():
    xs = list(range(-30, -3)) + list(range(3, 30))
    ys = list(range(-15, 30))
    return random.choice(xs), random.choice(ys)

def surprise_animation(time, t_start, layers ,dirx, diry):
    t_since = time - t_start
    gumball_ind = get_index(layers, Gumball)
    gumball = layers[gumball_ind]

    if t_since == 0:
        layers.pop(gumball_ind)
        layers.insert(gumball_ind + 1, gumball)

    if 0 < t_since < 20:
        gumball.x += dirx
        gumball.y -= diry

    if t_since == 20:
        img_name = random.choice(['oompa_caitrin.jpg', 'giraffe.png'])
        surprise = Surprise(img_name, gumball.x, gumball.y)
        surprise.scale(.05)
        layers.append(surprise)

    if 20 < t_since < 40:
        surprise_ind = get_index(layers, Surprise, last = True)
        surprise = layers[surprise_ind]
        surprise.scale(1.1, centered = True)

    if t_since == 40:
        return layers, False, False

    return layers, True, True


def main():
    pygame.init()
    time = 0
    angle = 0

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
        layer.scale(.8)


    # game loop flags
    done = False
    g_playing = False
    s_playing = False
    g_played = False


    while not done:
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        #get input: exit game, check for click
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                done = True
            if event.type == MOUSEBUTTONDOWN and not (g_played or g_playing or s_playing):
                if int(mouse_pos_x) in range(500,595) and int(mouse_pos_y) in range(335,445):#specific clicking area of dispenser
                    g_playing = True
                    t_start = time
                    gumball = Gumball(color = random.choice(colors))
                    layers.insert(1, gumball)

            if event.type == MOUSEBUTTONDOWN and g_played and not (g_playing or s_playing):
                dirx, diry = get_dir()
                if int(mouse_pos_x) in range (510,553) and int(mouse_pos_y) in range(700,730):
                    s_playing = True
                    t_start = time

        screen.fill(BLACK)


        if g_playing:
            layers, g_playing, g_played = gumball_animation(time, t_start, layers)
        if s_playing:
            layers, s_playing, g_played = surprise_animation(time, t_start, layers, dirx, diry)

        for layer in layers:

            if isinstance(layer, Machine_layer) or isinstance(layer, Quarter):
                screen.blit(layer.image, (layer.x,layer.y))
            if isinstance(layer, Gumball):
                pygame.draw.circle(screen, layer.color, (layer.x, layer.y), 10)

        if not g_playing and not g_played:
            if int(mouse_pos_x) in range(500,595) and int(mouse_pos_y) in range(335,445):
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
