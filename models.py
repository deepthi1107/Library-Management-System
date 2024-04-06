"""
The code defines three classes: `Book`, representing a book with title, author, and ISBN; 
`User`, representing a user with name and user ID; 
and `Checkout`, representing a checkout instance linking a user ID with an ISBN. Each class has a `__str__` method for string representation and appropriate initialization methods.
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

    def update(self, title=None, author=None, isbn=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"


class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
    def __str__(self):
        return f"Book with isbn: {self.isbn} checkout by user with User ID: {self.user_id}"
