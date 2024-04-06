from models import Book
from storage import Storage

class BookManager:
    """
    A class to manage books using a storage system.
    """
    def __init__(self, filename):
        """
        Initialize the BookManager with a storage system.
        
        Args:
        - filename (str): The name of the file for storage.
        """

        self.storage = Storage(filename)

    def add_book(self, title, author, isbn):
        """
        Add a new book to the storage.

        Args:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - isbn (str): The ISBN of the book.

        Returns:
        - int: -1 if there was an error.
        """
        if not isbn.isnumeric():
            print("x"*50)
            print("Error: ISBN must be an integer.")
            return -1
        isbn=int(isbn)  
        data = self.storage.load_data()
        for book_data in data:
            if book_data['isbn'] == isbn:
                print("x"*50)
                print(f"Error: Book with ISBN {isbn} already exists in storage.")
                return -1

        book = Book(title, author, isbn)
        self.storage.append_data(vars(book))

    def update_book(self, isbn, title=None, author=None):
        """
        Update the information of an existing book.

        Args:
        - isbn (str): The ISBN of the book to update.
        - title (str): The new title (optional).
        - author (str): The new author (optional).

        Returns:
        - int: -1 if there was an error.
        """
        if not isbn.isnumeric():
            print("x"*50)
            print("Error: ISBN must be an integer.")
            return -1
        isbn=int(isbn)
        books = self.storage.load_data()
        for book_data in books:
            if book_data["isbn"] == isbn:
                if title:
                    book_data["title"] = title
                if author:
                    book_data["author"] = author
                self.storage.save_data(books)
                return
        print("x"*50)
        print("Book not found.")


    def delete_book(self, isbn):
        """
        Delete a book from the storage.

        Args:
        - isbn (str): The ISBN of the book to delete.

        Returns:
        - int: -1 if there was an error.
        """
        if not isbn.isnumeric():
            print("x"*50)
            print("Error: ISBN must be an integer.")
            return -1
        isbn=int(isbn)
        books = self.storage.load_data()
        for index, book_data in enumerate(books):
            if book_data["isbn"] == isbn:
                del books[index]
                self.storage.save_data(books)
                return
        print("x"*50)
        print("Book not found.")

    def list_books(self):
        """
        List all books in the storage.
        """
        books = self.storage.load_data()
        books.sort(key=lambda x: x["isbn"])  
        if books:
            for book_data in books:
                book = Book(**book_data)
                print(book)
        else:
            print("No books found in storage.")

    def search_books(self, attribute, value):
        """
        Search for books based on an attribute and value.

        Args:
        - attribute (str): The attribute to search by ('title', 'author', 'isbn').
        - value (str): The value to search for.

        Returns:
        - int: -1 if there was an error or no books found.
        """
        if attribute not in ["title", "author", "isbn"]:
            print("x" * 50)
            print("Error: Attribute must be one of 'title', 'author', or 'isbn'.")
            return -1
        if attribute=="isbn" and not value.isnumeric():
            print("x"*50)
            print("Error: ISBN must be an integer.")
            return -1
        value = int(value) if attribute == "isbn" else value
        books = self.storage.load_data()
        found_books = []
        for book_data in books:
            book = Book(**book_data)
            if getattr(book, attribute, None) == value:
                found_books.append(book)
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("x"*50)
            print("No books found.")
            return -1