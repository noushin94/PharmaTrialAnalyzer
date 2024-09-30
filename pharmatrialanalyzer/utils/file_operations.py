import os

def save_file(file_path, data):
    """Saves data to the specified file path."""
    with open(file_path, 'w') as file:
        file.write(data)
