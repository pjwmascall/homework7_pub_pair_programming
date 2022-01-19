import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Paul", 1000.00)

    def test_customer_has_name(self):
        self.assertEqual("Paul", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(1000.00, self.customer.wallet)

    def test_reduce_money(self):
        self.customer.reduce_money(5.00)
        self.assertEqual(995.00, self.customer.wallet)