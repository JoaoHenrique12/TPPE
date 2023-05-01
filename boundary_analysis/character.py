from . import MAX_HEALTH

class character:
    def __init__(self, name="Default", health=100):
        self.name = name
        self.health = health

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be integer")
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.__amount = amount

    def sum_health(self, amount=0):
        self.amount = amount

        if amount + self.health > MAX_HEALTH:
            self.health = MAX_HEALTH
        else:
            self.health += amount

    def reduce_health(self, amount=0):
        self.amount = amount

        if self.health - amount < 0:
            self.health = 0
        else:
            self.health -= amount

