class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def does_pub_have_drinks(self):
        if len(self.drinks) > 0:
            return True

    def remove_drink(self, drink_choice):
        for drink in self.drinks:
            if drink.name == drink_choice:
                self.drinks.remove(drink)
