import pygame
import time
from pygame.locals import *
from src.snake import Snake
from src.food import Food


class Game:
    def __init__(self):
        # Define game window
        pygame.init()
        pygame.display.set_caption('Snake - Python 3.8')
        self.surface = pygame.display.set_mode((800, 600))
        self.surface.fill((230, 220, 210))
        # Define game properties
        self.block_size = 40
        self.snake = Snake(self.surface, self.block_size)
        self.score = self.Score()
        self.food = Food(self.block_size, self.surface)

    class Score:                # Keep and display the current game score
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
        time_passed = time.time_ns()        # Use time to animate the game
        running = True
        while running:
            # Scan pending events
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    break
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    if not self.pause():
                        running = False
                        break
                elif event.type == KEYDOWN and event.key in [K_LEFT, K_DOWN, K_UP, K_RIGHT]:
                    self.snake.key_pressed(event.key)
            # Look for collisions
            if self.head_to_food():
                self.food.renew(self.snake.body)
                self.snake.body.insert(1, [self.snake.body[0][0], self.snake.body[0][1]])
            elif self.head_to_body() or self.head_to_border():
                running = False
            # Animate
            frequency = 10**9/9
            if time.time_ns() - time_passed >= frequency:
                self.snake.move()
                time_passed = time.time_ns()
            time_part = (time.time_ns() - time_passed)/frequency
            # show(): Update game window
            self.surface.fill((250, 250, 250))
            self.food.show()
            self.snake.show(time_part)
            self.score.score = self.snake.get_score()
            self.score.show(self.surface)
            pygame.display.flip()
        self.game_over()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.run()
                    return
            self.surface.fill((232, 232, 232))
            self.line_show("Welcome to Snake!", 88, 0.5)
            self.line_show("(Press SPACE to start the game)", 36, 0.85)
            pygame.display.flip()

    def pause(self) -> bool:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    return True
            self.surface.fill((232, 232, 232))
            self.line_show("Game paused", 88, 0.5)
            self.line_show("(Press SPACE to continue)", 36, 0.85)
            self.line_show(f"Current score: {self.score.score}", 46, 0.1)
            pygame.display.flip()

    def game_over(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                    break
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.snake = Snake(self.surface, self.block_size)
                    self.run()
            self.surface.fill((232, 232, 232))
            self.line_show("Game Over", 68, 0.4)
            self.line_show(f"Your score: {self.score.score}", 46, 0.5)
            self.line_show("(Press ESCAPE to quit or SPACE to play again)", 36, 0.85)
            pygame.display.flip()

    def head_to_food(self) -> bool:
        return self.snake.body[0] == self.food.position

    def head_to_body(self) -> bool:
        return self.snake.body[0] in self.snake.body[3:]

    def head_to_border(self) -> bool:
        if self.snake.body[0][0] < 0 or self.snake.body[0][1] < 0:
            return True
        if self.snake.body[0][0] >= self.snake.width or self.snake.body[0][1] >= self.snake.height:
            return True
        return False

    def line_show(self, text, size, height):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.surface.get_rect().centerx
        textpos.centery = self.surface.get_height() * height
        self.surface.blit(text, textpos)
