'''
1. Operations using Data Types and Operators 
1.1 Evaluate expressions to identify the data types Python assigns to variables 
• str, int, float, and bool 

1.2 Perform and analyze data and data type operations 
• Data type conversion,

1.3 Determine the sequence of execution based on operator precedence 
• Assignment (=, +=, -=, /=, %=, //=, **=), comparison (==, >=, <=, !=), logical  
(and, or, not), logical, arithmetic (+, -, /, //, %, **, unary + and -), identity (is),  
containment (in) 

1.4 Select operators to achieve the intended results 
• Assignment (=, +=, -=, /=, %=, //=, **=), comparison (==, >=, <=, !=), logical  
(and, or, not), logical, arithmetic (+, -, /, //, %, **, unary + and -), identity (is),  
containment (in) 

'''
######   Global and Local Variables #########
## global variables are available to functions
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

##If you create a variable with the same name inside a function,
# this variable will be local, and can only be used inside the function.
# It will have higher precedence inside the function.
# The global variable with the same name will remain as it was,
# global and with the original value.
# notice the function has to be called
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # Python is fantastic

myfunc()

print("Python is " + x) #Python is awesome


#If you use the global keyword, the variable belongs to the global
# scope:
# this is considered poor form
# it's better to create global variables on the global scope
# and pass them by reference into functions
# notice the function has to be called
def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)

# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:
# notice the function has to be called
x = "awesome"

def myfunc3():
  global x
  x = "fantastic"

myfunc3()

print("Python is " + x)
### ----------------------------------
### FLOAT ####
#Floats are  positive, negative, or zero containing a decimal or
# scientific numbers with an "e" to indicate the power of 10.
x = 0.0
y = 1.1
z = -35.59
x = 35e3
y = 12E4
z = -87.7e100

### ----------------------------------
### Complex ####
# you cannot convert complex into another number type
x = 3+5j
y = 5j
z = -5j


## swapping
s1 = 'first'
s2 = 'second'
s1, s2 = s2, s1
print(s1)   # 'second'
print(s2)   # 'first'

## boolean in order of precedence: not, and, or
print(not True)
print('True and True:', True and True)  # True
print("True and False:", True and False)
print("False and False:", False and False) # False
print("False and True", False and True)
print("not(True and True):",not(True and True)) # False
print("not True and True:", not True and True) #False


# 'You can have pizza or chicken'
# English is exclusive or (one or the other but not both)
# Python interprets or as inclusive.
# inclusive or allows both and either
print("True or True:", True or True) # True (both)
print("True or False:", True or False) # True (either)
print("False or False:", False or False) # False (neither)

#  Build Exclusive or  (XOR)
# want True only if exactly one of them is True
pizza = False
chicken = False
print("I want neither of pizza or chicken: ", end='')
print((pizza and not chicken) or (chicken and not pizza)) # False

pizza = False
chicken = True
print("I want pizza or chicken (exclusive or): ", end='')
print((pizza and not chicken) or (chicken and not pizza)) # True

pizza = True
chicken = False
print("I want pizza or chicken (exclusive or): ", end="")
print((pizza and not chicken) or (chicken and not pizza)) # True

pizza = True
chicken = True
print("I want pizza and chicken (inclusive or): ", end="")
print((pizza and not chicken) or (chicken and not pizza)) # False

## DeMorgan's Laws
P = True
Q = False

print(not (P and Q), "==", not P or not Q)
print(not (P or Q), "==", not P and not Q)

## Data types and Booleans
print("1 : ", bool(1))  #True  #All numbers not zero are True
print("5 : ", bool(5))  #True
print("-6 : ", bool(-6)) #True
print("0 : ", bool(0))  #False  # zero is false
print('not 1 : ', not 1)  #False
print('not 0 : ', not 0) # true 
print("True : ", int(True))   # 1  # True casts to 1
print("False : ", int(False))  # 0   # False casts to 0
print("6.3 : ", bool(6.3))  # True  # all numbers not zero are True
print("0.0 : ",bool(0.0))   # zero is False

print("s : ", bool("s")) # a non-empty string is True
print(" : ", bool(""))   # empty string is False
print("not '' :", not '')  # True
print("not 'bad' : ", not 'bad')  # False

