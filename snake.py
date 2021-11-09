import pygame
from pygame.locals import *


class Snake:
    def __init__(self, surface):
        self.surface = surface
        self.block_size = 30
        self.width = surface.get_width() // self.block_size
        self.height = surface.get_height() // self.block_size
        self.direction = K_RIGHT
        start = [self.width // 3, self.height // 2]
        self.body = [
            start,
            [start[0] - 1, start[1]],
            [start[0] - 2, start[1]],
            [start[0] - 3, start[1]]
        ]

    def key_pressed(self, key):
        # move all other ? (for now)
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        # if time to move
        if key == K_UP:
            self.body[0][1] -= 1
        elif key == K_RIGHT:
            self.body[0][0] += 1
        elif key == K_LEFT:
            self.body[0][0] -= 1
        elif key == K_DOWN:
            self.body[0][1] += 1

    def show(self):
        block_color = (30, 240, 10, 200)
        for b in self.body:
            x = b[0] * self.block_size
            y = b[1] * self.block_size
            block = pygame.Rect(x, y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, block_color, block)

    def get_score(self):
        return len(self.body) - 4
