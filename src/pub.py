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

    def add_drink(self, drink):
        if drink.name in self.drinks:
            self.drinks[drink.name][1] += 1
        else:
            self.drinks[drink.name] = [drink, 1]

    def has_drink(self, drink):
        return True if drink in self.drinks else False

    def remove_drink(self, drink):
        if drink in self.drinks:
            if self.drinks[drink][1] > 1:
                 self.drinks[drink][1] -= 1
            else:
                self.drinks.pop(drink)

    def add_food(self, item):
        if item.name in self.food:
            self.food[item.name][1] += 1
        else:
            self.food[item.name] = [item, 1]

    def has_food(self, item):
        return True if item in self.food else False

    def remove_food(self, item):
        if item in self.food:
            if self.food[item][1] > 1:
                self.food[item][1] -= 1
            else:
                self.food.pop(item)

    def get_total_drinks_and_stock_value(self):
        current_item_quantity = 0
        stock_total = 0
        value_total = 0
        for drink in self.drinks:
            current_item_quantity = self.drinks[drink][1]
            value_total += self.drinks[drink][0].price * current_item_quantity
            stock_total += current_item_quantity
            current_item_quantity = 0
        return [stock_total, value_total]

    def get_total_food_and_stock_value(self):
        current_item_quantity = 0
        stock_total = 0
        value_total = 0
        for item in self.food:
            current_item_quantity = self.food[item][1]
            value_total += self.food[item][0].price * current_item_quantity
            stock_total += current_item_quantity
            current_item_quantity = 0
        return [stock_total, value_total]


