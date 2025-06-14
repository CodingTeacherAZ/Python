import random
import json

def initialize_variables() -> None:
    global upper_range
    global set_size
    upper_range = int(input("What is the largest number in the data set? "))
    set_size = int(input("How many numbers would you like to test? "))

def list_of_random_numbers(upper_range: int, data_set_size: int) -> list:
    '''Generate a list of random integers'''
    return [random.randint(0, upper_range) for _ in range(data_set_size)]

def extract_first_digit(number: int) -> int:
    '''Extract the first digit of any number'''
    return int(str(number)[0])

def digit_count(digit: int) -> None:
    '''Create a dictionary to count occurrences of the digits'''
    global frequency
    if digit not in frequency:
        frequency[digit] = 1
    else:
        frequency[digit] += 1

# global variables
frequency = {}
upper_range = 10000
set_size = 200000

'''
# While the user wants to play
playing = True
while playing:
    playing = input("Do you want to see if a random data set conforms to Benford's Law? (y or n) ").lower() == 'y'
    if playing:
        initialize_variables()
        initial_list = list_of_random_numbers(upper_range, set_size)
        first_digit_list = [extract_first_digit(value) for value in initial_list]
        for value in first_digit_list:
            digit_count(value)
        print(frequency)
        frequency = {}  # Reset frequency for the next iteration
'''
