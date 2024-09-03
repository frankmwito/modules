# use the os module to list all files and directories in the current working directory.

import os

def list_files_and_directories():
    # Get the current working directory
    current_directory = os.getcwd()
    
    # List all files and directories in current working directory
    items = os.listdir(current_directory)
    
    print(f"Listing all files and directories in: {current_directory}\n")
    
    for item in items:
        print(item)
        
        
list_files_and_directories()