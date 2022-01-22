class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    def decrease_drunkenness(self, food):
        if self.drunkenness > food.rejuvenation_level:
            self.drunkenness -= food.rejuvenation_level
        else:
            self.drunkenness = 0

    def can_afford_drink(self, drink):
        return True if (self.wallet >= drink.price) else False

    def can_afford_food(self, food):
        return True if (self.wallet >= food.price) else False

    def is_not_too_drunk(self):
        return True if (self.drunkenness < 10) else False

    def buy_drink(self, drink, pub):
        if pub.check_customer_over_18(self) is False:
            return False
        if pub.has_drink(drink) is False:
            return False
        if self.is_not_too_drunk() is False:
            return False
        if self.can_afford_drink(pub.drinks[drink]) is False:
            return False
        self.reduce_wallet(pub.drinks[drink].price)
        pub.increase_till(pub.drinks[drink].price)
        pub.remove_drink(drink)

    def buy_food(self, food, pub):
        if pub.has_food(food) is False:
            return False
        if self.can_afford_food(pub.food[food]) is False:
            return False
        self.reduce_wallet(pub.food[food].price)
        pub.increase_till(pub.food[food].price)
        pub.remove_food(food)