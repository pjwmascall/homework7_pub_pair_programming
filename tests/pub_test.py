import unittest
from src.pub import Pub
from src.drinks import Drink
from src.food import Food
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_check_customer_age_pass(self):
        customer = Customer("Jack", 60.00, 19)
        age_check = self.pub.check_customer_over_18(customer)
        self.assertEqual(True, age_check)

    def test_check_customer_age_fail(self):
        customer = Customer("Jill", 80.00, 17)
        age_check = self.pub.check_customer_over_18(customer)
        self.assertEqual(False, age_check)

    def test_has_drink_pass(self):
        self.pub.drinks["Beer"] = Drink("Beer", 5.00, 3)
        self.assertEqual(True, self.pub.has_drink("Beer"))

    def test_has_drink_fail(self):
        self.pub.drinks["Beer"] = Drink("Beer", 5.00, 3)
        self.assertEqual(False, self.pub.has_drink("Wine"))

    def test_has_drink_fail_no_drinks(self):
        self.assertEqual(False, self.pub.has_drink("Beer"))

    def test_remove_drink(self):
        self.pub.drinks["Beer"] = Drink("Beer", 5.00, 3)
        self.pub.drinks["Gin"] = Drink("Gin", 6.00, 4)
        self.pub.remove_drink("Beer")
        self.assertEqual(1, len(self.pub.drinks))

    def test_remove_drink_one_drink(self):
        self.pub.drinks["Beer"] = Drink("Beer", 5.00, 3)
        self.pub.remove_drink("Beer")
        self.assertEqual(0, len(self.pub.drinks))

    def test_remove_drink_no_drinks(self):
        self.assertEqual(None, self.pub.remove_drink("Beer"))

    def test_has_food_pass(self):
        self.pub.food["Burger"] = Food("Burger", 6.00, 3)
        self.assertEqual(True, self.pub.has_food("Burger"))

    def test_has_food_fail(self):
        self.pub.food["Burger"] = Food("Burger", 6.00, 3)
        self.assertEqual(False, self.pub.has_food("Soup"))

    def test_has_food_fail_no_food(self):
        self.assertEqual(False, self.pub.has_food("Burger"))

    def test_remove_food(self):
        self.pub.food["Burger"] = Food("Burger", 6.00, 3)
        self.pub.food["Chips"] = Food("Chips", 2.00, 1)
        self.pub.remove_food("Burger")
        self.assertEqual(1, len(self.pub.food))

    def test_remove_food_one_item(self):
        self.pub.food["Burger"] = Food("Burger", 6.00, 3)
        self.pub.remove_food("Burger")
        self.assertEqual(0, len(self.pub.food))

    def test_remove_food_no_food(self):
        self.assertEqual(None, self.pub.remove_food("Burger"))
