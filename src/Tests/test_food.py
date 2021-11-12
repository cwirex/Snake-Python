import unittest
from src.food import *


class TestFood(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.food = Food(40, pygame.display.set_mode((800, 600)))

    def test_init(self):
        self.assertIsNotNone(self.food)

    def test_renew_small(self):
        self.food = Food(1, pygame.display.set_mode((1, 1)))
        self.food.renew([])
        self.assertEqual(self.food.position, [0, 0])

    def test_renew(self):
        body = []
        for i in range(800//40):
            for j in range(600//40//2):
                body.append([i, j])
        for t in range(10):
            self.food.renew(body)
            self.assertNotIn(self.food.position, body)

    def test_renew_one_free(self):
        body = []
        for i in range(800//40):
            for j in range(600//40):
                body.append([i, j])
        body.pop(0)
        self.food.renew(body)
        self.assertEqual(self.food.position, [0, 0])

    def test_renew_all_taken(self):
        body = []
        for i in range(800 // 40):
            for j in range(600 // 40):
                body.append([i, j])
        self.food.renew(body)
        self.assertEqual(self.food.position, [-1, -1])


if __name__ == '__main__':
    unittest.main()
