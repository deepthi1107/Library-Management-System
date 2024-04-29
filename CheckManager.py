from models import Checkout
from storage import Storage

class CheckManager:
    """
    A class to manage book checkouts and check-ins.
    """
    def __init__(self, filename):
        """
        Initialize the CheckManager with a storage system.
        
        Args:
        - filename (str): The name of the file for storage.
        """
        self.storage = Storage(filename)
        self.userstorage=Storage("users.json")
        self.bookstorage=Storage("books.json")

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book for a user.

        Args:
        - user_id (str): The ID of the user.
        - isbn (str): The ISBN of the book.

        Returns:
        - int:-1 if there was an error.
        """
        if not user_id.isnumeric() or not isbn.isnumeric():
            print("x"*50)
            print("Error: user_id/isbn must be an integer.")
            return -1
        user_id=int(user_id)
        isbn=int(isbn)
        checkouts = self.storage.load_data()
        userdatastorage=self.userstorage.load_data()
        bookdatastorage=self.bookstorage.load_data()
        user_exists = False
        book_exists = False

        for userdata in userdatastorage:
            if userdata["user_id"] == user_id:
                user_exists = True

        for bookdata in bookdatastorage:
            if bookdata["isbn"] == isbn:
                book_exists = True

        if not user_exists:
            print("x" * 50)
            print(f"User does not exist with provided user_id: {user_id}.")
            return -1

        if not book_exists:
            print("x" * 50)
            print(f"Book with the provided isbn: {isbn} does not exist.")
            return -1
        
        for checkout_data in checkouts:
            if checkout_data["user_id"] == user_id and checkout_data["isbn"] == isbn:
                print("x"*50)
                print("Book is already checked out by this user.")
                return -1
        new_checkout = Checkout(user_id, isbn)
        print(new_checkout)
        self.storage.append_data(vars(new_checkout))
        

    def check_in_book(self, user_id, isbn):
        """
        Check in a book for a user.

        Args:
        - user_id (str): The ID of the user.
        - isbn (str): The ISBN of the book.

        Returns:
        - int:  -1 if there was an error.
        """
        if not user_id.isnumeric() or not isbn.isnumeric():
            print("x"*50)
            print("Error: user_id/isbn must be an integer.")
            return -1
        user_id=int(user_id)
        isbn=int(isbn)
        checkouts = self.storage.load_data()
        userdatastorage=self.userstorage.load_data()
        bookdatastorage=self.bookstorage.load_data()
        user_exists = False
        book_exists = False

        for userdata in userdatastorage:
            if userdata["user_id"] == user_id:
                user_exists = True

        for bookdata in bookdatastorage:
            if bookdata["isbn"] == isbn:
                book_exists = True

        if not user_exists:
            print("x" * 50)
            print(f"User does not exist with provided user_id: {user_id}.")
            return -1

        if not book_exists:
            print("x" * 50)
            print(f"Book with the provided isbn: {isbn} does not exist.")
            return -1
        
        for index, checkout_data in enumerate(checkouts):
            if checkout_data["user_id"] == user_id and checkout_data["isbn"] == isbn:
                del checkouts[index]
                self.storage.save_data(checkouts)
                return
        print("x" * 50)
        print("Book not found in checked out list.")
        return -1

    def list_checkouts(self):
        """
        List all current checkouts.
        """
        checkouts = self.storage.load_data()
        if not checkouts:
            print("No books checked out.")
        else:
            for checkout_data in checkouts:
                checkout = Checkout(**checkout_data)
                print(checkout)
                

    def get_available_books(self):
        """
        List all available books (not checked out).
        """
        checkouts = self.storage.load_data()
        books = self.bookstorage.load_data()

        available_isbns = set(book["isbn"] for book in books)
        checked_out_isbns = set(checkout["isbn"] for checkout in checkouts)

        available_isbns -= checked_out_isbns

        available_books = [book for book in books if book["isbn"] in available_isbns]
        available_books.sort(key=lambda x: x["isbn"])

        if available_books:
            print("=" * 50)
            print("Available Books (Sorted by ISBN)")
            print("=" * 50)
            for book in available_books:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"ISBN: {book['isbn']}")
                print("-" * 50)
        else:
            print("No available books.")
