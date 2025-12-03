print("Hello, Python!")
print(10 + 20)
# This is a single-line comment

"""
This is a
multi-line comment
"""
name = "Rama"
age = 25
pi = 3.14
is_active = True
"""
String (str)

"""
text = "Hello World"
print(text)
print(type(text))
"""
Integer (int)

"""
x = 10
y = -5
print(x + y)

"""
Float (float)

"""
price = 99.99
print(price)
"""
Boolean (bool)

"""
is_valid = True
is_active = False
print(is_valid)
"""
List

Ordered, changeable, allows duplicates.

"""
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[1])        # banana
fruits.append("orange") # Add item
"""
Tuple

Ordered, unchangeable.
"""
colors = ("red", "blue", "green")
print(colors)

"""
Dictionary (dict)

Key–value pairs.

"""
student = {
    "name": "Rama",
    "age": 23,
    "course": "Python"
}
print(student["name"])


"""""
Set

Unordered, unique values.
"""""
unique_numbers = {1, 2, 3, 4, 4}
print(unique_numbers)  # {1, 2, 3, 4}

"""""
Type Casting
"""""
a = "10"
b = int(a)  # convert string to int
print(b + 5)

"""""
Input From User
"""""
name = input("Rama Krushna Pati: ")
print("Hello", name)

"""""
Bonus: Conditional Example
"""""
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

"""""
Bonus: Loop Example
"""""
for i in range(5):
    print("Hello", i)


"""""
Variables & Operators
"""""
# -------------------------------
# VARIABLES IN PYTHON
# -------------------------------

# Integer variable
age = 25

# Float variable
price = 199.99

# String variable
name = "Rama"

# Boolean variable
is_active = True

print("Age:", age)
print("Price:", price)
print("Name:", name)
print("Active:", is_active)


# -------------------------------
# BASIC OPERATORS
# -------------------------------

a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.33
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 10^3 = 1000

# Comparison Operators
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical Operators
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Assignment Operators
num = 5
num += 3   # num = num + 3
print("After += :", num)

num *= 2   # num = num * 2
print("After *= :", num)


# -------------------------------
# STRING OPERATORS
# -------------------------------

first = "Hello"
second = "World"

# Concatenation
print(first + " " + second)

# Repetition
print(first * 3)
