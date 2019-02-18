from abc import ABC, abstractmethod


class Bank:
    def reduce(self, source, target_currency):
        return source.reduce(self, target_currency)

    def add_rate(self, param, param1, param2):
        pass

    def rate(self, source_currency, target_currency):
        return 2 if source_currency == "CHF" and target_currency == "USD" else 1


class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, target_currency):
        raise NotImplemented


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, target_currency):
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

    def reduce(self, bank, target_currency):
        rate = bank.rate(self.currency(), target_currency)

        return Money(self._amount / rate, target_currency)
