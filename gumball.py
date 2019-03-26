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

class Gumball:
    def __init__(self, x, y, color):
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

class Layers:
    def __init__(self, *images):
        self.imgs = []
        for image in images:
            self.imgs.append(image)

    def insert(image, index):
        pass

def main():
    pygame.init()
    time = 0

    # set screen
    screen = pygame.display.set_mode((1080, 980))
    pygame.display.set_caption("Gumball Surprise")

    # time stuff
    clock = pygame.time.Clock()

    machine_l1 = pygame.image.load('gumball_layer_1.png')
    machine_l2 = pygame.image.load('gumball_layer_2.png')
    layers = Layers(machine_l1, machine_l2)


    # game loop
    done = False
    while not done:

        #get input: exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                done = True

        screen.fill(BLACK)


        if time == 100:
            layers.imgs[0] = machine_l2
            layers.imgs[1] = machine_l1

        for image in layers.imgs:
            screen.blit(image, (0,0))



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
