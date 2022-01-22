import unittest
from src.customer import Customer
from src.pub import Pub
from src.drinks import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 30.00, 20)

    def test_customer_has_name(self):
        self.assertEqual("Joe", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(30.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(20, self.customer.age)

    def test_has_drunkenness(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(5.00)
        self.assertEqual(25.00, self.customer.wallet)

    def test_increase_drunkenness(self):
        drink = Drink("Beer", 5.00, 3)
        self.customer.increase_drunkenness(drink)
        self.assertEqual(3, self.customer.drunkenness)

    def test_decrease_drunkenness(self):
        food = Food("Burger", 6.00, 3)
        self.customer.drunkenness = 7
        self.customer.decrease_drunkenness(food)
        self.assertEqual(4, self.customer.drunkenness)

    def test_decrease_drunkenness_below_zero(self):
        food = Food("Burger", 6.00, 3)
        self.customer.drunkenness = 0.5
        self.customer.decrease_drunkenness(food)
        self.assertEqual(0, self.customer.drunkenness)

    def test_can_afford_item_pass(self):
        item = Drink("Beer", 5.00, 3)
        wallet_check = self.customer.can_afford_item(item)
        self.assertEqual(True, wallet_check)

    def test_can_afford_item_fail(self):
        item = Drink("Champagne", 75.00, 8)
        wallet_check = self.customer.can_afford_item(item)
        self.assertEqual(False, wallet_check)           

    def test_is_not_too_drunk_pass(self):
        self.assertEqual(True, self.customer.is_not_too_drunk())

    def test_is_not_too_drunk_fail(self):
        self.customer.drunkenness = 12
        self.assertEqual(False, self.customer.is_not_too_drunk())

    def test_buy_drink(self):
        pub = Pub("The Prancing Pony", 100.00)
        pub.drinks["Beer"] = Drink("Beer", 5.00, 3)
        self.customer.buy_drink("Beer", pub)
        self.assertEqual(25.00, self.customer.wallet)
        self.assertEqual(105.00, pub.till)
        self.assertEqual(3, self.customer.drunkenness)
        self.assertEqual(0, len(pub.drinks))

    def test_buy_food(self):
        pub = Pub("The Prancing Pony", 100.00)
        pub.food["Burger"] = Food("Burger", 6.00, 3)
        self.customer.drunkenness = 7
        self.customer.buy_food("Burger", pub)
        self.assertEqual(24.00, self.customer.wallet)
        self.assertEqual(106.00, pub.till)
        self.assertEqual(4, self.customer.drunkenness)
        self.assertEqual(0, len(pub.food))