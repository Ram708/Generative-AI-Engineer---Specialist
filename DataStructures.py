#Lists & list comprehensions

#Tuples

#Dictionaries & sets

#Advanced string operations

#Slicing & indexing

#Nested data structures

#collections module basics 

"""
Python Data Structures – Learning Code

Covers:
- Lists and list comprehensions
- Tuples
- Dictionaries and sets
- Advanced string operations
- Slicing and indexing
- Nested data structures
- Working with collections module
"""

print("\n===== 1. LISTS & LIST COMPREHENSIONS =====")

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.append(6)
print("After append(6):", numbers)

numbers.remove(3)
print("After remove(3):", numbers)

squared = [n ** 2 for n in numbers]
print("List comprehension (squares):", squared)

even_squared = [n ** 2 for n in numbers if n % 2 == 0]
print("List comprehension (even squares):", even_squared)


print("\n===== 2. TUPLES =====")

coords = (10, 20)
print("Tuple:", coords)
print("First element:", coords[0])
# coords[0] = 100  # This would cause an error (tuples are immutable)

single_tuple = (5,)  # Note the comma
print("Single-element tuple:", single_tuple)


print("\n===== 3. DICTIONARIES & SETS =====")

student = {
    "name": "Rama",
    "age": 25,
    "courses": ["Python", "Data Science"]
}
print("Dictionary:", student)
print("Name:", student["name"])
print("Courses:", student.get("courses"))

# Add / update
student["age"] = 26
student["city"] = "Bhubaneswar"
print("Updated dictionary:", student)

# Iterate
for key, value in student.items():
    print(f"{key} -> {value}")

# Sets (unique values, no order)
fruits = {"apple", "banana", "orange", "apple"}
print("Set (unique items):", fruits)

fruits.add("mango")
print("After add('mango'):", fruits)

other_fruits = {"banana", "kiwi"}
print("Intersection:", fruits & other_fruits)
print("Union:", fruits | other_fruits)


print("\n===== 4. ADVANCED STRING OPERATIONS =====")

text = "   Python is awesome and powerful. Python is fun.   "
print("Original text:", repr(text))

# strip
clean_text = text.strip()
print("Stripped text:", repr(clean_text))

# replace
replaced_text = clean_text.replace("Python", "Java")
print("Replaced text:", replaced_text)

# split & join
words = clean_text.split()
print("Words list:", words)

joined = "-".join(words)
print("Joined with '-':", joined)

# find, count, startswith, endswith
print("First index of 'Python':", clean_text.find("Python"))
print("Count of 'is':", clean_text.count("is"))
print("Starts with 'Python'?", clean_text.startswith("Python"))
print("Ends with '.' ?", clean_text.endswith("."))

# formatting
name = "Rama"
lang = "Python"
print(f"{name} is learning {lang}.")


print("\n===== 5. SLICING & INDEXING =====")

data_list = [10, 20, 30, 40, 50, 60]
print("List:", data_list)
print("First element:", data_list[0])
print("Last element:", data_list[-1])
print("Slice [1:4]:", data_list[1:4])
print("Slice [:3]:", data_list[:3])
print("Slice [3:]:", data_list[3:])
print("Slice with step [::2]:", data_list[::2])

string_data = "PYTHON"
print("String:", string_data)
print("string_data[0:3]:", string_data[0:3])
print("string_data[::-1] (reverse):", string_data[::-1])


print("\n===== 6. NESTED DATA STRUCTURES =====")

students = [
    {"name": "Rama", "marks": [85, 90, 92]},
    {"name": "Sita", "marks": [78, 88, 91]},
]

for s in students:
    avg = sum(s["marks"]) / len(s["marks"])
    print(f"{s['name']} -> marks: {s['marks']}, average: {avg}")

# Dict with lists and nested dicts
company = {
    "name": "Newon Lab",
    "departments": {
        "dev": ["Python", "Django"],
        "cloud": ["AWS", "Azure"],
    },
}
print("Company name:", company["name"])
print("Dev stack:", company["departments"]["dev"])


print("\n===== 7. WORKING WITH collections MODULE =====")

from collections import Counter, defaultdict, namedtuple, deque

print("\n--- Counter ---")
letters = "abracadabra"
counter = Counter(letters)
print("Counter for 'abracadabra':", counter)
print("Most common letters:", counter.most_common(2))

print("\n--- defaultdict ---")

scores = [("Rama", 90), ("Sita", 85), ("Rama", 95)]
score_map = defaultdict(list)

for name_key, score in scores:
    score_map[name_key].append(score)

print("Defaultdict scores:", dict(score_map))

print("\n--- namedtuple ---")

Person = namedtuple("Person", ["name", "age"])
p1 = Person(name="Rama", age=25)
print("Namedtuple Person:", p1)
print("Person name:", p1.name)

print("\n--- deque ---")

queue = deque([1, 2, 3])
print("Initial deque:", queue)
queue.append(4)
print("After append(4):", queue)
queue.appendleft(0)
print("After appendleft(0):", queue)
queue.pop()
print("After pop():", queue)
queue.popleft()
print("After popleft():", queue)

print("\n===== END OF DATA STRUCTURES DEMO =====\n")
