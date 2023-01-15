import sys
import pygame


pygame.init()

surface = pygame.display.set_mode((800, 600))

ob = pygame.image.load("0bbcb743-5100-45bd-931e-da9b60b949a7.jpg")

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.blit(ob, (0, 0))
    pygame.display.update()