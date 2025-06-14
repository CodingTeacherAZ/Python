"""
4. Code Documentation and Structure
    4.1 Document code segments
            Use indentation, white space, comments, and docstrings;
            generate documentation by using pydoc
    4.2 Construct and analyze code segments that include function definitions
            Call signatures, default values, return, def, pass

"""

##  SIGNATURE, DEF, RETURN
## header, body, variable scope
##
## def add_numbers(x: int, y: int) -> int:
## the function signature includes the entire line that
## starts with the def keyword and declares the function
## name, parameters, and return type (if any).
##
## def add_numbers(x, y):
## The function header is a subset of the function signature
## and may not include the additional information.
##
## After the function signature is the function body where
## a block of code is executed. Keyword return may or may
## not be used.
##
## variables that are created within the function and the function
## parameters are called local variables. They are created and erased
## each time the function is called.  They exist only within the function
## and cannot be called or accessed from outside the function
##
## The area of a program that a variable can be accessed is called the
## variable's scope.  The scope of a local variable is from the line it
## is defined until the end of the function.

def f(x):         # local
    x = 2 * x    # local
    #print("local x", x)
    return x     # local

x = 1            #global
x = f(x + 1) + f(x + 2)   #global
#print("global x", x)

## When Python executes a function call it creates a namespace to
## store the local variables where it keeps track of them as long as
## the function is being executed, then destroys the namespace.
##
## Python creates a namespace for variables created in the shell and
## a different namespace for variables created in .py
##
## The parameter of f is in a different namespace than the variable
## assignment in the program.

## DOCSTRINGS
## the docstring is a description of what the function does,
## describe the parameters,the expected return, and  may include
## examples of function calls with correct returns

def example_function(parameter1, parameter2):
    """
    Short description of the function.

    More detailed description if necessary.

    Parameters:
    - parameter1 (type): Description of parameter1.
    - parameter2 (type): Description of parameter2.

    Returns:
    type: Description of the return value.

    Raises:
    - SpecificError: Description of when this error might occur.
    """
    # Function implementation goes here
    return result


def multiply_numbers(x, y):
    """
    Multiplies two numbers.

    Parameters:
    - x (float): The first number.
    - y (float): The second number.

    Returns:
    float: The product of x and y.

    Examples:
    >>> multiply_numbers(3, 4)
    12.0
    >>> multiply_numbers(0.5, 2)
    1.0
    >>> multiply_numbers(-1, 5)
    -5.0
    """
    return x * y


## CREATING FUNCTIONS
##     1. Start with the function call and expected results
##     2. Write the header/signature and decide on parameter names & types
##     3. Write the docstring
##     4. Write the body
##     5. Test your function using the example calls

def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing.
    >>> above_freezing_v2(5.2)
    True
    >>> above_freezing_v2(-2)
    False
    """
    return celsius > 0

from typing import List
def running_sum(L: List[float]) -> None:
    """Modify L so that it contains the running sums of its original items.
    >>> L = [4, 0, 2, -5, 0]
    >>> running_sum(L)
    >>> L
    [4, 4, 6, 1, 1]
    """
    for i in range(1,len(L)):
        L[i] = L[i - 1] + L[i]


def days_difference(day1: int, day2: int) -> int:
    """ Return the number of days between day1 and day2, which are
    both in the range 1-365 (thus indicating the day of the year).

    Examples:
    days_difference(200, 224) -> 24
    days_difference(50, 50) -> 0
    days_difference(100, 99) -> -1
    """
    return day2 - day1

def get_weekday(current_weekeday: int, days_ahead: int) -> int:
    """ Return which day of the week it will be days_ahed days from the
    current_weekday.

    current_weekday is the current day of the week and in the range 1 - 7,
    indicating today is Sunday(1) ... Saturday(7)

    days_ahead is the number of days after today

    Examples:
    get_weekday(3, 1) -> 4
    get_weekday(7, 1) -> 1
    get_weekday(4, 7) -> 4
    get_weekday(7, 22) -> 2
    """
    return (current_weekday + days_ahead - 1) % 7

def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int) -> int:
    """ Return the day of the week it will be on birthday_day,
    given that the day of the week is the current_weekday and the
    day of the year is the current_day.

    current_weekday is the current day of the week and is in the range 1 - 7,
    indicating whether today is Sunday(1)...Saturnday(7)

    current_day and birthday_day are both in the range of 1 - 365

    Examples:
    get_birthday_weekday(5, 3, 4) -> 6
    get_birthday_weekday(5, 3, 116) -> 6
    get_birhtday_weekday(6, 116, 3) -> 5
    """
    days_diff = days_difference(current_day, birthay_day)
    return get_weekday(current_weekday, days_diff)

def weeks_elapsed(day1: int, day2: int) -> int:
    """ day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.

    Examples:
    weeks_elapsed(3, 20) -> 2
    weeks_elapsed(20, 3) -> 2
    weeks_elapsed(8, 5) -> 0
    weeks_elapsed(40, 61) -> 3
    """
    return abs(day2 - day1) // 7 

## PASS
## In Python, the pass statement is a null operation that does nothing when
## it is executed. It is often used as a placeholder in situations where
## syntactically some code is required but no action is desired or necessary.
## One common use case for pass is in the definition of functions or classes
## where the body is intentionally left empty.
def my_function():
    # TODO: Implement the logic for this function later
    pass


class MyClass:
    # TODO: Build this class later
    pass

if True:
    # Code to be added later
    pass


###  DEFAULT VALUES

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Calling the function without providing a value for 'greeting'
greet("Alice")  # Output: Hello, Alice!

# Calling the function and providing a value for 'greeting'
greet("Bob", "Hi")  # Output: Hi, Bob!


## Default values must be immutable:
## Default values are evaluated only once when the function is defined.
## If the default value is a mutable object (e.g., a list or dictionary),
## modifications made to the object will persist across function calls.
## This behavior is often not what you want. Use immutable objects
## (e.g., None, integers, strings) as default values.

## Mutable objects can be used as regular function parameters without
## causing the same issues as mutable default values. The key consideration
## is whether the function modifies the mutable object in a way that leads
## to unexpected behavior or side effects.

##  PYDOC
##
## 1. Add Docstrings to Your Code:
## 2. Generate Documentation Using pydoc from the Terminal:
##
##     Open your terminal and navigate to the directory containing your Python file.
##     cd /path/to/your/directory
##
##  3. Run pydoc followed by the name of your Python file (excluding
##   the ".py" extension).
##
##    pydoc your_file_name
##
##    This will display the documentation in the terminal.
##
##  4. Generate HTML Documentation:
##
##    You can generate HTML documentation for your module using
##    the -w option with pydoc. This will create an HTML file with the documentation.
##
##    pydoc -w your_file_name
##
##   This will create a file named your_file_name.html (or my_module.html in the example).
##
## 5. Open the HTML Documentation:
##    Open the generated HTML file in a web browser to view the documentation
##    in a more structured and visually appealing format.
##
##    That's it! By adding docstrings to your code and using pydoc, you can easily
##    generate and view documentation for your Python modules and functions.
##    Remember to replace "your_file_name" with the actual name of your Python
##    file or module. If you have multiple modules, you can specify them as a
##    comma-separated list.


####  functions for unittesting
def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the preceding item, and replace the first item with 0.
        >>> L = [1, 2, 3]
        >>> double_preceding(L)
        >>> L
        [0, 2, 4]
        """
    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
                temp2 = values[i]
                values[i] = 2 * temp
                temp = temp2


