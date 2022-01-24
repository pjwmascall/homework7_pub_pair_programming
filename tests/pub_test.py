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

    def test_add_beer_no_drinks(self):
        drink = Drink("Beer", 5.00, 3)
        self.pub.add_drink(drink)
        self.assertEqual(True, self.pub.has_drink("Beer"))

    def test_add_beer_one_beer(self):
        drink = Drink("Beer", 5.00, 3)
        self.pub.add_drink(drink)
        self.pub.add_drink(drink)
        self.assertEqual(1, len(self.pub.drinks))
        self.assertEqual(2, self.pub.drinks["Beer"][1])

    def test_has_drink_pass(self):
        drink = Drink("Beer", 5.00, 3)
        self.pub.add_drink(drink)
        self.assertEqual(True, self.pub.has_drink("Beer"))

    def test_has_drink_fail(self):
        drink = Drink("Beer", 5.00, 3)
        self.pub.add_drink(drink)
        self.assertEqual(False, self.pub.has_drink("Wine"))

    def test_has_drink_fail_no_drinks(self):
        self.assertEqual(False, self.pub.has_drink("Beer"))

    def test_remove_beer_two_beer_one_gin(self):
        drink1 = Drink("Beer", 5.00, 3)
        drink2 = Drink("Gin", 6.00, 4)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.remove_drink("Beer")
        self.assertEqual(2, len(self.pub.drinks))
        self.assertEqual(1, self.pub.drinks["Beer"][1])    

    def test_remove_beer_one_beer_one_gin(self):
        drink1 = Drink("Beer", 5.00, 3)
        drink2 = Drink("Gin", 6.00, 4)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.remove_drink("Beer")
        self.assertEqual(1, len(self.pub.drinks))
        self.assertEqual(1, self.pub.drinks["Gin"][1])

    def test_remove_beer_one_beer(self):
        drink = Drink("Beer", 5.00, 3)
        self.pub.add_drink(drink)
        self.pub.remove_drink("Beer")
        self.assertEqual(0, len(self.pub.drinks))

    def test_remove_drink_no_drinks(self):
        self.assertEqual(None, self.pub.remove_drink("Beer"))

    def test_add_burger_no_food(self):
        food = Food("Burger", 6.00, 3)
        self.pub.add_food(food)
        self.assertEqual(True, self.pub.has_food("Burger"))

    def test_add_burger_one_burger(self):
        food = Food("Burger", 6.00, 3)
        self.pub.add_food(food)
        self.pub.add_food(food)
        self.assertEqual(1, len(self.pub.food))   
        self.assertEqual(2, self.pub.food["Burger"][1])   

    def test_has_food_pass(self):
        food = Food("Burger", 6.00, 3)
        self.pub.add_food(food)
        self.assertEqual(True, self.pub.has_food("Burger"))

    def test_has_food_fail(self):
        food = Food("Burger", 6.00, 3)
        self.pub.add_food(food)
        self.assertEqual(False, self.pub.has_food("Soup"))

    def test_has_food_fail_no_food(self):
        self.assertEqual(False, self.pub.has_food("Burger"))

    def test_remove_burger_two_burgers_one_chips(self):
        food1 = Food("Burger", 6.00, 3)
        food2 = Food("Chips", 2.00, 1)
        self.pub.add_food(food1)
        self.pub.add_food(food1)
        self.pub.add_food(food2)
        self.pub.remove_food("Burger")
        self.assertEqual(2, len(self.pub.food))
        self.assertEqual(1, self.pub.food["Chips"][1])

    def test_remove_burger_one_burger_one_chips(self):
        food1 = Food("Burger", 6.00, 3)
        food2 = Food("Chips", 2.00, 1)
        self.pub.add_food(food1)
        self.pub.add_food(food2)
        self.pub.remove_food("Burger")
        self.assertEqual(1, len(self.pub.food))
        self.assertEqual(1, self.pub.food["Chips"][1])

    def test_remove_burger_one_burger(self):
        food = Food("Burger", 6.00, 3)
        self.pub.add_food(food)
        self.pub.remove_food("Burger")
        self.assertEqual(0, len(self.pub.food))

    def test_remove_food_no_food(self):
        self.assertEqual(None, self.pub.remove_food("Burger")) 
    
    def test_get_total_drinks_and_stock_value(self):
        drink1 = Drink("Beer", 5.00, 3)
        drink2 = Drink("Gin", 6.00, 4)
        for _ in range(5):
            self.pub.add_drink(drink1)
        for _ in range(2):
            self.pub.add_drink(drink2)
        self.pub.drinks["Beer"] = [Drink("Beer", 5.00, 3), 5]
        self.pub.drinks["Gin"] = [Drink("Gin", 6.00, 4), 2]
        self.assertEqual([7, 37], self.pub.get_total_drinks_and_stock_value())

    def test_get_total_drinks_and_stock_value(self):
        food1 = Food("Burger", 6.00, 3)
        food2 = Food("Chips", 2.00, 1)
        self.pub.add_food(food1)
        self.pub.add_food(food2)
        self.assertEqual([2, 8], self.pub.get_total_food_and_stock_value())