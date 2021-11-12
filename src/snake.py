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

    def key_pressed(self, key):             # if Key.DIRECTION pressed, change direction
        if key == K_UP and self.direction != K_DOWN:
            self.direction_next = K_UP
        elif key == K_RIGHT and self.direction != K_LEFT:
            self.direction_next = K_RIGHT
        elif key == K_LEFT and self.direction != K_RIGHT:
            self.direction_next = K_LEFT
        elif key == K_DOWN and self.direction != K_UP:
            self.direction_next = K_DOWN

    def move(self):                         # Move Head to next block and update body
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

    def show(self, part):
        # Draw snake
        my_range = range(1, len(self.body) - 1)
        if self.body[0][0] == self.body[1][0] and self.body[0][1] == self.body[1][1]:
            my_range = range(2, len(self.body)-1)
        for i in my_range:
            x = self.body[i][0] * self.block_size
            y = self.body[i][1] * self.block_size
            block = pygame.Rect(x, y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, self.color, block)
        # Smooth Head
        b = self.body[0]
        b_size = self.block_size
        direction = self.direction
        x = b[0] * b_size
        y = b[1] * b_size
        if direction == K_RIGHT:
            x += (part - 1) * b_size
        elif direction == K_LEFT:
            x += b_size * (1 - part)
        elif direction == K_UP:
            y += b_size * (1 - part)
        elif direction == K_DOWN:
            y += (part - 1) * b_size
        block = pygame.Rect(x, y, b_size, b_size)
        pygame.draw.rect(self.surface, self.color, block)
        # Smooth Tail
        b = self.body[len(self.body)-1]
        b_size = self.block_size
        b_len = len(self.body)
        direction = [self.body[b_len-2][0] - self.body[b_len-1][0], self.body[b_len-2][1] - self.body[b_len-1][1]]
        x = b[0] * b_size
        y = b[1] * b_size
        if direction == [1, 0]:
            x += part*b_size
        elif direction == [-1, 0]:
            x -= part*b_size
        elif direction == [0, -1]:
            y -= part*b_size
        elif direction == [0, 1]:
            y += part*b_size
        block = pygame.Rect(x, y, b_size, b_size)
        pygame.draw.rect(self.surface, self.color, block)

    def get_score(self):
        return len(self.body) - 4
