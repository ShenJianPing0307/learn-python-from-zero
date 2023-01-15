import sys, random
import pygame
from collections import deque
import time
from pygame.locals import *

pygame.init()


class Snake:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Snake, cls).__new__(cls)
        return cls._instance

    def __init__(self, surface):
        self.init_snake = deque([(0, 40), (20, 40), (40, 40)])
        self.surface = surface

    def draw_snake(self):
        for s in self.init_snake:
            pygame.draw.rect(self.surface, (200, 200, 200), (s, (19, 19)))


class Food:

    def __init__(self, surface):
        self.surface = surface
        self.x_range = [x for x in range(0, 601, 20)]
        self.y_range = [y for y in range(0, 481, 20)]
        self.x_food = random.choice(self.x_range) # 20
        self.y_food = random.choice(self.y_range) # 80
        self.snake = Snake(self.surface)

    def get_food(self):
        while (self.x_food, self.y_food) in self.snake.init_snake: # (0, 40), (20, 40), (40, 40), (20, 80)
            self.x_food = random.choice(self.x_range)
            self.y_food = random.choice(self.y_range)
        return self.x_food, self.y_food

    def draw_food(self):
        x, y = self.get_food()
        pygame.draw.rect(self.surface, (100, 255, 100), ((x, y), (19, 19)))


def main():
    surface = pygame.display.set_mode((600, 480))
    pygame.display.set_caption("贪吃蛇")

    snake = Snake(surface)
    food = Food(surface)

    pos = (20, 0)  # 向右

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key in (K_d, K_RIGHT):
                    pos = (20, 0)
                elif event.key in (K_s, K_DOWN):
                    pos = (0, 20)
                elif event.key in (K_a, K_LEFT):
                    pos = (-20, 0)
                elif event.key in (K_w, K_UP):
                    pos = (0, -20)

        surface.fill((40, 40, 60))

        for x in range(20, 600, 20):
            pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, 480), 1)

        for y in range(20, 480, 20):
            pygame.draw.line(surface, (0, 0, 0), (0, y), (600, y), 1)

        time.sleep(0.3)

        next_pos = (snake.init_snake[-1][0] + pos[0], snake.init_snake[-1][1] + pos[1])

        if next_pos == food.get_food():
            snake.init_snake.append(next_pos)
        else:
            snake.init_snake.append(next_pos)
            snake.init_snake.popleft()

        food.draw_food()
        snake.draw_snake()

        pygame.display.flip()


if __name__ == '__main__':
    main()
