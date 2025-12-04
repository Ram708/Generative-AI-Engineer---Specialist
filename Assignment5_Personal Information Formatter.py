"""
Patient Information Processing System

This program collects basic patient information, processes it,
and displays a clean and formatted patient report.

It demonstrates:
- User input handling
- String operations and formatting
- Numeric conversion and validation
- BMI calculation
- Boolean processing for insurance status
- Clean output formatting
"""


def get_valid_number(prompt, number_type=float):
    """
    Validate numeric input.
    Repeats until the user enters a valid number (int or float).
    """
    while True:
        value = input(prompt)

        try:
            return number_type(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def get_valid_yes_no(prompt):
    """
    Ask for a yes/no answer.
    Converts to boolean:
    - yes → True
    - no → False
    """
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False

        print("Invalid response. Please enter 'yes' or 'no'.\n")


def process_full_name(full_name):
    """
    Split full name into first and last name.
    Capitalize each part.
    Return tuple: (first_name, last_name)
    """
    parts = full_name.strip().lower().split()

    if len(parts) < 2:
        print("Please enter at least a first and last name.\n")
        return None

    first_name = parts[0].capitalize()
    last_name = parts[-1].capitalize()

    return first_name, last_name


def main():
    """Main program execution."""

    print("\n--- Patient Information Entry ---\n")

    # Validate and process the full name
    while True:
        full_name_input = input("Enter full name (first and last): ")
        name_data = process_full_name(full_name_input)
        if name_data:
            break

    first_name, last_name = name_data

    # Collect and validate numeric inputs
    age = get_valid_number("Enter age (years): ", int)
    weight_kg = get_valid_number("Enter weight (kg): ", float)
    height_cm = get_valid_number("Enter height (cm): ", float)

    # Insurance (convert yes/no input to boolean)
    has_insurance = get_valid_yes_no("Do you have insurance? (yes/no): ")

    # Calculations
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    weight_lbs = weight_kg * 2.20462

    # Insurance status formatting
    insurance_status = "Insured" if has_insurance else "Uninsured"

    # Final formatted report
    print("\n--- Patient Report ---")
    print(f"Name          : {last_name}, {first_name}")
    print(f"Age           : {age} years")
    print(f"Weight        : {weight_kg:.1f} kg ({weight_lbs:.1f} lbs)")
    print(f"Height        : {height_cm:.1f} cm")
    print(f"BMI           : {bmi:.1f}")
    print(f"Insurance     : {insurance_status}")
    print("\nReport generated successfully.\n")


# Run the program
if __name__ == "__main__":
    main()
