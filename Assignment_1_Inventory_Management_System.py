"""
Inventory Management System
This program manages products, quantities, and prices using lists
and performs basic inventory operations using list comprehensions.
"""

# Inventory data
products = ["Apple", "Banana", "Milk", "Bread", "Eggs"]
quantities = [50, 75, 8, 20, 5]
prices = [0.99, 0.50, 2.50, 1.80, 3.20]


def low_stock_items(products_list, quantities_list):
    """
    Returns a list of product names with quantity less than 10.
    """
    return [
        products_list[i]
        for i in range(len(quantities_list))
        if quantities_list[i] < 10
    ]


def total_inventory_value(quantities_list, prices_list):
    """
    Calculates the total inventory value.
    """
    return sum(
        quantities_list[i] * prices_list[i]
        for i in range(len(quantities_list))
    )


def add_discount(prices_list, quantities_list):
    """
    Applies a 10% discount to products with quantity greater than 50.
    Returns a new list of discounted prices.
    """
    return [
        round(price * 0.9, 2) if quantities_list[i] > 50 else price
        for i, price in enumerate(prices_list)
    ]


# Function calls and output
low_stock = low_stock_items(products, quantities)
total_value = total_inventory_value(quantities, prices)
discounted_prices = add_discount(prices, quantities)

print("Low Stock Items:", low_stock)
print("Total Inventory Value: $", total_value)
print("Discounted Prices:", discounted_prices)
