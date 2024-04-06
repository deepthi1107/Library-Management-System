from models import User
from storage import Storage

class UserManager:
    """
    A class to manage users using a storage system.
    """
    def __init__(self, filename):
        """
        Initialize the UserManager with a storage system.
        
        Args:
        - filename (str): The name of the file for storage.
        """
        self.storage = Storage(filename)

    def add_user(self, name, user_id):
        """
        Add a new user to the storage.

        Args:
        - name (str): The name of the user.
        - user_id (str): The ID of the user.

        Returns:
        - int:  -1 if there was an error.
        """

        if not user_id.isnumeric():
            print("x"*50)
            print("Error: user_id must be an integer.")
            return -1
        user_id=int(user_id)
        data = self.storage.load_data()
        for user_data in data:
            if user_data['user_id'] == user_id:
                print("x"*50)
                print(f"Error: Book with user_id {user_id} already exists in storage.")
                return -1

        user = User(name, user_id)
        self.storage.append_data(vars(user))



    def update_user(self, user_id, name=None):
        """
        Update the information of an existing user.

        Args:
        - user_id (str): The ID of the user to update.
        - name (str): The new name (optional).

        Returns:
        - int:  -1 if there was an error.
        """
        if not user_id.isnumeric():
            print("x"*50)
            print("Error: user_id must be an integer.")
            return -1
        user_id=int(user_id)
        users = self.storage.load_data()
        for user_data in users:
            if user_data["user_id"] == user_id:
                if name:
                    user_data["name"] = name
                self.storage.save_data(users)
                return
        print("x"*50)
        print("User not found.")
        print("x"*50)

    def delete_user(self, user_id):
        """
        Delete a user from the storage.

        Args:
        - user_id (str): The ID of the user to delete.

        Returns:
        - int:  -1 if there was an error.
        """
        if not user_id.isnumeric():
            print("x"*50)
            print("Error: user_id must be an integer.")
            return -1
        user_id=int(user_id)
        users = self.storage.load_data()
        for index, user_data in enumerate(users):
            if user_data["user_id"] == user_id:
                del users[index]
                self.storage.save_data(users)
                return
        print("x"*50)
        print("User not found.")
        print("x"*50)
        

    def list_users(self):
        """
        List all users in the storage.
        """
        users = self.storage.load_data()
        users.sort(key=lambda x: x["user_id"]) 
        if users:
            for user_data in users:
                user = User(**user_data)
                print(user)
        else:
            print("No users found in storage.")

    def search_users(self, attribute, value):
        """
        Search for users based on an attribute and value.

        Args:
        - attribute (str): The attribute to search by ('name', 'user_id').
        - value (str): The value to search for.

        Returns:
        - int:  -1 if there was an error or no users found.
        """
        if attribute not in ["name", "user_id"]:
            print("x" * 50)
            print("Error: Attribute must be one of 'name', or 'user_id'.")
            return -1
        
        if attribute == "user_id" and not value.isnumeric():
            print("x" * 50)
            print("Error: user_id must be an integer.")
            return -1
        user_id=int(user_id) if attribute == "user_id" else value
        users = self.storage.load_data()
        found_users = []
        for user_data in users:
            user = User(**user_data)
            if getattr(user, attribute, None) == value:
                found_users.append(user)
        if found_users:
            for user in found_users:
                print(user)
        else:
            print("x"*50)
            print("No users found.")
            print("x"*50)