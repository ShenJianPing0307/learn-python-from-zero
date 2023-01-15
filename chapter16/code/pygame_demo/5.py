import sys
import pygame

pygame.draw

pygame.init()

surface = pygame.display.set_mode((400, 600))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEWHEEL:
            print("MOUSEWHEEL")

