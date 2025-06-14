'''
6.1 Perform basic file system and command-line operations by using  
built-in modules 
• io, os, os.path, sys (importing modules, using modules to open, read, and  
check existence of files, command-line arguments)  
'''
'''
# in the shell: 
>>> import os
>>> os.getcwd()
'/Users/pallaskennedy/Documents/MyPy/Python_cert'

In the shell:
>>>> os.chdir('/Users/pallaskennedy/Documents')
>>>> os.getcwd()
'/Users/pallaskennedy/Documents'


#####    Basic File System Operations:    #####

## io Module:
# The io module provides tools for working with I/O streams. However,
# for basic file operations, you'll usually use the built-in open function.


## os Module:
# The os module provides a way to interact with the operating system.
# Common operations include:

os.getcwd(): Get the current working directory.
os.listdir(path): Get a list of files and directories in the specified path.
os.mkdir(path): Create a new directory.
os.remove(path): Remove a file.
os.rmdir(path): Remove an empty directory.
os.path.exists(path): Check if a file or directory exists.

# Example
import os
current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)


## os.path Module:
The os.path module provides common operations on file paths:

os.path.join(path, *paths): Join one or more path components.
os.path.abspath(path): Return the absolute version of a path.
os.path.basename(path): Return the base name of a path.
os.path.dirname(path): Return the directory name of a path.


##  sys Module
# The sys module provides access to some variables used or maintained
# by the Python interpreter and functions that interact with the interpreter:

sys.argv     List of command-line arguments passed to the script.
sys.exit()    Exit the Python interpreter.


####    File Operations:    #####

## Opening and Reading Files:
# Use the open function to open a file and return a file object.
# Common modes include 'r' for reading, 'w' for writing, and 'a' for appending.

# Example:
with open('example.txt', 'r') as file:
    content = file.read()

## Writing to Files:
Use 'w' mode to open a file for writing. This will create a new file or
overwrite an existing one.

# Example:
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
    
## Command-Line Arguments:
Access command-line arguments using sys.argv.

#Example:

import sys
script_name = sys.argv[0]
arguments = sys.argv[1:]


### Example Script Combining File and Command-Line Operations:
import os
import sys

def process_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of {file_path}:\n{content}")
    else:
        print(f"{file_path} does not exist.")


# This script takes a file path as a command-line argument, checks if
# the file exists, and prints its content if it does.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        process_file(file_path)


