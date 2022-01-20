class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def can_afford_drink(self, drink):
        if (self.wallet >= drink.price):
            return True
        else:
            return False

    def buy_drink(self, drink, pub):
        if (pub.check_customer_over_18(self)):
            if (self.can_afford_drink(drink)):
                if (pub.remove_drink(drink.name)):
                    self.reduce_wallet(drink.price)
                    pub.increase_till(drink.price)

        

    