import pygame
import random


class Food:
    def __init__(self, block_size, surface):
        self.color = (204, 27, 53)
        self.surface = surface
        self.b_size = block_size
        self.width = surface.get_width() // self.b_size
        self.height = surface.get_height() // self.b_size
        self.position = [self.width // 2, self.height // 2]

    def show(self):
        center = [self.position[0] * self.b_size + self.b_size / 2, self.position[1] * self.b_size + self.b_size / 2]
        pygame.draw.circle(self.surface, self.color, center, self.b_size * 0.45)

    def renew(self, s_body):
        free = []
        for i in range(self.width):
            for j in range(self.height):
                if [i, j] not in s_body:
                    free.append([i, j])
        if len(free) == 0:
            self.position = [-1, -1]
        else:
            self.position = random.choice(free)
