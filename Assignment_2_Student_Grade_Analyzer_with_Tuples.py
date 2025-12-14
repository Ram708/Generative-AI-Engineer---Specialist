"""
Student Grade Analyzer
This program analyzes student grades using immutable tuple data structures.
"""

# Student data: (student_id, name, (math, science, english))
student_data = (
    (101, "Alice", (90, 85, 92)),
    (102, "Bob", (78, 88, 84)),
    (103, "Charlie", (95, 91, 89)),
    (104, "Diana", (82, 79, 88)),
    (105, "Ethan", (88, 90, 85)),
)


def get_top_student(data):
    """
    Finds the student with the highest average grade.
    Returns (student_name, average_grade).
    """
    top_student = max(
        data,
        key=lambda student: sum(student[2]) / len(student[2])
    )

    average_grade = sum(top_student[2]) / len(top_student[2])
    return top_student[1], round(average_grade, 2)


def get_subject_grades(data, subject_index):
    """
    Returns a tuple of grades for a specific subject.
    Subject index: 0 = Math, 1 = Science, 2 = English
    """
    return tuple(
        student[2][subject_index]
        for student in data
    )


def grade_summary(data):
    """
    Returns a tuple containing:
    (highest_grade, lowest_grade, overall_average)
    """
    all_grades = tuple(
        grade
        for student in data
        for grade in student[2]
    )

    highest = max(all_grades)
    lowest = min(all_grades)
    average = sum(all_grades) / len(all_grades)

    return highest, lowest, round(average, 2)


# Function calls and output
top_student_name, top_average = get_top_student(student_data)
math_grades = get_subject_grades(student_data, 0)
science_grades = get_subject_grades(student_data, 1)
english_grades = get_subject_grades(student_data, 2)
summary = grade_summary(student_data)

print("Top Student:", top_student_name, "-", top_average)
print("Math Grades:", math_grades)
print("Science Grades:", science_grades)
print("English Grades:", english_grades)
print("Grade Summary (High, Low, Avg):", summary)
