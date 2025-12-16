"""
Shape Hierarchy Module
This module demonstrates the use of abstract base classes
to enforce a common interface for geometric shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the circumference of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


# Testing the shape classes
circle = Circle(7)
rectangle = Rectangle(5, 10)

print("Circle Area:", round(circle.area(), 2))
print("Circle Perimeter:", round(circle.perimeter(), 2))

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
