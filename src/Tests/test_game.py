import unittest

from src.game import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_init(self):
        self.assertIsNotNone(self.game)

    def test_head_to_body(self):
        self.game.snake.body = [[5, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
        self.assertTrue(self.game.head_to_body())
        self.game.snake.body = [[0, 0], [0, 0], [0, 0]]
        self.assertFalse(self.game.head_to_body())

    def test_head_to_border(self):
        self.assertFalse(self.game.head_to_border())
        self.game.snake.body[0] = [0, 0]
        self.assertFalse(self.game.head_to_border())
        self.game.snake.body[0] = [self.game.snake.width-1, self.game.snake.height-1]
        self.assertFalse(self.game.head_to_border())
        self.game.snake.body[0] = [-1, 0]
        self.assertTrue(self.game.head_to_border())
        self.game.snake.body[0] = [0, self.game.snake.height]
        self.assertTrue(self.game.head_to_border())

    def test_head_to_food(self):
        self.assertFalse(self.game.head_to_food())
        self.game.snake.body[0] = self.game.food.position
        self.assertTrue(self.game.head_to_food())

if __name__ == '__main__':
    unittest.main()
