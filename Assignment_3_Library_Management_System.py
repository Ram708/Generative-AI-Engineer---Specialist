"""
Library Management System
This program demonstrates encapsulation and controlled access
using properties in Python classes.
"""


class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    @property
    def title(self):
        """
        Gets the book title.
        """
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Book title cannot be empty.")
        self.__title = value

    @property
    def author(self):
        """
        Gets the book author.
        """
        return self.__author

    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Author name cannot be empty.")
        self.__author = value

    @property
    def isbn(self):
        """
        Gets the book ISBN.
        """
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not (value.isdigit() and len(value) == 13):
            raise ValueError("ISBN must be a 13-digit numeric string.")
        self.__isbn = value

    def display_book(self):
        """
        Displays book details.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("-" * 40)


class Member:
    """
    Represents a library member.
    """

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []

    @property
    def name(self):
        """
        Gets the member name.
        """
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Member name cannot be empty.")
        self.__name = value

    @property
    def member_id(self):
        """
        Gets the member ID.
        """
        return self.__member_id

    @member_id.setter
    def member_id(self, value):
        if not value.strip():
            raise ValueError("Member ID cannot be empty.")
        self.__member_id = value

    @property
    def borrowed_books(self):
        """
        Returns a copy of borrowed books to maintain encapsulation.
        """
        return list(self.__borrowed_books)

    def borrow_book(self, book):
        """
        Allows the member to borrow a book.
        """
        if book in self.__borrowed_books:
            print("Book already borrowed.")
        else:
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        """
        Allows the member to return a borrowed book.
        """
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed.")

    def display_member_details(self):
        """
        Displays member details and borrowed books.
        """
        print(f"Member Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        if self.__borrowed_books:
            print("Borrowed Books:")
            for book in self.__borrowed_books:
                print(f"- {book.title}")
        else:
            print("No books borrowed.")
        print("-" * 40)


# Testing the system
book_1 = Book("Clean Code", "Robert C. Martin", "9780132350884")
book_2 = Book("Atomic Habits", "James Clear", "9780735211292")

member_1 = Member("Rama Krushna Pati", "M001")

member_1.borrow_book(book_1)
member_1.borrow_book(book_2)
member_1.display_member_details()

member_1.return_book(book_1)
member_1.display_member_details()
