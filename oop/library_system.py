# library_system.py

# Base class (Baba)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived class 1: EBook (Mtoto)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size       # Unique to EBook

    def get_details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __str__(self):
        return f"EBook: {self.title}, {self.author}, File Size: {self.file_size}KB"

# Derived class 2: PrintBook (Mtoto)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count     # Unique to PrintBook

    def get_details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __str__(self):
        return f"PrintBook: {self.title}, {self.author}, Page Count: {self.page_count}"

# Composition class: Library (Binamu)
class Library:
    def __init__(self):
        self.books = []  # This is a list to hold Book, EBook, or PrintBook objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_details())
