import pygame
from pygame.locals import QUIT
import sys

pygame.init() # 初始化所有模块

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("hello world")


while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit() # 卸载所有模块
            sys.exit() # 退出程序
