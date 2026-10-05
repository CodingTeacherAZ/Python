'''
3. Input and Output Operations 
3.1 Construct and analyze code segments that perform file input and  
output operations 
• open, close, read, write, append, check existence, delete, with statement
'''
#####    open, close    #####
file = open('file_example.txt', 'r')
contents = file.read()
file.close()
print(contents)


#####   with statement    #####
## if there is a problem and an error occurs, it’s possible that our code has an
## error preventing execution of the statement file.close(), and the associated
## resources are never released. Python provides a with statement for situations
## like this where we always want to tidy up, regardless of whether an error occurs.
## For this reason, the with statement is frequently used for file access.

with open('file_example.txt', 'r') as file:
    contents = file.read()
print(contents)

import os
os.chdir('/Users/pallaskennedy/Documents')
with open("The ultimate guide to Warcraft lore in print.txt",'r') as file:
    contents = file.read()
print(contents)


#####    read    ######
os.chdir('/Users/pallaskennedy/Documents/MyPy/Python_Cert')

## read()
# Use read() when you want the entirety of the file in a single string
# with no arguments, read() puts everything from the current file cursor position
# to the end of the file into a single string and moves the cursor to the end of the
# file.

with open('file_example.txt', 'r') as file:
    contents = file.read()
print(contents)


# When called with a single integer, it reads that many characters, and moves the
# file cursor to that point

with open('file_example.txt', 'r') as file:
    first_ten_chars = file.read(10)
    rest_of_file = file.read()
print("The first 10 characters : ", first_ten_chars)
print("The rest of the file : ", rest_of_file)

##  readlines()
# Generates a list of strings splittling text along lines
# Cursor is moved to the end of the file.
# Each string ends with \n

with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()
print(lines)
for element in reversed(lines):
    print(element.strip())
print("--------------------")    
for element in sorted(lines):
    print(element)
print("--------------------")

## for line in file technique
with open('file_example.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))  # each line has \n which adds 1 char to the len
print("--------------------")
## readline() technique
## reads one line at a time
## Use this when you want to read only part of a file

with open('hopedale.txt', 'r') as hopedale_file:
    hopedale_file.readline()  # read and skip the header
    data = hopedale_file.readline().strip()  
    print(data)

    while data.startswith('#'):  # commented lines
        data = hopedale_file.readline().strip()  # read, strip and overwrite the variable
    print(data)                             # the last thing data holds is the first number
    
    total_pelts = int(data)  #conver to int and initialize the tracker variable

    for data in hopedale_file:
        print(data)
        total_pelts += int(data.strip())   # get a running total

print("Total number of pelts : ", total_pelts)
print("--------------------")
##  Files over the internet  ##
#  Module urllib.request
#  function urlopen
#  urllib.urlrequest.read
#  most common encodings is UTF-8


import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
    total_pelts = 0
    for line in webpage:

        line = line.strip()
        line = line.decode('utf-8')
        if line.startswith('C') or line.startswith("#"):
            continue
        else:
            total_pelts += int(line)
print(total_pelts)
print("--------------------")

#####   Write, Append    #####


## 'w' creates a file if it doesn't exist, erases and replaces content if it does exist
with open('topics.txt', 'w') as output_file:
    output_file.write("Computer Science\n")

# 'a' appends to the end of an existing file
with open('topics.txt', 'a') as output_file:
    output_file.write("\tSoftware Engineer\n")

with open('topics.txt', 'r') as file:
    lines = file.read()
    print(lines)



# from typing import TextIO:
# The TextIO type is part of the typing module, and it is used to annotate variables
# that represent text file objects. It's a type hint indicating that a variable is expected
# to be a file object opened in text mode (as opposed to binary mode).
# For example, when you see a function parameter annotated with TextIO,
# it suggests that the function expects a file-like object that deals with text data.
# Here's an example:
from typing import TextIO

def process_text_file(file: TextIO) -> None:
    for line in file:
        # Process each line of the text file
        print(line.strip())
        
with open('file_example.txt', 'r') as file:
    process_text_file(file)

# from io import StringIO:
# The StringIO class is part of the io module and is used to create an in-memory
# file-like object that you can read from and write to as if it were a file. It's particularly
# useful when you want to treat a string as a file, allowing you to use file-related
# operations on it.
# Here's an example:
from io import StringIO

# Create a StringIO object with initial content
sio = StringIO("Hello, this is a StringIO example.")

# Read from the StringIO object
content = sio.read()
print(content)

# Write to the StringIO object
sio.write("\nAppending more text.")
sio.seek(0)  # Move the cursor to the beginning
updated_content = sio.read()
print(updated_content)

# Close the StringIO object (not mandatory, but good practice)
sio.close()
     
def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """Read the data from input_file, which contains two floats per line separated
    by a space. output_file for writing and, for each line in input_file, write a line
    to output_file that contains the two floats from the corresponding line of
    input_file plus a space and the sum of the two floats."""
    for number_pair in input_file:
        number_pair = number_pair.strip() # strip whitespace
        operands = number_pair.split()  #create list
        total = float(operands[0]) + float(operands[1])  # sum elements
        new_line = '{0} sums to {1}\n'.format(number_pair, total)  
        output_file.write(new_line)  #write to new file

if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
         open('number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)



#####    check existence    #####

import os

def file_exists(file_path):
    return os.path.isfile(file_path)
file_path = 'topics.txt'
if file_exists(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")

#####    delete    #####
import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}")

# Example usage:
file_path = "topics.txt"
delete_file(file_path)
