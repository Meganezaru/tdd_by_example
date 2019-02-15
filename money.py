from abc import abstractmethod


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._amount == other._amount

    @classmethod
    def dollar(cls, amount):
        return Dollar(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Franc(amount, "CHF")

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier, self._currency)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier, self._currency)

