import pygame
from pygame.locals import *


class Snake:
    def __init__(self, surface, block_size):
        self.color = (30, 179, 77)
        self.surface = surface
        self.block_size = block_size
        self.width = surface.get_width() // self.block_size
        self.height = surface.get_height() // self.block_size
        self.direction = K_RIGHT
        self.direction_next = K_RIGHT
        start = [self.width // 3, self.height // 2]
        self.body = [
            start,
            [start[0] - 1, start[1]],
            [start[0] - 2, start[1]],
            [start[0] - 3, start[1]]
        ]

    def key_pressed(self, key):
        if key == K_UP and self.direction != K_DOWN:
            self.direction_next = K_UP
        elif key == K_RIGHT and self.direction != K_LEFT:
            self.direction_next = K_RIGHT
        elif key == K_LEFT and self.direction != K_RIGHT:
            self.direction_next = K_LEFT
        elif key == K_DOWN and self.direction != K_UP:
            self.direction_next = K_DOWN

    def move(self):
        self.body.pop(len(self.body) - 1)
        self.body.insert(0, [self.body[0][0], self.body[0][1]])
        self.direction = self.direction_next
        if self.direction == K_UP:
            self.body[0][1] -= 1
        elif self.direction == K_RIGHT:
            self.body[0][0] += 1
        elif self.direction == K_LEFT:
            self.body[0][0] -= 1
        elif self.direction == K_DOWN:
            self.body[0][1] += 1

    def show(self):
        for b in self.body:
            x = b[0] * self.block_size
            y = b[1] * self.block_size
            block = pygame.Rect(x, y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, self.color, block)

    def get_score(self):
        return len(self.body) - 4
