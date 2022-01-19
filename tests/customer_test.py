import unittest
from src.customer import Customer
from src.pub import Pub
from src.drinks import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Paul", 1000.00)
        self.pub = Pub("my pub", 100000)
        self.drink = Drink("corona", 5.00)

    def test_customer_has_name(self):
        self.assertEqual("Paul", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(1000.00, self.customer.wallet)

    def test_reduce_money(self):
        self.customer.reduce_money(5.00)
        self.assertEqual(995.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buying_drink(self.drink, self.pub)
        self.assertEqual(995.00, self.customer.wallet )
        self.assertEqual(self.pub.name, "my pub")