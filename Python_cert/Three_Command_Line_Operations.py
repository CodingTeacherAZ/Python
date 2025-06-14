''''
3.2 Construct and analyze code segments that perform console input  and output operations 
Read input from console
using command-line arguments
'''

# Using input() to read input from the console
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))


## Command line SYS
import sys

# Console Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Command-Line Arguments
script_name = sys.argv[0]  # script name
arguments = sys.argv[1:]  # no other arguements 
print(f"Script Name: {script_name}")
print(f"Arguments: {arguments}")

# run the above script from the console using:
#  python script.py argument1 argument2

## Command line ARGPARSE
import argparse

# Command-Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="User's name")
args = parser.parse_args()

# Console Input
if args.name:
    name = args.name
else:
    name = input("Enter your name: ")

# Greeting
print(f"Hello, {name}!")

#run the above script from the console using:
# python script.py --name Jill

