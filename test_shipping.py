from shipping import calculate_shipping


def test_standard_shipping_below_threshold():
    # Arrange
    order_total = 30
    expedited = False
    expected_shipping = 5

    # Act
    result = calculate_shipping(order_total, expedited)

    # Assert
    assert result == expected_shipping


def test_standard_shipping_at_threshold():
    # Arrange
    order_total = 50
    expedited = False
    expected_shipping = 0

    # Act
    result = calculate_shipping(order_total, expedited)

    # Assert
    assert result == expected_shipping


def test_standard_shipping_above_threshold():
    # Arrange
    order_total = 75
    expedited = False
    expected_shipping = 0

    # Act
    result = calculate_shipping(order_total, expedited)

    # Assert
    assert result == expected_shipping


def test_expedited_shipping_below_threshold():
    # Arrange
    order_total = 30
    expedited = True
    expected_shipping = 15

    # Act
    result = calculate_shipping(order_total, expedited)

    # Assert
    assert result == expected_shipping


def test_expedited_shipping_above_threshold():
    # Arrange
    order_total = 75
    expedited = True
    expected_shipping = 10

    # Act
    result = calculate_shipping(order_total, expedited)

    # Assert
    assert result == expected_shipping