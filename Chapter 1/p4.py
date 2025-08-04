import os

# Specify the directory (you can change this to any valid path)
directory = "/"  # Current directory

try:
    # List all files and folders in the directory
    contents = os.listdir(directory)

    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permissions to access this directory.")
