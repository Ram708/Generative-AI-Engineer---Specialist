"""
Library Management System

This program manages books, authors, and borrowers using nested
data structures. It demonstrates:
- Nested dictionaries, lists, and tuples
- Safe updates and queries
- Data validation and integrity
- Date comparison logic
"""

from datetime import datetime
from typing import Dict, List, Tuple


# -----------------------------
# Library Data Structure
# -----------------------------
library = {
    "books": [
        {
            "title": "Python Basics",
            "author": ("John", "Doe"),
            "isbn": "1111111111",
            "copies_available": 3,
            "borrowers": [
                {"name": "Alice", "due_date": "2023-12-01"},
            ],
        },
        {
            "title": "Advanced Python",
            "author": ("Jane", "Smith"),
            "isbn": "2222222222",
            "copies_available": 2,
            "borrowers": [],
        },
        {
            "title": "Data Science Essentials",
            "author": ("Emily", "Clark"),
            "isbn": "3333333333",
            "copies_available": 1,
            "borrowers": [
                {"name": "Bob", "due_date": "2023-10-15"},
            ],
        },
        {
            "title": "Machine Learning 101",
            "author": ("John", "Doe"),
            "isbn": "4444444444",
            "copies_available": 4,
            "borrowers": [],
        },
        {
            "title": "Algorithms Explained",
            "author": ("Alan", "Turing"),
            "isbn": "5555555555",
            "copies_available": 2,
            "borrowers": [
                {"name": "Carol", "due_date": "2023-11-10"},
            ],
        },
    ]
}


# -----------------------------
# Functions
# -----------------------------
def check_out_book(title: str, borrower_name: str, due_date: str) -> str:
    """
    Check out a book to a borrower.

    Decrements copies_available and adds borrower info.
    """
    for book in library["books"]:
        if book["title"].lower() == title.lower():
            if book["copies_available"] <= 0:
                return f"No copies available for '{title}'."

            book["copies_available"] -= 1
            book["borrowers"].append(
                {"name": borrower_name, "due_date": due_date}
            )
            return f"'{title}' checked out to {borrower_name}."

    return f"Book titled '{title}' not found."


def books_by_author(last_name: str) -> List[str]:
    """
    Return a list of book titles by the given author's last name.
    """
    result = []

    for book in library["books"]:
        _, author_last = book["author"]
        if author_last.lower() == last_name.lower():
            result.append(book["title"])

    return result


def overdue_books(current_date: str) -> Dict[str, List[str]]:
    """
    Return a dictionary of overdue books.

    Keys: book titles
    Values: list of borrower names with overdue books
    """
    overdue: Dict[str, List[str]] = {}
    current = datetime.strptime(current_date, "%Y-%m-%d")

    for book in library["books"]:
        overdue_borrowers = []

        for borrower in book["borrowers"]:
            due = datetime.strptime(borrower["due_date"], "%Y-%m-%d")
            if due < current:
                overdue_borrowers.append(borrower["name"])

        if overdue_borrowers:
            overdue[book["title"]] = overdue_borrowers

    return overdue


def add_new_book(
    title: str,
    author: Tuple[str, str],
    isbn: str,
    copies_available: int,
) -> str:
    """
    Add a new book to the library.

    Ensures ISBN uniqueness and correct structure.
    """
    for book in library["books"]:
        if book["isbn"] == isbn:
            return "Error: A book with this ISBN already exists."

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "copies_available": copies_available,
        "borrowers": [],
    }

    library["books"].append(new_book)
    return f"Book '{title}' added successfully."


# -----------------------------
# Demonstration
# -----------------------------
def main():
    """Demonstrate library system functionality."""
    print("\n--- Check Out Book ---")
    print(check_out_book("Python Basics", "David", "2023-12-20"))
    print(check_out_book("Data Science Essentials", "Eva", "2023-12-05"))

    print("\n--- Books by Author (Doe) ---")
    print(books_by_author("Doe"))

    print("\n--- Overdue Books as of 2023-11-01 ---")
    overdue = overdue_books("2023-11-01")
    for title, borrowers in overdue.items():
        print(f"{title}: {borrowers}")

    print("\n--- Add New Book ---")
    print(
        add_new_book(
            "Deep Learning Fundamentals",
            ("Andrew", "Ng"),
            "6666666666",
            5,
        )
    )

    print("\n--- Attempt Duplicate ISBN ---")
    print(
        add_new_book(
            "Duplicate Book",
            ("Test", "Author"),
            "1111111111",
            1,
        )
    )


if __name__ == "__main__":
    main()
