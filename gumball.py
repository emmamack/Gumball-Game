"""Gumball animation game.
Authors: Emma Mack, Gabriella Bourdon
"""


import pygame
from pygame.locals import * # you can skip the modulename. portion and simply use functionname() just like Python's built in functions
from sys import exit
import random
import math

#global variables -- colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, YELLOW]

class Quarter():
    """Represents a quarter."""
    def __init__(self, image_name, x = 0, y = 0):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)

class Gumball:
    """Represents a gumball. Has no image because  it is drawn as a circle."""
    def __init__(self, x = 0, y = 0, color = RED):
        self.x = x
        self.y = y
        self.color = color

class Machine_layer:
    """Represents a singular layer of the drawing of the machine. Multiple layers
    are necessary so the gumball can weave in front of and behind the pole, and
    the knob can independently rotate.
    """
    def __init__(self, image_name, x = 0, y = 0):
        self.image = pygame.image.load(image_name)
        self.x = x
        self.y = y

        #for use in self.scale
        self.orig_image = pygame.image.load(image_name)
        self.orig_size = self.orig_image.get_size()
        self.current_scale = 1

    def scale(self, amt, centered = False):
        """Scales image by amt. References original image so as not to lose image quality.

        amt: float amount to increase current (not original) size. 1 is no change
        centered: if True, shifts x and y coordinates of object to keep it centered
        on current point
        """
        scale_amt = self.current_scale*amt
        self.image = pygame.transform.scale(
            self.orig_image, (int(self.orig_size[0]*scale_amt), int(self.orig_size[1]*scale_amt)))

        if centered:
            current_size = self.image.get_size()
            self.x -= current_size[0]*(amt - 1)/2
            self.y -= current_size[1]*(amt - 1)/2

        #update current scale to reflect change
        self.current_scale = self.current_scale*amt

class Surprise():
    """Represents a surprise. Has same methods as Machine_layer but cannot be "child"
    of Machine_layer becuase this introduces bugs.
    """
    def __init__(self, image_name, x = 0, y = 0):
        self.image = pygame.image.load(image_name)
        self.x = x
        self.y = y

        #for use in self.scale
        self.orig_image = pygame.image.load(image_name)
        self.orig_size = self.orig_image.get_size()
        self.current_scale = 1

    def scale(self, amt, centered = False):
        """Scales image by amt. References original image so as not to lose image quality.

        amt: float amount to increase current (not original) size. 1 is no change
        centered: if True, shifts x and y coordinates of object to keep it centered
        on current point
        """
        scale_amt = self.current_scale*amt
        self.image = pygame.transform.scale(
            self.orig_image, (int(self.orig_size[0]*scale_amt), int(self.orig_size[1]*scale_amt)))

        if centered:
            current_size = self.image.get_size()
            self.x -= current_size[0]*(amt - 1)/2
            self.y -= current_size[1]*(amt - 1)/2

        #update current scale to reflect change
        self.current_scale = self.current_scale*amt



def get_index(list, cl, last = False):
    """Returns index of first object in a list that is an instance of given class.

    list: list that contains at least one instance of desired class. If no instance
    of class, raises an error.
    cl: name of desired class
    last: if True, returns last index of class instance instead of first
    """
    indices = []
    for ind in range(len(list)):
        if isinstance(list[ind], cl):
            #exit loop and return first index if not finding last index
            if not last:
                return ind
            indices.append(ind)
    return indices[-1]

def gumball_animation(time, t_start, layers):
    """Animates a gumball travelling down gumball machine track. Each time function
    is called, it alters objects in layers to one clock-tick's worth of animation.

    time: current game time
    t_start: start time of gumball animation. Used to determine which step to animate.
    layers: list of objects that contains at least all four machine layers and
    one gumball.

    Returns: altered list of objects and boolean values for flags
    """
    t_since = time - t_start
    #find gumball within layers
    gumball_ind = get_index(layers, Gumball)
    gumball = layers[gumball_ind]

    speed = 6   #gumball speed
    slope = 0.2087  #slope of ramp
    width = 127     #width of chute

    #first timestep: rotate dispenser 90 degrees
    if t_since == 0:
        disp_ind = get_index(layers, Machine_layer, last = True)
        dispenser = layers[disp_ind]
        rotated_dispenser = pygame.transform.rotate(dispenser.image, 90)
        dispenser.image = rotated_dispenser
        dispenser.x  = 537
        dispenser.y = 380

        gumball.x, gumball.y = 483, 473

    #change gumball layer position at specific time steps
    if t_since == int(width/speed) or t_since == int(3*width/speed):
        layers.pop(gumball_ind)
        layers.insert(gumball_ind + 1, gumball)
    if t_since == int(2*width/speed) or t_since == int(4*width/speed):
        layers.pop(gumball_ind)
        layers.insert(gumball_ind - 1, gumball)

    #move gumball down and to the right in certain time intervals
    if  (0 < t_since < int(width/speed) or int(2*width/speed) < t_since < int(3*width/speed)
                or int(4*width/speed) < t_since < int(4.4*width/speed)):
        gumball.x += speed
        gumball.y += math.ceil(speed*slope)

    #move gumball down and to the left in certain time intervals
    if (int(width/speed) < t_since < int(2*width/speed)
                or int(3*width/speed) < t_since < int(4*width/speed)):
        gumball.x -= speed
        gumball.y += math.ceil(speed*slope)

    #move gumball down in last time interval
    if int(4.4*width/speed) < t_since < int(5.1*width/speed):
        gumball.y += speed

    #last timestep: change flags to reflect completion of animation
    if t_since == int(5.1*width/speed):
        return layers, False, True

    return layers, True, False


