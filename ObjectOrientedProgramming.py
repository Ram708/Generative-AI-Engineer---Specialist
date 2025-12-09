"""
Object-Oriented Programming (OOP) – Data Types Demonstration

Covers:
- Using strings with classes
- Using dictionaries with objects
- Using tuples in OOP
- Using sets in OOP
- Classes, objects, methods, constructors
- Encapsulation concepts
"""

print("\n===== 1. OOP with STRINGS =====")

class Person:
    def __init__(self, name):
        self.name = name  # String attribute

    def greet(self):
        return f"Hello, my name is {self.name}!"  # String method return


p = Person("Rama")
print(p.greet())
print("Uppercase name:", p.name.upper())


print("\n===== 2. OOP with DICTIONARIES =====")

class Student:
    def __init__(self, name, scores):
        # scores is a dictionary: {"math": 90, "science": 85}
        self.name = name
        self.scores = scores

    def get_score(self, subject):
        return self.scores.get(subject, "Subject not found")

    def all_scores(self):
        return self.scores


s = Student("Sita", {"math": 92, "science": 88, "english": 90})

print("Student name:", s.name)
print("Math score:", s.get_score("math"))
print("All scores:", s.all_scores())


print("\n===== 3. OOP with TUPLES =====")

class Point:
    def __init__(self, x, y):
        self.coordinates = (x, y)  # tuple stored

    def display(self):
        print(f"Point Coordinates: {self.coordinates}")

    def x_value(self):
        return self.coordinates[0]


point1 = Point(10, 20)
point1.display()
print("X value:", point1.x_value())


print("\n===== 4. OOP with SETS =====")

class UniqueItems:
    def __init__(self):
        self.items = set()  # set attribute

    def add_item(self, item):
        self.items.add(item)  # only unique items
        print(f"Added: {item}")

    def show_items(self):
        return self.items


u = UniqueItems()
u.add_item("apple")
u.add_item("banana")
u.add_item("apple")  # duplicate
print("Unique items:", u.show_items())


print("\n===== 5. COMBINED OOP EXAMPLE – All Data Types Together =====")

class Product:
    def __init__(self, name, price, tags, specifications):
        self.name = name                      # string
        self.price = price                    # number
        self.tags = set(tags)                 # set
        self.specifications = specifications  # dictionary
        self.dimensions = (10, 5, 2)          # tuple example

    def display_info(self):
        print(f"\nProduct: {self.name}")
        print(f"Price: {self.price}")
        print(f"Tags: {self.tags}")           # set
        print(f"Specifications: {self.specifications}")  # dictionary
        print(f"Dimensions (tuple): {self.dimensions}")

    def add_tag(self, tag):
        self.tags.add(tag)


product1 = Product(
    "Laptop",
    55000,
    ["electronics", "computer", "tech"],
    {"RAM": "16GB", "CPU": "i7", "Storage": "512GB SSD"}
)

product1.display_info()
product1.add_tag("premium")
print("Updated Tags:", product1.tags)


print("\n===== END OF OOP DATA TYPE DEMO =====\n")
