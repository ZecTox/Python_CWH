# Write a python program to print the contents of a directory using the OS module. Search online for the function which does that.

import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        # Print each item in the directory
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")

# Specify the directory you want to list
directory_path = '/'  # Change this to your target directory
list_directory_contents(directory_path)
