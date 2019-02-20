from abc import ABC, abstractmethod


class Bank:
    def __init__(self):
        self.rates = dict()

    def reduce(self, source, target_currency):
        return source.reduce(self, target_currency)

    def add_rate(self, source_currency, target_currency, rate):
        target_rate = self.rates.get(source_currency, dict())
        target_rate[target_currency] = rate
        self.rates[source_currency] = target_rate

    def rate(self, source_currency, target_currency):
        if source_currency == target_currency:
            return 1

        return self.rates.get(source_currency, dict()).get(target_currency, -1)


class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, target_currency):
        raise NotImplemented

    @abstractmethod
    def plus(self, addend):
        raise NotImplemented


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, target_currency):
        amount = self.augend.reduce(bank, target_currency)._amount +\
                 self.addend.reduce(bank, target_currency)._amount
        return Money(amount, target_currency)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        pass


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
