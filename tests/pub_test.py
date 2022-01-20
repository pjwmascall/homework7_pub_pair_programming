import unittest
from src.pub import Pub
from src.drinks import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.drinks.append( Drink("Beer", 5.00))
        self.pub.drinks.append( Drink("Gin", 6.00))

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_has_drinks(self):
        self.assertEqual(True, self.pub.does_pub_have_drinks())

    def test_remove_drink(self):
        length_of_list = len(self.pub.drinks)
        self.pub.remove_drink("Beer")
        self.assertEqual( length_of_list-1, len(self.pub.drinks))

    