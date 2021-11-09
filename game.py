import pygame
from pygame.locals import *
from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake - Python 3.8')
        self.surface = pygame.display.set_mode((900, 600))
        self.surface.fill((250, 250, 250))
        self.snake = Snake(self.surface)
        self.score = self.Score()

    class Score:
        def __init__(self):
            self.score = 0
            self.font_size = 42
            self.font = pygame.font.Font(None, self.font_size)
            self.text = self.font.render(f'Score: {self.score}', False, (10, 10, 10))
            self.text_pos = self.text.get_rect()
            self.text_pos.y = self.font_size / 2

        def show(self, surface):
            self.text_pos.x = surface.get_width() - self.text.get_rect().width - self.font_size / 2
            self.text = self.font.render(f'Score: {self.score}', False, (10, 10, 10))
            surface.blit(self.text, self.text_pos)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    else:
                        self.snake.key_pressed(event.key)
                elif event.type == QUIT:
                    running = False
                self.show()

    def show(self):
        self.surface.fill((250, 250, 250))
        self.snake.show()
        self.score.score = self.snake.get_score()
        self.score.show(self.surface)
        pygame.display.flip()
