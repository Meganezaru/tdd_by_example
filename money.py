class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc:
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        return self._amount == other._amount
