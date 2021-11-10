import pygame
from pygame.locals import *
from src.snake import Snake
from src.food import Food


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake - Python 3.8')
        self.surface = pygame.display.set_mode((600, 450))
        self.surface.fill((250, 250, 250))
        self.block_size = 30
        self.snake = Snake(self.surface, self.block_size)
        self.score = self.Score()
        self.food = Food(self.block_size, self.surface)

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
            if self.head_to_food():
                self.food.renew(self.snake.body)
                self.snake.body.insert(1, [self.snake.body[0][0], self.snake.body[0][1]])       # collisions?
            elif self.head_to_body() or self.head_to_border():
                running = False
            self.show()

    def head_to_food(self) -> bool:
        return self.snake.body[0] == self.food.position

    def head_to_body(self) -> bool:
        return self.snake.body[0] in self.snake.body[2:]

    def head_to_border(self) -> bool:
        if self.snake.body[0][0] < 0 or self.snake.body[0][1] < 0:
            return True
        if self.snake.body[0][0] >= self.snake.width or self.snake.body[0][1] >= self.snake.height:
            return True
        return False

    def show(self):     # show all components
        self.surface.fill((250, 250, 250))
        self.food.show()
        self.snake.show()
        self.score.score = self.snake.get_score()
        self.score.show(self.surface)
        pygame.display.flip()
