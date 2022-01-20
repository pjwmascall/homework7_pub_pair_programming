import unittest
from src.customer import Customer
from src.pub import Pub
from src.drinks import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 60.00)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Beer", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("Joe", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(60.00, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(5.00)
        self.assertEqual(55.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(55.00, self.customer.wallet )
        self.assertEqual(self.pub.name, "The Prancing Pony")