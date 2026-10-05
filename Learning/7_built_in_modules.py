'''
6.2 Solve complex computing problems by using built-in modules 
• Math (fabs, ceil, floor, trunc, fmod, frexp, nan, isnan, sqrt, isqrt, pow, pi)  
datetime (now, strftime, weekday), random (randrange, randint, random,  
shuffle, choice, sample) 
 
'''

# built in functions
print(int(34.6))    # 34
print(int(-3.4))    # -3
print(float(21))    #21.0
print(abs(-7))  # 7 -> int
print(abs(3.3))  # 3.3  -> float
print(abs(-7) + abs(3.3))   # 10.3  -> float
print(round(4.3))   # 4  round(value) -> int
print(round(3.141592653, 2))   # 3.14  ->  round(value, decimal precision)
print(pow(abs(-2), round(4.3))) #16 -> pow(base, exp)
print(pow(2, 4, 3)) #1 ->  pow(base, exp, mod)
print(id(3))    #id() gets the memory address of an object
print(min(2, 3, 4))
print(max(2, -3, 4, 7. -5))
print(max(2, -3, min(4, 7), abs(-5)))
print(min(max(3, 4), abs(-5)))
print(abs(min(4, 6, max(2, 8))))
print(round(max(5.572, 3.258), abs(-2)))
# help(abs) in shell to acces documentation on built-in functions


### Math module
from math import fabs, ceil, floor, trunc, fmod, frexp, nan, isnan, sqrt, isqrt, pow, pi
print('math.sqrt(9) : ', sqrt(9)) # 3.0 -> float
print('math.pi : ', pi)   # value for pi
print('math.fabs(9) : ', fabs(9))  # 9.0  forces float
print('math.ceil(9.1) : ', ceil(9.1))  #10  rounds up  ->  int
print('math.ceil(-9.1) : ', ceil(-9.1)) # -9 rounds up -> int
print('math.floor(9.7) : ', floor(9.7)) #9  rounds down same as //1 but returns int
print('9.7 // 1 : ', 9.7 // 1)  ## 9.0 returns float
print('math.floor(-9.7) : ', floor(-9.7)) # -10 rounds down same as //1 but returns int
print('-9.7 // 1 : ', -9.7 // 1) #-10.0  returns float
print('math.trunc(3.8) : ', trunc(3.8))  # 3
print('math.trunc(-3.8) : ', trunc(-3.8))  # -3
print('math.trunc(.5) : ', trunc(.5))  # 0
print('math.fmod(10, 2) : ', fmod(10, 2))  # 10 % 2 -> 0.0  float
print('math.frexp(16) : ', frexp(16))  #  (0.5, 5)  means 16 = 0.5 * 2 ** 5
##frexp(x, /)
##    Return the mantissa and exponent of x, as pair (m, e).
##    
##    m is a float and e is an int, such that x = m * 2.**e.
##    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0
##
print(' math.nan : ', nan)
print('math.nan + 5 : ',  nan + 5)
## NaN is often used to represent the result of operations that
## don't produce a meaningful numerical result, such as the square
## root of a negative number or the division of zero by zero.
##
## Checking for NaN is important in situations where invalid or unexpected
## results might occur in floating-point computations.

nan_value = nan
is_nan = isnan(nan_value)

print(nan_value)  # Output: nan
print(is_nan)     # Output: True

##  Keep in mind that comparisons with NaN using standard equality
##  operators (==, !=, etc.) always evaluate to False.
##  Instead, use math.isnan() for NaN-specific checks.


# Example 1: Using isqrt with a non-negative integer
print('isqrt(16) : ', isqrt(16) ) # integer square root 4 => int
print('sqrt(16) :', sqrt(16))  # 4.0 -> float

# Example 2: Using isqrt with a large non-negative integer
number2 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print('isqrt(large number) : ', isqrt(number2))
#print('sqrt(large number) : ', sqrt(number2))  ## OverFlowError: int too large to convert to a float

## The isqrt function in Python's math module is designed specifically for computing
## the integer square root of a non-negative integer, and it is generally safer to
## use than sqrt for large integers.
##
## The sqrt function returns a floating-point result, and for very large integers, the
## floating-point representation may lose precision or encounter overflow issues,
## leading to errors.
##
## On the other hand, isqrt returns an integer result, making it more suitable for
## scenarios where you want the integer square root of a large non-negative
## integer without dealing with potential precision issues associated with floating-point
## arithmetic.

######## RANDOM

# Generate a random integer between 0 and 9 (exclusive)
from random import randrange
random_number = randrange(10)
print(random_number)

# Generate a random integer between 1 and 100 (inclusive)
from random import randint
random_number = randint(1, 100)
print(random_number)

# Generate a random floating-point number between 0 and 1
from random import random
random_float = random()
print(random_float)


# Shuffle a list in-place
from random import shuffle
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)

# Choose a random element from a sequence
from random import choice
my_list = ["apple", "banana", "orange", "grape"]
random_fruit = choice(my_list)
print(random_fruit)


# Sample k unique elements from a sequence
from random import sample
my_list = ["a", "b", "c", "d", "e"]
random_sample = sample(my_list, 3)
print(random_sample)


######### DATETIME

# Get the current date and time
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)  # datetime.now() retrieves the current date and time.


# Format the current date and time as a string
from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime) #strftime(format) formats a datetime object as a string using a specified format.


# Get the day of the week (Monday is 0, Sunday is 6) for the current date
from datetime import datetime
current_datetime = datetime.now()
day_of_week = current_datetime.weekday()
print(day_of_week)  # weekday() returns the day of the week as an integer (Monday is 0, Sunday is 6) for a given datetime object.



