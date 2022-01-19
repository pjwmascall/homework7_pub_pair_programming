import unittest
from src.pub import Pub


# having as an argument unittest.TestCase
class TestPub(unittest.TestCase):
    # pass
    # self.assertEqual/ is defined somewhere in TestCase
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        # Arrange
        # this is the setup
        # Act
        self.pub.increase_till(2.50)
        # Assert
        self.assertEqual(102.50, self.pub.till)
        # Are the three A's to create a test