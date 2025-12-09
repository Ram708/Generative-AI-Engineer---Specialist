"""
Password Strength Checker

This program validates a user's password using a loop until it meets all
security requirements. It demonstrates:
- While loops
- String validation
- Logical conditions
- Clear error messaging
"""


def validate_password():
    """
    Prompt the user for a password and validate it based on the rules:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (!@#$%^&*)

    Continues asking until the password is valid.
    Returns:
        str: The valid password
    """
    special_chars = "!@#$%^&*"

    while True:
        password = input("Enter a password: ")
        errors = []  # List to collect all error messages

        # Check each condition
        if len(password) < 8:
            errors.append("• Password must be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            errors.append("• Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            errors.append("• Password must contain at least one lowercase letter.")

        if not any(char.isdigit() for char in password):
            errors.append("• Password must contain at least one digit.")

        if not any(char in special_chars for char in password):
            errors.append(
                "• Password must contain at least one special character (!@#$%^&*)."
            )

        # If no errors, password is valid
        if not errors:
            print("Password is valid!")
            return password

        # Print all errors and continue loop
        print("\nPassword is not strong enough. Please fix the following:")
        for message in errors:
            print(message)
        print()  # Blank line for readability


# Run the validator if the script is executed directly
if __name__ == "__main__":
    validate_password()

