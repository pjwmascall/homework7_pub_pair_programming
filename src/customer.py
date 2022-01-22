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

    def can_afford_item(self, item):
        return True if (self.wallet >= item.price) else False

    def is_not_too_drunk(self):
        return True if (self.drunkenness < 10) else False

    def buy_drink(self, drink, pub):
        if pub.check_customer_over_18(self) is False:
            return False
        if pub.has_drink(drink) is False:
            return False
        if self.is_not_too_drunk() is False:
            return False
        if self.can_afford_item(pub.drinks[drink]) is False:
            return False
        self.reduce_wallet(pub.drinks[drink].price)
        pub.increase_till(pub.drinks[drink].price)
        self.increase_drunkenness(pub.drinks[drink])
        pub.remove_drink(drink)

    def buy_food(self, item, pub):
        if pub.has_food(item) is False:
            return False
        if self.can_afford_item(pub.food[item]) is False:
            return False
        self.reduce_wallet(pub.food[item].price)
        pub.increase_till(pub.food[item].price)
        self.decrease_drunkenness(pub.food[item])
        pub.remove_food(item)