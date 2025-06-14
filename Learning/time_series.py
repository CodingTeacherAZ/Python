''''
Skip the first line in the file
Find and process the first line of data in the file
For each of the remaining lines:
    Process the data on that line

This is to be used with Time Series Data Library
'''
from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    '''Skip the header in a TSDL reader and
    return the first real piece of data'''

    # Read the description line
    line = reader.readline()

    # Find the first non-comment line
    line = reader.readline()
    while line.startswith("#"):
        line = reader.readline()

    # Now line contains the first real peice of data
    return line

def process_file(reader: TextIO) -> None:
    ''' Read and print the data from the reader.
    which must start with a single description
    line, then a sequence of lines beginning with
    '#', then a sequence of data.'''

    # Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)

    # read the rest of the data
    for line in reader:
        line = line.strip()
        print(line)

if __name__ == '__main__':
    with open('hopedale_full.txt', 'r') as input_file:
        process_file(input_file)
