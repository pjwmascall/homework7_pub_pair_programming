import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Burger", 6.00, 3)
    
    def test_drink_has_name(self):
        self.assertEqual("Burger", self.food.name)

    def test_drink_has_price(self):
        self.assertEqual(6.00, self.food.price)