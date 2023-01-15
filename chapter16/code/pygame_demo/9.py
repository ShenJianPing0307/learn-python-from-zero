import sys
import pygame


pygame.init()

surface = pygame.display.set_mode((800, 600))

pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()