def validate_line(line):
    """Validate a line represented as a list of two tuples."""
    return len(line) == 2 and all(
        isinstance(element, tuple) and len(element) == 2 and all(isinstance(num, (int, float)) for num in element)
        for element in line
    )

def find_intersection(x, y) -> str:
    """Find the intersection of two lines."""
    x_is_valid = isinstance(x, (int, float))
    y_is_valid = isinstance(y, (int, float))
    x_list_is_valid = validate_line(x)
    y_list_is_valid = validate_line(y)

    if not (x_is_valid or x_list_is_valid) or not (y_is_valid or y_list_is_valid):
        return "Unusable data was sent: ({}, {})".format(x, y)

    if x_is_valid and y_is_valid:
        solution = (x, y)
    elif x_is_valid and y_list_is_valid:
        x2s, y2s = y[0]
        x2e, y2e = y[1]
        y2 = round((y2e - y2s) / (x2e - x2s) * (x - x2s) + y2s, 2)
        solution = (round(x, 2), y2)
    elif x_list_is_valid and y_is_valid:
        x1s, y1s = x[0]
        x1e, y1e = x[1]
        xsol = round((y - y1s) * (x1e - x1s) / (y1e - y1s) - x1s, 2)
        solution = (xsol, round(y, 2))
    elif x_list_is_valid and y_list_is_valid:
        x1s, y1s = x[0]
        x1e, y1e = x[1]
        x2s, y2s = y[0]
        x2e, y2e = y[1]

        denominator = (y1e - y1s) * (x2e - x2s) - (y2e - y2s) * (x1e - x1s)
        if denominator == 0:
            return 'The lines are parallel' if y1e - y1s != 0 else 'The lines are coincident'

        numerator = (y1e - y1s) * (x2e - x2s) * x1s - (y2e - y2s) * (x1e - x1s) * x2s + (y2s - y1s) * (
                    x1e - x1s) * (x2e - x2s)
        xsol = round(numerator / denominator, 2)
        y1 = round((y1e - y1s) / (x1e - x1s) * (xsol - x1s) + y1s, 2)
        solution = (xsol, y1)

        if y1 != round((y2e - y2s) / (x2e - x2s) * (xsol - x2s) + y2s, 2):
            return "The y values don't match"

    return "The lines intersect at point {}".format(solution)


def all_prefixes(s: str) -> set:
        """ takes a string as its inputand returns the set of all nonempty substrings
        that start with the first character.
        Example:
        all_prefixes("lead")  ->  {"l", "le", "lea", "lead"}."""

        valid_input = isinstance(s, str)
        prefix = ''
        prefix_set = set()
        if valid_input: 
            for char in s:
                if char == " ":
                    continue
                prefix += char
                prefix_set.add(prefix)
            return prefix_set
        else:
            return set()
           
'''
In general, if the invalid input represents an exceptional case (i.e., it's an error that
shouldn't normally occur during correct usage), raising a ValueError is often
considered a better practice. This approach ensures that the calling code is aware
of the problem and can handle it appropriately. It also makes debugging and fixing
issues easier because the specific error message provides more information.

If invalid input is something that might be expected during normal operation and
doesn't necessarily indicate a critical failure, returning False might be a more lenient
approach, allowing the program to continue execution with a default or fallback value.
'''

def is_sorted(L: list) -> bool:
    """takes a list of integers as input and returns True if they are sorted
    in nondecreasing order (as opposed to strictly increasing order, because
    of the possibility of duplicate values), and False otherwise."""

    valid_input = isinstance(L, list) and all(isinstance(num, (int, float)) for num in L)

    if not valid_input:
        raise ValueError("Input must be a list of integers")

    else:
        for i in range(len(L) - 1):
            if L[i +1] < L[i]:
                return False
        else:
            return True

L = []
result = is_sorted(L)
print(result)
        

        

