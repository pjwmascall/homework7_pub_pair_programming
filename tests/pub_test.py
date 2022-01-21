import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.drinks.append(Drink("Beer", 5.00, 3))
        self.pub.drinks.append(Drink("Gin", 6.00, 4))
        self.pub.food.append(Food("Burger", 6.00, 3))
        self.customer = Customer("Joe", 60.00, 19)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_remove_drink(self):
        drink_list_length = len(self.pub.drinks)
        removed = self.pub.remove_drink("Beer")
        self.assertEqual(drink_list_length-1, len(self.pub.drinks))
        self.assertEqual(True, removed)

    def test_check_customer_over_18(self):
        age_check = self.pub.check_customer_over_18(self.customer)
        self.assertEqual(True, age_check)

    