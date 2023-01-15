import sys
import pygame

pygame.init()

surface = pygame.display.set_mode((400, 600))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("w")
            if event.key == pygame.K_DOWN:
                print("s")
            if event.key == pygame.K_LEFT:
                print("a")
            if event.key == pygame.K_RIGHT:
                print("d")
