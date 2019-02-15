from money import Money, Franc


def test_multiplication():
    five = Money.dollar(5)
    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Money.dollar(5) != Franc(5)


def test_franc_multiplication():
    five = Franc(5)
    assert five.times(2) == Franc(10)
    assert five.times(3) == Franc(15)
