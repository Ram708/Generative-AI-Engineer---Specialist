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
