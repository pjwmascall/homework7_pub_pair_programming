import unittest
from src.customer import Customer
from src.pub import Pub
from src.drinks import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 60.00, 19)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 5.00, 3)
        self.pub.drinks.append(self.drink)
        self.food = Food("Burger", 6.00, 3)
        self.pub.food.append(self.food)

    def test_customer_has_name(self):
        self.assertEqual("Joe", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(60.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(19, self.customer.age)

    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(self.drink)
        self.assertEqual(3, self.customer.drunkenness)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(5.00)
        self.assertEqual(55.00, self.customer.wallet)

    def test_can_afford_drink(self):
        wallet_check = self.customer.can_afford_drink(self.drink)
        self.assertEqual(True, wallet_check)

    def test_can_afford_food(self):
        wallet_check = self.customer.can_afford_food(self.food)
        self.assertEqual(True, wallet_check)

    def test_decrease_drunkenness(self):
        self.customer.drunkenness = 7
        self.customer.decrease_drunkenness(self.food)
        self.assertEqual(4, self.customer.drunkenness)       

    def test_is_not_too_drunk(self):
        self.assertEqual(True, self.customer.is_not_too_drunk())

    def test_is_not_too_drunk_is_false(self):
        self.customer.drunkenness = 10
        self.assertEqual(False, self.customer.is_not_too_drunk())

    def test_buy_drink(self):
        drink_list_length = len(self.pub.drinks)
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(55.00, self.customer.wallet)
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(drink_list_length-1, len(self.pub.drinks))

    def test_buy_food(self):
        food_list_length = len(self.pub.food)
        self.customer.buy_food(self.food, self.pub)
        self.assertEqual(54.00, self.customer.wallet)
        self.assertEqual(106.00, self.pub.till)
        self.assertEqual(food_list_length-1, len(self.pub.food))