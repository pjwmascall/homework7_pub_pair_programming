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

    def buy_drink(self, drink_name, pub):
        if pub.check_customer_over_18(self) is False:
            return False
        if pub.has_drink(drink_name) is False:
            return False
        if self.is_not_too_drunk() is False:
            return False
        drink_choice = pub.drinks[drink_name][0]
        if self.can_afford_item(drink_choice) is False:
            return False
        self.reduce_wallet(drink_choice.price)
        pub.increase_till(drink_choice.price)
        self.increase_drunkenness(drink_choice)
        pub.remove_drink(drink_name)

    def buy_food(self, item, pub):
        if pub.has_food(item) is False:
            return False
        food_choice = pub.food[item][0]
        if self.can_afford_item(food_choice) is False:
            return False
        self.reduce_wallet(food_choice.price)
        pub.increase_till(food_choice.price)
        self.decrease_drunkenness(food_choice)
        pub.remove_food(item)