import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Corona", 5.00)
    
    def test_drink_has_name(self):
        self.assertEqual("Corona", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)