from abc import abstractmethod


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._amount == other._amount

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount)

    @classmethod
    def franc(cls, amount):
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency


class Dollar(Money):
    def __init__(self, amount):
        super(Dollar, self).__init__(amount=amount, currency="USD")

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super(Franc, self).__init__(amount=amount, currency="CHF")

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

