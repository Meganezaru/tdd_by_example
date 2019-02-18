from abc import ABC, abstractmethod


class Bank:
    def reduce(self, source, target_currency):
        return source.reduce(target_currency)

    def add_rate(self, param, param1, param2):
        pass


class Expression(ABC):
    @abstractmethod
    def reduce(self, target_currency):
        raise NotImplemented


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, target_currency):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, target_currency)


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False

        return self._currency == other._currency and self._amount == other._amount

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, target_currency):
        return self
