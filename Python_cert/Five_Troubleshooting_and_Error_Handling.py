'''
5. Troubleshooting and Error Handling 
5.1 Analyze, detect, and fix code segments that have errors 
• Syntax errors, logic errors, runtime errors 

5.2 Analyze and construct code segments that handle exceptions 
• try, except, else, finally, raise 
5.3 Perform unit testing 
• Unittest, functions, methods, and assert methods (assertIsInstance,  
assertEqual, assertTrue, assertIs, assertIn) 
'''
### try, except Blocks:
#The try block is used to enclose the code that might raise an exception.
#The except block is executed if an exception occurs in the try block.


'''try:
    # Code that might raise an exception
except <ExceptionType>:
    # Code to handle the exception
'''
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero.")

## Handling Multiple Exceptions:
#You can handle multiple exceptions by specifying multiple except blocks
# or using a tuple of exception types.


'''try:
    # Code that might raise an exception
except (TypeError, ValueError):
    # Code to handle TypeError or ValueError
else Block:
'''
#The else block is executed if no exception occurs in the try block.

### Finally
'''try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful:", result)
finally Block:'''

# The finally block is __always__ executed, whether an exception occurs or not.
# It is typically used for cleanup operations, such as closing files or releasing resources.



### Raise
'''try:
    # Code that might raise an exception
except <ExceptionType>:
    # Code to handle the exception
finally:
    # Code that always runs, regardless of whether an exception occurred
raise Statement:
'''
# The raise statement is used to raise a specific exception manually.

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print("Error:", e)


##  Handling All Exceptions:
# You can use a generic except block to catch any exception.
# However, this is generally discouraged as it may hide bugs or unexpected issues.


'''try:
    # Code that might raise an exception
except Exception as e:
    # Code to handle any exception
'''

# Custom Exceptions:
# You can create your own custom exception classes by inheriting from the
# built-in Exception class or its subclasses.

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception.")
except CustomError as ce:
    print("Caught custom exception:", ce)








## Imports
import  unittest
import Four_code_documentation_and_structure as functions


#####    Notes    #####
##   quality isn’t some kind of magic pixie dust that
##   you can sprinkle on a program after it has been written

# Boundary cases are much more likely to contain bugs

## first test: Function calls
## second test: use doctest on the docstring examples

## unittest tests one isolated component of a program
## contrast to system test whch tests the behavior of the entire program as a whole

## pros: 
## for large test suites, its nice to have the testing code in a separate file
## Each test case can be in a separate method making the tests independent from each other
## Each method has its own doctstring to make clear how the test cases differ
## customizable error messages

## Test can show the absence of bugs but they can't show that a program is fully correct

###  Test Cases
#  Size: Test empty, one item, general collection, smallest interesting case
#  Dichotomies: empty/full, even/odd, positive/negative, alphabetic/nonalphabetic
#  Boundaries: above, below, and on
#  Order: does the function behave differently if the collection is ordered or not?


###  Debugging
# Work backwards from the incorrect behavior, come up with a solution, test the solution
# 1. Make sure you know what the program is supposed to do
# 2. Repeat the failure:  Find a test case that makes the program fail reliably. Once you have the test case, design a simpler one
# 3. Divide and conquer: Once you have a test case that makes the program fail, find the first moment and examine the code from there
# 4. Change ONE thing at a time and for a reason. After each change, rerun the test cases
# 5. Keep records: a notebook, a version history, a file open in the editor

#####    Testing above_freezing   #####
class TestAboveFreezing(unittest.TestCase):
    ''' Tests for functions.above_freezing '''
    def test_above_freezing_above(self):
        """Test a temperature that is above freezing"""
        expected = True
        actual = functions.above_freezing(5.2)
        self.assertEqual(expected, actual, "Error: The temperature is above freezing.")

    def test_above_freezing_below(self):
        """ Test a temperature that is below freezing """
        expected = False
        actual = functions.above_freezing(-2)
        self.assertEqual(expected, actual, "Error: The temperature is below freezing.")

    def test_above_freezing_at_zero(self):
        """ Test a temperature that is at freezing """
        expected = False
        actual = functions.above_freezing(0)
        self.assertEqual(expected, actual, "Error: The temperature is at the freezing mark.")

# unittest.main()

