"""
Vector Class
This module defines a 2D Vector class using magic methods
to support arithmetic operations and comparisons.
"""

import math


class Vector:
    """
    Represents a 2D mathematical vector.
    """

    def __init__(self, x, y):
        """
        Initializes a vector with x and y components.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Adds two vectors and returns a new Vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtracts one vector from another and returns a new Vector.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """
        Checks if two vectors are equal.
        """
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """
        Returns a readable string representation of the vector.
        """
        return f"Vector({self.x}, {self.y})"

    # Optional / Extra Credit Methods

    def __mul__(self, scalar):
        """
        Performs scalar multiplication.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        """
        Returns the magnitude (rounded to nearest integer).
        """
        return int(math.sqrt(self.x ** 2 + self.y ** 2))


# Testing the Vector class
vector_1 = Vector(3, 4)
vector_2 = Vector(1, 2)

print("Vector 1:", vector_1)
print("Vector 2:", vector_2)

print("Addition:", vector_1 + vector_2)
print("Subtraction:", vector_1 - vector_2)
print("Equality Check:", vector_1 == vector_2)

print("Scalar Multiplication:", vector_1 * 2)
print("Vector Length (Magnitude):", len(vector_1))
