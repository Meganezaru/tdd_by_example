class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._amount == other._amount

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount)


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
