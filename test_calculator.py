"""
from calculator import calculate_total


def test_calculate_total():
    result = calculate_total(10, 5)
    assert result == 50
"""

from calculator import calculate_total


def test_calculate_total_normal_purchase():
    # Arrange
    price = 10
    quantity = 5
    expected_total = 50

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == expected_total


def test_calculate_total_zero_quantity():
    # Arrange
    price = 10
    quantity = 0
    expected_total = 0

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == expected_total


def test_calculate_total_decimal_price():
    # Arrange
    price = 2.50
    quantity = 3
    expected_total = 7.50

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == expected_total