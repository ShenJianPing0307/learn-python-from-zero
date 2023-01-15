import sys
import pygame
from pygame.locals import QUIT
from pygame import draw

pygame.font
pygame.init()

surface = pygame.display.set_mode((600, 400))  # 创建surface

draw.line(surface, (255, 255, 0), (20, 20), (50, 50))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()  # 更新屏幕，显示线条
