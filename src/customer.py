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
        if (pub.check_customer_over_18(self)):
            if (self.can_afford_drink(drink)):
                if (self.is_not_too_drunk()):
                    if (pub.remove_drink(drink.name)):
                        self.reduce_wallet(drink.price)
                        pub.increase_till(drink.price)

    def buy_food(self, food, pub):
        if (self.can_afford_food(food)):
            if(pub.remove_food(food.name)):
                self.reduce_wallet(food.price)
                pub.increase_till(food.price)

        

    