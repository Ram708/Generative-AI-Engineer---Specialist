"""
Customer Database System

This program manages customer information for an e-commerce platform
using dictionaries and sets. It demonstrates:
- Nested dictionaries for structured data
- Sets for unique purchase tracking
- Set operations (union, intersection)
- Dictionary comprehension
- Error handling and clean code organization
"""


# Customer database with nested dictionaries and sets
customer_db = {
    "C1001": {
        "name": "Alice",
        "email": "alice@example.com",
        "purchase_history": {101, 205, 308},
        "loyalty_points": 1500,
    },
    "C1002": {
        "name": "Bob",
        "email": "bob@example.com",
        "purchase_history": {101, 402},
        "loyalty_points": 950,
    },
    "C1003": {
        "name": "Charlie",
        "email": "charlie@example.com",
        "purchase_history": {205, 308, 501},
        "loyalty_points": 1200,
    },
    "C1004": {
        "name": "Diana",
        "email": "diana@example.com",
        "purchase_history": {101, 308},
        "loyalty_points": 1800,
    },
    "C1005": {
        "name": "Evan",
        "email": "evan@example.com",
        "purchase_history": {402, 501},
        "loyalty_points": 700,
    },
}


def add_purchase(customer_id, product_id):
    """
    Add a product ID to a customer's purchase history.

    Args:
        customer_id (str): The customer ID.
        product_id (int): The product ID to add.

    Returns:
        str: Status message.
    """
    if customer_id not in customer_db:
        return f"Customer ID {customer_id} not found."

    customer_db[customer_id]["purchase_history"].add(product_id)
    return f"Product {product_id} added to customer {customer_id}."


def common_products(customer_id_1, customer_id_2):
    """
    Return common products purchased by two customers.

    Args:
        customer_id_1 (str): First customer ID.
        customer_id_2 (str): Second customer ID.

    Returns:
        set: Set of common product IDs, or empty set if invalid IDs.
    """
    if customer_id_1 not in customer_db or customer_id_2 not in customer_db:
        return set()

    purchases_1 = customer_db[customer_id_1]["purchase_history"]
    purchases_2 = customer_db[customer_id_2]["purchase_history"]

    return purchases_1.intersection(purchases_2)


def top_customers():
    """
    Return customers with loyalty points greater than 1000.

    Returns:
        dict: Dictionary with customer names as keys and loyalty points as values.
    """
    return {
        data["name"]: data["loyalty_points"]
        for data in customer_db.values()
        if data["loyalty_points"] > 1000
    }


def unique_products():
    """
    Return all unique product IDs purchased by any customer.

    Returns:
        set: Set of all unique product IDs.
    """
    all_products = set()

    for customer in customer_db.values():
        all_products = all_products.union(customer["purchase_history"])

    return all_products


def main():
    """Demonstrate customer database functionality."""

    print("\n--- Add Purchase ---")
    print(add_purchase("C1002", 308))
    print(add_purchase("C9999", 999))

    print("\n--- Common Products ---")
    common = common_products("C1001", "C1003")
    print(f"Common products between C1001 and C1003: {common}")

    print("\n--- Top Customers (Loyalty Points > 1000) ---")
    top = top_customers()
    for name, points in top.items():
        print(f"{name}: {points} points")

    print("\n--- Unique Products Purchased ---")
    print(unique_products())


if __name__ == "__main__":
    main()
