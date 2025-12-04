"""
Temperature Converter Utility

This program converts temperatures between Celsius and Fahrenheit.
Features:
- Menu-based user interaction
- Input validation for number and scale
- Conversion formulas for C <-> F
- Clean output formatting
"""

def convert_c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def convert_f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def get_valid_temperature():
    """
    Ask the user for a valid numeric temperature.
    Repeats until a correct number is provided.
    """
    while True:
        temp_input = input("Enter the temperature value: ")

        try:
            return float(temp_input)  # Convert to float if valid
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.\n")


def temperature_converter():
    """
    Main function to display menu, ask user for temperature input,
    validate scale type, perform conversion, and display results.
    """
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            temperature = get_valid_temperature()
            converted = convert_c_to_f(temperature)
            print(
                f"\nOriginal: {temperature:.1f}°C"
                f"\nConverted: {converted:.1f}°F\n"
            )

        elif choice == "2":
            temperature = get_valid_temperature()
            converted = convert_f_to_c(temperature)
            print(
                f"\nOriginal: {temperature:.1f}°F"
                f"\nConverted: {converted:.1f}°C\n"
            )

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


# Run the program
if __name__ == "__main__":
    temperature_converter()
