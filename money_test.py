from money import Money


def test_multiplication():
    five = Money.dollar(5)
    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.dollar(5) != Money.franc(5)


def test_currency():
    assert Money.dollar(1).currency() == "USD"
    assert Money.franc(1).currency() == "CHF"


def test_simple_addition():
    five = Money.dollar(5)
    sum_expression = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum_expression, "USD")
    assert reduced == Money.dollar(10)