## booleans and arithmetic operations:
print("True * 5 : ", True * 5)  # 5
print("False * 5 : ", False * 5)  # 0
print("True + 5 : ", True + 5)    #  6
print("False + 5 : ", False + 5)   # 5
print("True - 5 : ", True - 5)    # Output: -4
print("False - 5 : ", False - 5)   # Output: -5
print("True / 2 : ", True / 2)    # Output: 0.5

## Comparing Strings
print(" 'A' < 'a' : ", 'A' < 'a')
print("A : ", ord("A"), " and 'a' : ", ord('a'))
print("Check if 'Jan' is in '01 Jan 1838' : ", 'Jan' in '01 Jan 1838')
print("Check if '83' is in '01 Jan 1838 : ", '83' in "01 Jan1838")
print("Check if empty string in 'abc' : ", '' in 'abc')  ##empty string is always a subset of all strings

## PRECEDENCE
##  In Python, operators have different precedence levels, which determine
## the order of evaluation when multiple operators are used in the same
## expression. Here's a general overview of the operator precedence in Python
## from highest to lowest:
##
## Exponentiation: **
## Unary plus and minus: +x, -x
## Multiplication, Division, Floor Division, Modulus: *, /, //, %
## Addition and Subtraction: +, -
## Bitwise Shifts: <<, >>
## Bitwise AND: &
## Bitwise XOR: ^
## Bitwise OR: |
## Comparison Operators: ==, !=, >, <, >=, <=, in, is, not in, is not
## Logical NOT: not
## Logical AND: and
## Logical OR: or
## Assignment Operators: =, +=, -=, /=, //=, %=, **=
##

a = -5
b = -3

# Example with Unary Plus, Logical AND, and Arithmetic Operations
result = +a * b ** 2 >= 0 and a + b > 0
# order: exponentiation, unary, multiplication, comparison -> bool
# order: addition, comparison -> bool
# logical AND
print(result)


### BItWISE
## Left Shift (<<):
##
## The left shift operator (<<) shifts the bits of a binary number
## to the left by a specified number of positions.
## Each shift to the left is equivalent to multiplying the number by
## 2 raised to the power of the shift amount.
## For each shift to the left, a zero is introduced on the right side.
x = 5
result = x << 2  # Shift the binary representation of 5 two positions to the left
print(result)    # Output: 20 (5 * 2^2)

## Right Shift (>>):
##
## The right shift operator (>>) shifts the bits of a binary number to the right
## by a specified number of positions.
## Each shift to the right is equivalent to dividing the number by 2 raised
## to the power of the shift amount (with rounding towards negative infinity).

y = 16
result = y >> 2  # Shift the binary representation of 16 two positions to the right
print(result)    # Output: 4 (16 / 2^2)


### efficient multiplication or division by powers of 2
x = 10
result = x << 2  # Equivalent to x * 2^2
print(result)    # Output: 40

### creating or extracting bit fields
flags = 0b10101100
# Extracting the third and fourth bits
extracted_bits = (flags >> 2) & 0b11
print(bin(extracted_bits))  # Output: 0b10

#### encoding or decoding
# Packing two values into a single byte
value1 = 3
value2 = 5
packed_byte = (value1 << 4) | value2
print(bin(packed_byte))  # Output: 0b00110101

### bitwise operations
# Checking if the third bit is set
number = 0b100
is_third_bit_set = (number >> 2) & 1
print(is_third_bit_set)  # Output: 1 (True)

### memory allocation and masking
# Using a bitmask to check if a specific flag is set
flags = 0b11001010
flag_to_check = 0b00100000
is_flag_set = (flags & flag_to_check) != 0
print(is_flag_set)  # Output: True


# For each shift to the right, zeros are introduced on the left side.

### bitwise and &
a = 0b1100
b = 0b1010
result = a & b  #The result bit is 1 only if both input bits are 1.
print(bin(result))  # Output: 0b1000

## bitwise or |
a = 0b1100
b = 0b1010
result = a | b  #The result bit is 1 if at least one of the input bits is 1.
print(bin(result))  # Output: 0b1110

## bitwise xor  ^
a = 0b1100
b = 0b1010
result = a ^ b  # The result bit is 1 if the input bits are different.
print(bin(result))  # Output: 0b0110