def get_dir():
    """Returns random integers which represent an x amount and a y amount to travel
    in one clock cycle. Helper function for surprise_animation
    """
    xs = list(range(-30, -3)) + list(range(3, 30))
    ys = list(range(-30, 10))
    return random.choice(xs), random.choice(ys)

def surprise_animation(time, t_start, layers, dirx, diry):
    """Animates gumball travelling to random spot, adds surprise to layers, and
    plays scaling animation for surprise. Each time function is called, it alters
    objects in layers to one clock-tick's worth of animation.

    time: current game time
    t_start: start time of gumball animation. Used to determine which step to animate.
    layers: list of objects that contains at least all four machine layers and
    one gumball.
    dirx: integer amount of pixels to move gumball in x direction each timestep
    diry: integer amount of pixels to move gumball in y direction each timestep

    Returns: altered list of objects and boolean values for flags
    """
    t_since = time - t_start
    #find gumball within layers
    gumball_ind = get_index(layers, Gumball)
    gumball = layers[gumball_ind]

    #change gumabll layer in first time step
    if t_since == 0:
        layers.pop(gumball_ind)
        layers.insert(gumball_ind + 1, gumball)

    #move gumball in specified direction
    if 0 < t_since < 20:
        gumball.x += dirx
        gumball.y += diry

    #insert surprise into layers
    if t_since == 20:
        img_name = random.choice(['cat.png', 'giraffe.png', 'hippo.png', 'turtle.png'])
        surprise = Surprise(img_name, gumball.x, gumball.y)
        surprise.scale(.05)
        layers.append(surprise)
        pygame.mixer.music.load('ding.mp3')
        pygame.mixer.music.play(0)

    #scale surprise a small amount each timestep
    if 20 < t_since < 40:
        surprise_ind = get_index(layers, Surprise, last = True)
        surprise = layers[surprise_ind]
        surprise.scale(1.1, centered = True)

    #last timestep: change flags
    if t_since == 40:
        disp_ind = get_index(layers, Machine_layer, last = True)
        dispenser = layers[disp_ind]
        rotated_dispenser = pygame.transform.rotate(dispenser.image, 90)
        dispenser.image = rotated_dispenser
        dispenser.x  = 523
        dispenser.y = 392
        return layers, False, False

    return layers, True, True



def main():
    """Main game setup and game loop.
    """

    pygame.init()
    time = 0
    angle = 0

    # set screen
    screen = pygame.display.set_mode((1080, 980))
    pygame.display.set_caption("Gumball Surprise")

    # iniialize clock
    clock = pygame.time.Clock()

    #import quarter image and set position
    this_quarter = Quarter('quarter.png')
    this_dark_quarter = Quarter('gumball_quarter_dark.png')

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

    #main game loop
    while not done:

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        #get input
        for event in pygame.event.get():

            #check for quit
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                done = True

            #check for gumball animation click
            if event.type == MOUSEBUTTONDOWN and not (g_played or g_playing or s_playing):
                if int(mouse_pos_x) in range(500,595) and int(mouse_pos_y) in range(335,445):#specific clicking area of dispenser
                    g_playing = True
                    t_start = time
                    gumball = Gumball(color = random.choice(colors))
                    layers.insert(1, gumball)

            #check for surprise animation click
            if event.type == MOUSEBUTTONDOWN and g_played and not (g_playing or s_playing):
                if int(mouse_pos_x) in range (510,553) and int(mouse_pos_y) in range(700,750):
                    dirx, diry = get_dir()
                    s_playing = True
                    t_start = time

        #reinitialize background
        screen.fill(BLACK)

        #play timestep of gumball animation if flags correspond
        if g_playing:
            layers, g_playing, g_played = gumball_animation(time, t_start, layers)

        #play timestep of surprise animation if flags correspond
        if s_playing:
            layers, s_playing, g_played = surprise_animation(time, t_start, layers, dirx, diry)

        #draw all layers onto the screen
        for layer in layers:
            if isinstance(layer, Machine_layer) or isinstance(layer, Quarter) or isinstance(layer, Surprise):
                screen.blit(layer.image, (layer.x,layer.y))
            if isinstance(layer, Gumball):
                pygame.draw.circle(screen, layer.color, (layer.x, layer.y), 10)

        #make quarter follow mouse if flags correspond
        if not g_playing and not g_played:
            if int(mouse_pos_x) in range(500,595) and int(mouse_pos_y) in range(335,445):
                screen.blit(this_dark_quarter.image,(mouse_pos_x-15,mouse_pos_y-15))
            else:
                screen.blit(this_quarter.image,(mouse_pos_x-15,mouse_pos_y-15))

        # maintain frame rate
        clock.tick(30)
        time += 1

        pygame.display.update()


if __name__ == '__main__':
    main()
    #exit game if main game loop ends
    pygame.display.quit()
    pygame.quit()
    exit()