#####    Testing running_sum    #####
# determine the test cases and before-after results, then implement using unittest
'''
Test Case Description       List Before         List After
Empty list                      []                       []
One-item list                   [5]                     [5]   
Two-item list                   [2, 5]                  [2. 7]
Multiple items, all negative   [-1, -5, -3, -4]          [-1. -6, -9, -13]
Multiple items, all zero       [0, 0, 0, 0]             [0, 0, 0, 0]
Multiple items, all positive   [4, 2, 3, 6]             [4, 6, 9, 15]
Multiple items, mixed         [4, 0, 2, -5, 0]         [4, 4, 6, 1, 1]
'''
class TestRunningSum(unittest.TestCase):
    """Tests for functions.running_sum """
    def test_running_sum_empty(self):
        """ Test an empty list """
        argument = []
        expected = []
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list is empty")

    def test_running_sum_one_item(self):
        """ Test a one-item list """
        argument = [5]
        expected = [5]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one value")

    def test_running_sum_two_items(self):
        """" Test a two-item list """
        argument = [2, 5]
        expected = [2, 7]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two values")

    def test_running_sum_multi_negative(self):
        """ Test a list of negative values """
        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains negative values")

    def test_running_sum_multi_zero(self):
        """Test a list of all zeros """
        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains zeros")

    def test_running_sum_multi_positive(self):
        """ Test a list of all positive values """
        argument =  [4, 2, 3, 6]
        expected = [4, 6, 9, 15]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains positive values")

    def test_running_sum_multi_mixed(self):
        """ Test a list of mixed values """
        argument = [4, 0, 2, -5, 0]
        expected = [4, 4, 6, 1, 1]
        functions.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains mixed values")

#unittest.main()

#####    Testing double_preceding   ######
'''
Test Case Description       List Before         List After
Empty list                      []                       []
One-item list                   [5]                     [0]   
Two-item list                   [2, 5]                  [0. 4]
Multiple items, all negative   [-1, -5, -3, -4]          [0. -2, -10, -6]
Multiple items, all zero       [0, 0, 0, 0]             [0, 0, 0, 0]
Multiple items, all positive   [4, 2, 3, 6]             [0, 8, 4, 6]
Multiple items, mixed         [4, 0, 2, -5, 0]         [0, 8, 0, 4, -10]
Float items                    [1.1, 3.2, -2.4, 6.3]     [0, 2.2, 6.4, -4.8]
'''
class TestDoublePreceding(unittest.TestCase):
    """Tests for functions.double_preceding """
    def test_double_preceding_empty(self):
        """ Test an empty list """
        argument = []
        expected = []
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list is empty")

    def test_double_preceding_one_item(self):
        """ Test a one-item list """
        argument = [5]
        expected = [0]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains one value")

    def test_double_preceding_two_items(self):
        """" Test a two-item list """
        argument = [2, 5]
        expected = [0, 4]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains two values")

    def test_double_preceding_multi_negative(self):
        """ Test a list of negative values """
        argument = [-1, -5, -3, -4]
        expected = [0, -2, -10, -6]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains negative values")

    def test_double_preceding_multi_zero(self):
        """Test a list of all zeros """
        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains zeros")

    def test_double_preceding_multi_positive(self):
        """ Test a list of all positive values """
        argument =  [4, 2, 3, 6]
        expected = [0, 8, 4, 6]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains positive values")

    def test_double_preceding_multi_mixed(self):
        """ Test a list of mixed values """
        argument = [4, 0, 2, -5, 0]
        expected = [0, 8, 0, 4, -10]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains mixed values")
      
    def test_double_preceding_float(self):
        """ Test a list of float values """
        argument = [1.1, 3.2, -2.4, 6.3]
        expected = [0, 2.2, 6.4, -4.8 ]
        functions.double_preceding(argument)
        self.assertEqual(expected, argument, "The list contains mixed floats")


