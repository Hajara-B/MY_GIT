# Parent class Publisher
class Publisher:
    def __init__(self, name):
        self.name = name  # Publisher's name

    def display_publisher(self):
        return f"Publisher: {self.name}"

# Derived class Book from Publisher
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # Initialize Publisher class
        self.title = title      # Book title
        self.author = author    # Book author

    def display_book(self):
        return f"Book Title: {self.title}, Author: {self.author}"

# Derived class Python from Book
class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)  # Initialize Book class
        self.price = price  # Price of the Python book
        self.pages = pages  # Number of pages in the Python book

    def display_python_book(self):
        return (f"{self.display_publisher()}\n"
                f"{self.display_book()}\n"
                f"Price: ${self.price}, Pages: {self.pages}")

# Example of using these classes
book = Python(name="O'Reilly", title="Learning Python", author="Mark Lutz", price=39.99, pages=1104)
print(book.display_python_book())
