from money import Money, Bank, Sum


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


def test_plus_return_sum():
    five = Money.dollar(5)
    sum_expression = five.plus(five)
    assert sum_expression.augend == five
    assert sum_expression.addend == five


def test_reduce_sum():
    sum_expression = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum_expression, "USD")
    assert result == Money.dollar(7)


def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert result == Money.dollar(1)


def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert result == Money.dollar(1)


def test_identify_rate():
    assert Bank().rate("USD", "USD") == 1


def test_mixed_addition():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_francs), "USD")
    assert result == Money.dollar(10)


def test_sum_plus_money():
    five_bucks = Money.dollar(5)
    ten_franc = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    expression_sum = Sum(five_bucks, ten_franc).plus(five_bucks)
    result = bank.reduce(expression_sum, "USD")
    assert result == Money.dollar(15)
