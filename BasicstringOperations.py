# Basic String Operations in Python

# 1. Creating Strings
str1 = "Hello"
str2 = 'Python Programming'
str3 = """This is a 
multi-line string."""

print("1. Strings:")
print(str1)
print(str2)
print(str3)
print("-" * 40)


# 2. String Concatenation
concat_str = str1 + " " + "World"
print("2. Concatenation:", concat_str)
print("-" * 40)


# 3. String Repetition
repeat_str = str1 * 3
print("3. Repetition:", repeat_str)
print("-" * 40)


# 4. String Length
print("4. Length of str2:", len(str2))
print("-" * 40)


# 5. Indexing and Slicing
print("5. Indexing:", str1[0], str1[1])     # H, e
print("   Slicing:", str2[0:6])             # Python
print("   Last character:", str2[-1])       # g
print("-" * 40)


# 6. Useful String Methods
print("6. String Methods:")
print("Uppercase:", str2.upper())
print("Lowercase:", str2.lower())
print("Title Case:", str2.title())
print("Replace:", str2.replace("Python", "Java"))
print("Split:", str2.split())
print("Join:", "-".join(["Python", "Programming", "Basics"]))
print("-" * 40)


# 7. Checking Substrings
print("7. Substring check:")
print("Is 'Python' in str2?", "Python" in str2)
print("Is 'Java' in str2?", "Java" in str2)
print("-" * 40)


# 8. Strip (removing spaces)
str4 = "   Hello Python!   "
print("8. Strip Example:")
print("Original:", "[" + str4 + "]")
print("Stripped:", "[" + str4.strip() + "]")
print("-" * 40)


# 9. String Formatting
name = "Rama"
age = 25
print("9. String Formatting:")
print(f"My name is {name} and I am {age} years old.")
print("Using format(): My name is {} and I am {} years old.".format(name, age))
print("-" * 40)


# 10. Escaping Characters
escape_str = "He said, \"Python is awesome!\""
print("10. Escaping Characters:", escape_str)
print("-" * 40)
