import sys
import pygame
from pygame import draw
from pygame.locals import QUIT


pygame.init()

surface = pygame.display.set_mode((400, 600))

c = pygame.Color(255, 234, 60) # pygame.Color("red")

draw.line(surface, c, (20, 20), (50, 50), width=10)

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()


