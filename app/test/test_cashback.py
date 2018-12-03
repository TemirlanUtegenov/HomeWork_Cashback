import pytest

from app.cashback import calculate_cashback

@pytest.mark.parametrize('summ, type_of_operation, expected', [
    (1000, 'original', 10.0),
    (1000, 'vip', 300.0),
    (1000, 'high', 50.0),
    (100000, 'vip', 3000.0)
])

def test_cashback(summ, type_of_operation, expected):
    actual = calculate_cashback(summ, type_of_operation)
    assert expected == actual