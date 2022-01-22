class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {}
        self.food = {}

    def increase_till(self, amount):
        self.till += amount

    def check_customer_over_18(self, customer):
        return True if (customer.age >= 18) else False

    def has_drink(self, drink):
        return True if drink in self.drinks else False

    def remove_drink(self, drink):
        if drink in self.drinks:
            self.drinks.pop(drink)

    def has_food(self, item):
        return True if item in self.food else False

    def remove_food(self, item):
        if item in self.food:
            self.food.pop(item)