import sys

import pygame

from pygame.locals import QUIT, KEYUP

pygame.init()

surface = pygame.display.set_mode((400, 600))

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            print("键盘弹起触发！")