class TestFindIntersection(unittest.TestCase):
    """ Tests functions.find_intersection
    """
    def test_intersecting_lines(self):
        """ Test 1: Lines with different slopes must intersect at a Point """
        L1 = [(1, 5), (2, 7)]
        L2 = [(3, -5), (5, -11)]
        expected = "The lines intersect at point (0.2, 3.4)"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The lines intersect. The function should handle this case appropriately")

    def test_parallel_lines(self):
        ''' Test 2: No solution: Parallel Lines cause 0/0 division '''
        L1 = [(0,3), (1,5)]
        L2 = [(0, 5), (1,7)]
        expected =  'The lines are parallel'
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The lines are parallel. The function should handle this case appropriately")

    def coincident_lines(self):
        """ Test 3: Infinite solutions: Coincident Lines cause 0/# division """
        # same point
        L1 = [(1,5), (2,7)]
        L2 = [(1,5), (2,7)]
        expected = "The lines are coincident"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The lines are coincident. The function should handle this case appropriately")

        # different points
        L1 = [(-1.5, 0), (1.5, 6)]
        L2 = [(4,11), (6,15)]
        expected = "The lines are coincident"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The lines are coincident. The function should handle this case appropriately")

    def vert_hor_lines(self):
        """ Test 4: User sends equations for Vertical and Horizontal Lines """
        # both lines
        expected = 'The lines intersect at point (3, 5)'
        result = functions.find_intersection(x=3, y=5)
        self.assertEqual(expected, result, "Both lines are horizontal and vertical.  The function should handle this case appropriately")

        # y line
        L1 = [(1, -1), (2, -2)]
        L2 = 7 
        expected = 'The lines intersect at point (-9.0, 7)'
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "One line is vertical. The function should handle this case appropriately.")

        # x line
        L1 = 2
        L2 = [(1, -1), (2, -2)]
        expected = "The lines intersect at point (2, -2.0)"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "One line is horizontal. The function should handle this case appropriately.")

                        
        
    def rounded_values(self):
        """ Test 5: Differences in precision due to division by some numbers such as 3, 6, and 9 """
        L1 =[(1, 1), (2, 3)]
        L2 = [(1, -1), (2, -2)]
        expected = "The lines intersect at point (0.333, -0.33)"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The lines intersect.  The function should handle precision and rounding appropriately")

    def bad_data(self):
        """ Test 6: strings or some other unusable data was sent """
        # Invalid: strings
        L1 = "a"
        L2 = "$"
        expected = "Unusable data was sent: ('a', '$')"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should hanlde bad input appropriately")

        # Invalid: Points with non-numeric values
        L1 = [("a", 5), (2, 7)]
        L2 = [(3, -5), ("b", -11)]
        expected = "Unusable data was sent: ([('a', 5), (2, 7)], [(3, -5), ('b', -11)])"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")
        
        # Invalid: Points with missing coordinates
        L1 = [(1, 5), (2,)]  # Missing the y-coordinate for the second point
        L2 = [(3, -5), (5, -11, 2)]  # Extra coordinate for the second point
        expected = "Unusable data was sent: ([(1, 5), (2,)], [(3, -5), (5, -11, 2)])"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")

        L1 = [(1, ), (2, 5)]  # Missing the x- coordinate for the second point
        L2 = [(3, -5, 2), (5, -11)]  # Extra coordinate for the first point
        expected = "Unusable data was sent: ([(1, 5), (2,)], [(3, -5), (5, -11, 2)])"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")

        # Invalid: Incorrect format for points
        L1 = [1, 5, 2, 7]  # Points should be tuples
        L2 = "3, -5, 5, -11"  # Points should be in a list, not a string
        expected = "Unusable data was sent: ([1, 5, 2, 7], '3, -5, 5, -11')"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")
        
        # Invalid: Points with invalid data types
        L1 = [("1", 5), (2, 7)]  # String instead of an integer
        L2 = [(3, -5), (5.5, -11)]  # Float instead of an integer
        expected = "Unusable data was sent: ([('1', 5), (2, 7)], [(3, -5), (5.5, -11)])"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")

        L1 = {(1, 4), (7, 8)} # String instead of an integer
        L2 = ((3, -5), (5.5, -11)) # Float instead of an integer
        expected = "Unusable data was sent: ([('1', 5), (2, 7)], [(3, -5), (5.5, -11)])"
        result = functions.find_intersection(L1, L2)
        self.assertEqual(expected, result, "The function should handle bad input appropriately")



