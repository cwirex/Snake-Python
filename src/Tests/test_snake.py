import unittest
from src.snake import *


class TestSnake(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snake = Snake(pygame.display.set_mode((600, 450)), 30)

    def test_init(self):
        self.assertIsNotNone(self.snake)

    def test_score(self):
        self.assertEqual(0, self.snake.get_score())
        self.snake.body.append([0, 0])
        self.assertEqual(1, self.snake.get_score())
        self.snake.body.append([0, 1])
        self.assertEqual(2, self.snake.get_score())

    def test_key_pressed(self):
        first = [self.snake.body[0][0], self.snake.body[0][1]]
        self.assertNotEqual(first, self.snake.body[1])
        self.snake.key_pressed(K_DOWN)
        self.assertEqual(first, self.snake.body[1])
        first[1] += 1
        self.assertEqual(first, self.snake.body[0])


if __name__ == '__main__':
    unittest.main()
