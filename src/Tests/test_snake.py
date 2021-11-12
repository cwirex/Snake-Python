import unittest
from src.snake import *


class TestSnake(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snake = Snake(pygame.display.set_mode((800, 600)), 40)

    def test_init(self):
        self.assertIsNotNone(self.snake)

    def test_score(self):
        self.assertEqual(0, self.snake.get_score())
        self.snake.body.append([0, 0])
        self.assertEqual(1, self.snake.get_score())
        self.snake.body.append([0, 1])
        self.assertEqual(2, self.snake.get_score())

    def test_move(self):
        self.snake.body = [
            [2, 1], [1, 1], [0, 1], [0, 0]
        ]
        self.snake.move()
        self.assertEqual(self.snake.body, [
            [3, 1], [2, 1], [1, 1], [0, 1]
        ])


if __name__ == '__main__':
    unittest.main()
