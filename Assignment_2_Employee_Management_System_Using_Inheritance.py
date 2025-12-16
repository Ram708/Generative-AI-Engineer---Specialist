"""
Employee Management System
This program demonstrates inheritance and polymorphism
using different types of employees.
"""


class Employee:
    """
    Base class representing a generic employee.
    """

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_salary(self):
        """
        Returns the base salary.
        """
        return self.salary

    def display_details(self):
        """
        Displays employee details.
        """
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.calculate_salary():.2f}")
        print("-" * 40)


class FullTimeEmployee(Employee):
    """
    Represents a full-time employee.
    """

    def calculate_salary(self):
        """
        Returns the fixed monthly salary.
        """
        return self.salary


class PartTimeEmployee(Employee):
    """
    Represents a part-time employee.
    """

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """
        Calculates salary based on hours worked.
        """
        return self.hourly_rate * self.hours_worked


class Intern(Employee):
    """
    Represents an intern employee.
    """

    def __init__(self, name, employee_id, stipend, internship_duration):
        super().__init__(name, employee_id, stipend)
        self.internship_duration = internship_duration  # in months

    def calculate_salary(self):
        """
        Returns the monthly stipend.
        """
        return self.salary


# Testing polymorphism
employees = [
    FullTimeEmployee("Rama Krushna Pati", "FT101", 60000),
    PartTimeEmployee("Anita Sharma", "PT202", hourly_rate=500, hours_worked=40),
    Intern("Rahul Verma", "IN303", stipend=15000, internship_duration=6),
]

for employee in employees:
    employee.display_details()
