"""
The `Storage` class provides functionality to save, load, and append data to a JSON file. It uses the `json` 
module to handle data serialization and deserialization, providing a convenient way to store and retrieve 
structured data in a file-based format.
"""
import json

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def append_data(self, new_data):
        data = self.load_data()
        data.append(new_data) 
        self.save_data(data)

