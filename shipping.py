def calculate_shipping(order_total, expedited):
    """Return the shipping charge for the order total and shipping option."""
    if order_total >= 50:
        shipping_cost = 0
    else:
        shipping_cost = 5

    if expedited:
        shipping_cost += 10

    return shipping_cost