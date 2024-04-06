"""
The code represents a Library Management System with a command-line interface. It utilizes `BookManager`, `UserManager`, 
and `CheckManager` to manage books, users, and checkouts, respectively. The `main()` function handles user interactions 
through a menu-driven interface, allowing users to add, update, delete, list, and search books/users, as well as check 
books in and out.
"""

from book import BookManager
from user import UserManager
from check import CheckManager

def main_menu():
    print("="*50)
    print("Library Management System")
    print("="*50)
    print("1.  Add Book")
    print("2.  List Books")
    print("3.  Update Book")
    print("4.  Delete Book")
    print("5.  Search Books")
    print("6.  Add User")
    print("7.  List Users")
    print("8.  Update User")
    print("9.  Delete User")
    print("10. Search Users")
    print("11. Check Out Book")
    print("12. Check In Book")
    print("13. List Avialble Books")
    print("14. List Checkedout Books")
    print("15. Exit")
    print("="*50)
    choice = input("Enter choice: ")
    print("="*50)
    return choice

def main():
    book_manager = BookManager("books.json")
    user_manager = UserManager("users.json")
    check_manager = CheckManager("check.json")

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            result=book_manager.add_book(title, author, isbn)
            if result != -1:
                print("Book added successfully.")
            else:
                print("Book not added successfully.")
                print("x"*50)
        elif choice == '2':
            print("List of Books:")
            book_manager.list_books()
        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave empty to keep current): ")
            author = input("Enter new author (leave empty to keep current): ")
            result=book_manager.update_book(isbn, title, author)
            if result != -1:
                print("Book updated successfully.")
            else:
                print("Book not updated successfully.")
                print("x"*50)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            result=book_manager.delete_book(isbn)
            if result != -1:
                print("Book deleted successfully.")
            else:
                print("Book not deleted successfully.")
                print("x"*50)
        elif choice == '5':
            attribute = input("Enter attribute to search (title/author/isbn): ")
            value = input("Enter value to search: ")
            result=book_manager.search_books(attribute, value)
            if result != -1:
                print("Book found successfully.")
            else:
                print("Book not found successfully.")
                print("x"*50)
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            result=user_manager.add_user(name, user_id)
            if result != -1:
                print("User added successfully.")
            else:
                print("User not added successfully.")
                print("x"*50) 
        elif choice == '7':
            print("List of Users:")
            user_manager.list_users()
        elif choice == '8':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (leave empty to keep current): ")
            result=user_manager.update_user(user_id, name)
            if result != -1:
                print("User updated successfully.")
            else:
                print("User not updated successfully.")
                print("x"*50) 
        elif choice == '9':
            user_id = input("Enter user ID of the user to delete: ")
            result=user_manager.delete_user(user_id)
            if result != -1:
                print("User deleted successfully.")
            else:
                print("User not deleted successfully.")
                print("x"*50)
        elif choice == '10':
            attribute = input("Enter attribute to search (name/user_id): ")
            value = input("Enter value to search: ")
            result=user_manager.search_users(attribute, value)
            if result != -1:
                print("User found successfully.")
            else:
                print("User not found successfully.")
                print("x"*50)
        elif choice == '11':
            isbn = input("Enter ISBN of the book to check out: ")
            user_id = input("Enter User id to check out: ")
            result=check_manager.checkout_book(user_id,isbn)
            if result != -1:
                print("Book checked out successfully.")
            else:
                print("Book not checked out successfully.")
                print("x"*50)
        elif choice == '12':
            isbn = input("Enter ISBN of the book to check in: ")
            user_id = input("Enter User id to check out: ")
            result=check_manager.check_in_book(user_id, isbn)
            if result != -1:
                print("Book checked in successfully.")
            else:
                print("Book not checked in successfully.")
                print("x"*50)
        elif choice == '13':
            check_manager.get_available_books()
        elif choice == '14':
            check_manager.list_checkouts()
        elif choice == '15':
            print("-----------Exiting------------")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()