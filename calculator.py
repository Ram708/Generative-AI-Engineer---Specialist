"""
Basic Calculator Program

This program demonstrates fundamental Python concepts such as:
- Variables and operators
- User input handling
- Basic arithmetic operations
- Error handling for division by zero
"""

# Collect user inputs
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Perform arithmetic operations
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number

# Handle division with zero check
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = None  # Using None to represent an invalid division

# Display results
print("\n--- Calculation Results ---")
print(f"{first_number} + {second_number} = {sum_result}")
print(f"{first_number} - {second_number} = {difference_result}")
print(f"{first_number} * {second_number} = {product_result}")

if division_result is not None:
    print(f"{first_number} / {second_number} = {division_result}")
else:
    print("Cannot divide by zero.")
