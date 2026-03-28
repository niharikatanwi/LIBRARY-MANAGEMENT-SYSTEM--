"""
PROJECT: LIBRARY MANAGEMENT SYSTEM

NAME: NIHARIKA TANWI
COURSE: BTECH BIOENGINEERING
UNIVERSITY: VIT BHOPAL UNIVERSITY
REGISTRATION NUMBER: 25BOE10105
"""

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added successfully!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed successfully!")
        else:
            print("Book not found!")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if book in library.books:
            library.books.remove(book)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book}'")
        else:
            print("Book not available!")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)
            print(f"{self.name} returned '{book}'")
        else:
            print("You don't have this book!")


# ---------------- MAIN PROGRAM ---------------- #

library = Library()

# Pre-added books
library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning Basics")
library.add_book("Bioengineering Fundamentals")

student_name = input("\nEnter your name: ")
student = Student(student_name)

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book = input("Enter book name to add: ")
        library.add_book(book)

    elif choice == "3":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "4":
        book = input("Enter book name to borrow: ")
        student.borrow_book(book, library)

    elif choice == "5":
        book = input("Enter book name to return: ")
        student.return_book(book, library)

    elif choice == "6":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
