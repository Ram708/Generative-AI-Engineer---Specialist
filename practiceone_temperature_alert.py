"""
Temperature Alert System

This program monitors temperature ranges and provides alerts based on
weather safety thresholds. It demonstrates:
- User input handling with try-except
- Conditional logic with multiple branches
- Edge case and extreme temperature detection
- Clean and readable code organization
"""

# Prompt user for temperature with error handling
try:
    temp_input = input("Enter the current temperature (°C): ")
    temperature = float(temp_input)
except ValueError:
    print("Invalid input! Please enter a numeric temperature.")
    exit()  # Stop program if the input is invalid

print("\n--- Temperature Status ---")

# Check extreme temperatures FIRST
if temperature < 0:
    print("Extreme Cold Warning! Temperature is below freezing.")
elif temperature > 40:
    print("Extreme Heat Warning! Temperature is dangerously high.")
# Standard conditions
elif temperature < 15:
    print("Cold warning! Temperature is low.")
elif temperature == 15 or temperature == 25:
    print("Temperature is at threshold.")
elif 15 < temperature < 25:
    print("Conditions are comfortable.")
else:  # temperature > 25 but not extreme
    print("Heat warning! Temperature is high.")
