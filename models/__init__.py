#!/usr/bin/python3
"""init file"""


from models.engine.file_storage import FileStorage

# creates a Filestorage instance
storage = FileStorage()
# Method to deserializes a JSON file to an attribute __objects
# This is the first thing to do: check if there are any objects
storage.reload()
