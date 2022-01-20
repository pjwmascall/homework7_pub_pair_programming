class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def check_customer_over_18(self, customer):
        if (customer.age >= 18):
            return True
        else:
            return False

    def remove_drink(self, drink_choice):
        for drink in self.drinks:
            if drink.name == drink_choice:
                self.drinks.remove(drink)
                return True
        return False
