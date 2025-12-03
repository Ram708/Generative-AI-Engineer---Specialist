
#Input Operations (input())
# Basic input
name = input("Enter your name: ")
print("Hello", name)
#Input is always a string, so convert when needed
#Integer input
age = int(input("Enter your age: "))
print("Your age is:", age)
#Float input
height = float(input("Enter your height in meters: "))
print("Height:", height)
#Taking multiple inputs in one line
a, b = input("Enter two numbers: ").split()
print(a, b)
#With type conversion:
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)
#Output Operations (print())
print("Welcome to Python!")

#Printing multiple values
x = 10
y = 20
print("Values are:", x, y)
#Using sep (separator) & end in print 
print("A", "B", "C", sep="-")
print("Hello", end=" ")
print("World")
#Practical Input-Output Example
name = input("Enter your name: ")
math = int(input("Enter math marks: "))
science = int(input("Enter science marks: "))

total = math + science
print(f"Hello {name}, your total marks = {total}")
