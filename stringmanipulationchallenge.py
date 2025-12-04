"""
String Operations Program

This program demonstrates:
- Basic string manipulations
- Formatting customer information
- Extracting parts of strings using methods like capitalize(), find(), slicing
- Creating a custom formatted customer ID
"""

# Customer information stored in lowercase
first_name = "Rama Krushna"
last_name = "Pati"
email = "ramakrushna39@gmail.com"

# Capitalize first and last names
formatted_first_name = first_name.capitalize()
formatted_last_name = last_name.capitalize()

# Find the position of '@' in the email
at_position = email.find('@')

# Extract the domain (everything after '@')
domain = email[at_position + 1:]  # slicing after '@'

# Create a formatted customer ID:
# First 3 letters of last name + length of first name + first 3 letters of domain
customer_id = (
    last_name[:3].upper()            # First 3 letters of last name in UPPERCASE
    + str(len(first_name))           # Length of first name
    + domain[:3]                     # First 3 letters of domain
)

# Display all formatted information
print("\n--- Customer Information ---")
print(f"First Name       : {formatted_first_name}")
print(f"Last Name        : {formatted_last_name}")
print(f"Email Address    : {email}")
print(f"@ Position       : {at_position}")
print(f"Email Domain     : {domain}")
print(f"Generated CustID : {customer_id}")
