"""
Expense Calculator

This program collects monthly expenses across five categories,
calculates the total, and analyzes each category's percentage
contribution to the total.

Features:
- get_expenses(): collects validated non-negative expense amounts
- calculate_total(): sums expense values from a dictionary
- analyze_expenses(): computes percentage contribution per category
- Clean formatted report output
"""

from typing import Dict


def get_expenses() -> Dict[str, float]:
    """
    Prompt the user to enter expenses for each category and validate input.

    Returns:
        dict: A dictionary with category names as keys and amounts as float values.
    """
    categories = [
        "housing",
        "food",
        "transportation",
        "entertainment",
        "utilities",
    ]
    expenses: Dict[str, float] = {}

    print("\n--- Enter monthly expenses ---")
    for category in categories:
        while True:
            user_input = input(f"Enter expense for {category.capitalize()}: ").strip()
            try:
                amount = float(user_input)
                if amount < 0:
                    print("Amount cannot be negative. Please enter a non-negative number.")
                    continue
                expenses[category] = amount
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value (e.g., 123.45).")

    return expenses


def calculate_total(expenses: Dict[str, float]) -> float:
    """
    Calculate the total of all expense values.

    Args:
        expenses (dict): Dictionary of expenses.

    Returns:
        float: Sum of expense amounts.
    """
    total = 0.0
    for amount in expenses.values():
        total += amount
    return total


def analyze_expenses(expenses: Dict[str, float], total: float) -> Dict[str, float]:
    """
    Calculate the percentage contribution of each category.

    If total is 0, all percentages will be 0.0 to avoid division by zero.

    Args:
        expenses (dict): Dictionary of expenses.
        total (float): Total expenses.

    Returns:
        dict: Dictionary with same keys as expenses but values as percentages.
    """
    percentages: Dict[str, float] = {}
    if total == 0:
        for key in expenses:
            percentages[key] = 0.0
        return percentages

    for key, amount in expenses.items():
        pct = (amount / total) * 100
        percentages[key] = pct
    return percentages


def display_report(expenses: Dict[str, float], total: float, percentages: Dict[str, float]) -> None:
    """
    Print a formatted report showing category, amount, and percentage.

    Args:
        expenses (dict): Expense amounts.
        total (float): Total amount.
        percentages (dict): Percentage contributions.
    """
    print("\n--- Monthly Expense Report ---")
    print(f"{'Category':<15}{'Amount (USD)':>15}{'Percent of Total':>20}")
    print("-" * 50)
    for category, amount in expenses.items():
        pct = percentages.get(category, 0.0)
        print(f"{category.capitalize():<15}{amount:15.2f}{pct:20.1f}%")
    print("-" * 50)
    print(f"{'Total':<15}{total:15.2f}{'100.0%':>20}")


def main() -> None:
    """Main program flow: collect, calculate, analyze, and display."""
    expenses = get_expenses()
    total = calculate_total(expenses)
    percentages = analyze_expenses(expenses, total)
    display_report(expenses, total, percentages)


if __name__ == "__main__":
    main()
