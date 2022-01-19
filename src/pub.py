class Pub:
    # pass
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def do_we_have_drink(self):
        if len(self.drinks) >= 1:
            return True

    def remove_drink(self, drink_choice):
        for drink in self.drinks:
            if drink.name == drink_choice:
                self.drinks.remove(drink)

# {
#     "name": "corona"
# }