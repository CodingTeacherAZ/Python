''' 3. Input and Output Operations 
3.2 Construct and analyze code segments that perform console input
and output operations 
• print formatted text (string.format() method, f-String method)
'''
#### Concatenation and Comma Operator
a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)
print(a, b)

########  f-strings #########  
# formated string literal method
# introduced in Python 3.6 -- newer and most preferred method
# pattern:  f"{expression:format_specificaations}

name = "Alice"
age = 30
f_string = f"My name is {name} and I am {age} years old."
print(f_string)   # faster and more flexible than string concatenation
                  # could be excellent for loops

# place holders can contain Python code like math operations
x = 5
y = 10
result = f"The sum of {x} and {y} is {x + y}."
print(result)

# expression can access other objects
person = {"name": "Bob", "age": 25}
info = f"Name: {person['name']}, Age next year: {person['age'] + 1}"
print(info)

# using a multiline f-string
multiline_string = f"""
This is a
multiline
f-string.
"""
print(multiline_string)

# using format-specifications
name = 'Food'
amount = 12.5

    # Fill
print(f"|{name:-^10}|")         # |---Food---|      # Custom fill character
print(f"|{name:*<10}|")         # |Food******|      # Custom fill character
print(f"{42:05d}")              # 00042             # Pad with zeros

    # Alignment
print(f"|{name:<10}|")          # |Food      |      # Left-align with width 10 wide
print(f"|{amount:>10.2f}|")     # |     12.50|      # Rignt-align with width 10 with 2 decimal places
print(f"|{name[:3]:^10}|")      # |   Foo    |      # Center shown with string slicing

    # Sign
print(f"{amount:+}")            # +12.5             # Always show sign

    # Width
print(f"|{amount:10}|")         # |      12.5|      # At least 10 wide

    # Grouping
print(f"{1234567:,}")           # 1,234,567         # Thousands separator

    # Precision
print(f"{amount:.2f}")          # 12.50             # float data type = decimal places
print(f"{'Hello':.3s}")         # Hel               # string data type = characters

    # Type
print(f"{42:f}")                # 42.000000         # Fixed-point number - does NOT do type conversion 
print(f"{42:d}")                # 42                # Decimal integer - does NOT do type conversion
print(f"{0.875:.1%}")           # 87.5%             # Percentage
print(f"{1234:.2e}")            # 1.23e+03          # Scientific Notation
print(f"{13:b}")                # 1101              # Binary integer
print(f"{188:x}")               # bc                # Hexadecimal integer
print(f"{name:s}")              # Food              # string - does NOT do type conversion



# combining format specifications- can use ONE of each type
# ORDER matters:  fill → alignment → width → grouping → precision → type
print(f"{42:*^10,.2f}")           # **42.00***
print(f"|{name:^10.3s}|") 

# For more complex formatting, use f-string to create the string
# then apply a string method
print(f"{42:08.2f}".center(10, "*"))    # *00042.00*




###### format() method #######
# Example with string.format() method
formatted_string_format = "Hello, {}! You are {} years old.".format(user_name, user_age)
print(formatted_string_format)

number = 123.456789
formatted_string_format = "The number is {:.2f}".format(number)
print(formatted_string_format)

# Example with f-string method (available in Python 3.6 and later)
formatted_f_string = f"Hello, {user_name}! You are {user_age} years old."
print(formatted_f_string)

number = 123.456789
formatted_f_string = f"The number is {number:.2f}"
print(formatted_f_string)


def format_money(amount):
    return '${:,.2f}'.format(amount)

S = '{0} is derived from the {1} {2}'
print(S.format('none', 'no', 'one'))
print(S.format('Etymology', 'Greek', 'Ethos'))
print(S.format("December", "Latin", "decem"))

from math import pi
print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2, pi))
for i in range(1, 10, 2):
    print('Pi rounded to {0} decimal places is {1:.{0}f}.'.format(i, pi))

# as long as the order doesn't change!
print('Pi rounded to {:.2f} decimal places is {:.2f}.'.format(2, pi))



####### % string formatting  ########

