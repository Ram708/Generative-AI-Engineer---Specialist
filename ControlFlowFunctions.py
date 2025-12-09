"""
Python Concepts Demonstration
---------------------------------
This script teaches:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Break and continue statements
- Function creation and calling
- Parameters and return values
- Lambda functions
- Scope and namespaces
"""

print("\n===== Conditional Statements =====")

x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")


print("\n===== For Loop =====")

for i in range(1, 6):
    print(f"Number: {i}")


print("\n===== While Loop =====")

counter = 1
while counter <= 5:
    print(f"Count: {counter}")
    counter += 1


print("\n===== Break Statement =====")

for num in range(1, 10):
    if num == 5:
        print("Stopping loop at 5 using break.")
        break
    print(num)


print("\n===== Continue Statement =====")

for num in range(1, 6):
    if num == 3:
        print("Skipping 3 using continue.")
        continue
    print(num)


print("\n===== Functions (Definition & Calling) =====")

def greet(name):
    """Function with a parameter"""
    print(f"Hello, {name}!")


greet("Rama")


print("\n===== Function With Return Value =====")

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


result = add(10, 20)
print(f"10 + 20 = {result}")


print("\n===== Lambda Functions =====")

square = lambda n: n * n
print("Square of 6:", square(6))

add_lambda = lambda x, y: x + y
print("Lambda Add 5 + 7:", add_lambda(5, 7))


print("\n===== Scope & Namespaces =====")

global_var = "I am global"


def test_scope():
    local_var = "I am local"
    print(local_var)       # Local scope
    print(global_var)      # Accessing global variable


test_scope()

print(global_var)

# Uncommenting the below line will cause an error
# print(local_var)  # local_var is NOT available outside test_scope()
