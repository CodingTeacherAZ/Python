

import sys
import random

#########
# return the total byte size of the object. 
def total_bytes(object):
    return sys.getsizeof(object)
######
def largest(a, b, c):
    return a if (a > b and a > c) else b if (b > c) else c

######     
def describe_age(a):
    return f"You're a(n) {'kid'*(a<13) or 'teenager'*(a<18) or 'adult'*(a<65) or 'elderly'}"

#########
def split_and_merge(string_, separator):
    first_list = string_.split(" ")
    second_list= []
    for element in first_list:
        temp_list = []
        for char in element: 
            temp_list.append(char)
        second_list.append(temp_list)
    for index in range(len(second_list)):
        second_list[index] = separator.join(second_list[index])
    final = " ".join(second_list)

    return final

#######   THIS IS COOL!  #######
def collatz_conjecture(n):
    results = []
    if n > 1:
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                results.append(n)
            else:
                n = 3 * n + 1
                results.append(n)
    return len(results)

#######



def days_difference(day1: int, day2: int) -> int:
    '''Return the number of days between day1 and day2, which are
    both in the range 1-365 (thus indicating the day of the year).'''
    return day2 - day1
########
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    """Return which day of the week it will be days_ahead days from
    current_weekday.
    
    .current_weekday is the current day of the week and is in the
    range 1-7, indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).

    days_ahead is the number of days after today. """
    return (current_weekday + days_ahead + 1) % 7
##############
def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int) -> int:
    """Return the day of the week it will be on birthday_day
    given that the day of the week is current_weekday and the
    day of the year is current_day.
    current_weekday is the current day of the week and is in
    the range 1-7, indicating whether today is Sunday (1), ... Monday (2), ..., Saturday (7).
    current_day and birthday_day are both in the range 1-365."""
    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)
##############

def convert_to_ceslius(fahrenheit: float) -> float:
    '''Returns the nubmer of Celsius degrees equivalent to
    fahrentheit degrees'''
    return (fahrenheit - 32.0) * 5.0 / 9.0
#########


# return the total byte size of the object.
import sys
def total_bytes(object):
    return sys.getsizeof(object)
######
def largest(a, b, c):
    if (a>b) * (a>c): return a
    elif (b>c): return b
    else: return c  

#########
def split_and_merge(string_, separator):
    first_list = string_.split(" ")
    second_list= []
    for element in first_list:
        temp_list = []
        for char in element: 
            temp_list.append(char)
        second_list.append(temp_list)
    for index in range(len(second_list)):
        econd_list[index] = separator.join(second_list[index])
    final = " ".join(second_list)

    return final

#########
def random_numbers_sorted(start, stop, count):
    jump = round((stop - start)/count)
    print(jump)
    list_of_numbers = []
    sum = start
    for i in range(count):
        list_of_numbers.append(sum + random.randint(1,jump))
        sum += jump

    list_of_numbers.sort()
    return list_of_numbers

print(random_numbers_sorted(3,267,9))
