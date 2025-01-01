class Publisher:
    def __init__(self, name):
        self.name = name

    def display_publisher(self):
        return f"Publisher: {self.name}"

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display_book(self):
        return f"Book Title: {self.title}, Author: {self.author}"

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display_python_book(self):
        return (f"{self.display_publisher()}\n"
                f"{self.display_book()}\n"
                f"Price: ${self.price}, Pages: {self.pages}")

book = Python(name="O'Reilly", title="Learning Python", author="Mark Lutz", price=39.99, pages=1104)
print(book.display_python_book())
