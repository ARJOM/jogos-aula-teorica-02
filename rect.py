import random
# from random import randint

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

screen.lock()
for count in range(10):
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    random_pos = (random.randint(0, 639), random.randint(0, 479))
    random_size = (639 - random.randint(random_pos[0], 639), 479 - random.randint(random_pos[1], 479))
    pygame.draw.rect(screen, random_color, Rect(random_pos, random_size))


screen.unlock()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
