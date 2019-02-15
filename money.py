from abc import abstractmethod


class Money:
    def __init__(self, amount):
        self._amount = amount

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

    @abstractmethod
    def currency(self):
        pass


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def currency(self):
        pass


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def currency(self):
        pass