class TestAllPrefixes(unittest.TestCase):
    """ Tests functions.all_prefixes """
    def empty_string(self):
        '''This tests how the function handles an empty input.'''
        s = ""
        expected = set()
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should handle an empty string.")

    def single_char(self):
        '''This tests whether the function correctly handles a single character input.'''
        s = "a"
        expected = {"a"} # a set containing the single character
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process a single character string.")

    def general_cases(self):
        '''This is similar to the example given in the docstring.'''
        s =  "lead" 
        expected = {"l", "le", "lea", "lead"}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process a string with no spaces,")

        s = "tiny cats"
        expected = {'tinycat', 'tinycats', 'tinyca', 'tin', 't', 'tiny', 'tinyc', 'ti'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process a string containing spaces.")

    def numeric_string(s):
        """This tests whether the function works with numeric strings."""
        s = '1234'
        expected = {'12', '1', '1234', '123'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process numeric strings.")

    def special_chars(s):
        '''This tests whether the function correctly handles strings with special characters.'''
        s = "!@#$"
        expected = {'!@#$', '!', '!@', '!@#'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process special characters.")

    def mixed_chars(self):
        """This tests whether the function works with a mix of alphabetic and numeric characters"""
        s = "abc123"
        expected = {'abc', 'abc12', 'a', 'ab', 'abc1', 'abc123'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process mixed characters.")

        s = "123abc"
        expected = {'123abc', '1', '123ab', '123', '123a', '12'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process mixed characters.")

    def mixed_case(self):
        s = "Lead"
        expected = {"L", "Le", "Lea", "Lead"}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The functions should process mixed upper/lower case characters.")

    def long_strings(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = {'abcdefghijklmnopqrstuvwx', 'abcdefg', 'abcdefghijklmnop', 'abcdefghijklmnopqr', 'ab', 'abcdefghijklmnopqrstuvwxyz', 'abcdefghijklm', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuv', 'abcdefghijkl', 'abcd', 'abc', 'abcdefghijklmnopqrst', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefgh', 'a', 'abcdefghij', 'abcde', 'abcdefghijklmnopq', 'abcdefghijk', 'abcdef', 'abcdefghi', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrstu'}
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should process long strings.")
    
    def bad_data(self):
        "Input is not a string"
        s = 1234
        expected =  set()
        result = functions.all_prefixes(s)
        self.assertEqual(expected, result, "The function should handle bad input.")


class TestIsSorted(unittest:TestCase):
    """ Tests the functions.is_sorted() function"""
    def general_case(self):
        Input = [1, 2, 2, 3, 4]
        Expected_Output = True
        '''Explanation: This is a typical nondecreasing list with repeated values.'''
        result = functions.is_sorted(Input)
        self.assertEqual(Expected, Input, "The function should handle the general case")
        
    def strictly_increasing_case(self):

Input: [1, 2, 3, 4, 5]
Expected Output: True
Explanation: This is a strictly increasing list with no repeated values.
Decreasing Case:

Input: [5, 4, 3, 2, 1]
Expected Output: False
Explanation: This is a decreasing list, not nondecreasing.
Random Order with Duplicates:

Input: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Expected Output: False
Explanation: The list is not in nondecreasing order.
Empty List Case:

Input: []
Expected Output: True
Explanation: An empty list is considered sorted.





unittest.main()








####   Unittest Framework:


# Test Case Class:
#To create test cases, you need to define a class that inherits from unittest.TestCase.
# Each test method within this class should start with the word test.

import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Your test code goes here


#Assert Methods:
# unittest provides various assert methods to check conditions and report failures
# if they are not met.

#assertEqual(expected, actual, msg=None):  Checks if expected is equal to actual.
self.assertEqual(4, 2 + 2, "Adding 2 and 2 should equal 4")

# assertTrue(expr, msg=None):  Checks if expr evaluates to True.
self.assertTrue(len([1, 2, 3]) > 0, "The list should not be empty")

# assertIsInstance(obj, class_type, msg=None): Checks if obj is an instance of class_type.
self.assertIsInstance("hello", str, "The variable should be a string")

# assertIs(a, b, msg=None) Checks if a is the same object as b (i.e., they reference the same object in memory).
self.assertIs(obj1, obj2, "Both objects should be the same")


# assertIn(a, b, msg=None): Checks if a is a member of b (i.e., a is in the iterable b).
self.assertIn(3, [1, 2, 3, 4], "3 should be in the list")




Writing Test Cases:
Here's an example test case using these assertion methods:

python
Copy code
import unittest

class MathOperationsTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(4, 2 + 2, "Adding 2 and 2 should equal 4")

    def test_non_empty_list(self):
        self.assertTrue(len([1, 2, 3]) > 0, "The list should not be empty")

    def test_string_instance(self):
        self.assertIsInstance("hello", str, "The variable should be a string")

    def test_object_identity(self):
        obj1 = [1, 2, 3]
        obj2 = obj1
        self.assertIs(obj1, obj2, "Both objects should be the same")

    def test_element_in_list(self):
        self.assertIn(3, [1, 2, 3, 4], "3 should be in the list")

if __name__ == "__main__":
    unittest.main()
Running Tests:
Save the test file and run it using the following command in the terminal:

bash
Copy code
python test_math_operations.py
This will execute all the test methods within the MathOperationsTestCase class and report the results.












