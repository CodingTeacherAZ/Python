'''
2.2 Construct and analyze code segments that perform iteration 
• while, for, break, continue, pass, nested loops, loops that include compound  
conditional expressions
'''

# Every loop has three parts:
# an initialization section to set up the variables we’ll need,
# a loop condition,
# and a loop body.

#####    while    #####
# looping until a condition is met/ becomes False or when the count
# of times to loop is unknown or unknowable

rabbits = 5     # using a control variable
while rabbits > 0:  # <<expression>>  must evaluate to a boolean
    print(rabbits)
    rabbits -= 1   # must change the value of the control variable in the loop

time = 0
population = 1000 # 1000 bacteria to start with
growth_rate = 0.21 # 21% growth per minute
while population < 2000: # do not use != here because 2000 could be skipped over
    #this will cause the expression to go False at some point
    population = population + growth_rate * population
    print(round(population))
    
    time += 1   # keeping track of the number of loops
print("It took", time, "minutes for the bacteria to double.")
print("The final population was", round(population), "bacteria.")


text = ""
while text != "quit":  # using user input to control the loop
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

playing = True
while playing:    # using user input to control the loop
    print("playing a game")
    playing = input("Would you like to play again? y/n  ") ==  "y"


#####    for    #####
## looping for a count of times and
## when the count of times is known or knowable

speed = 2
velocities = [0.0, 9.81, 19.62, 29.43]
for speed in velocities:            # loop the list by element values
    print('Metric:', speed, 'm/sec')  # because we used the same variable name
print('Final speed: ', speed)        # speed is left holding the last value


country = 'United States of America'
for char in country:   # looping over a string by character
    if char.isupper():    # nesting an if block in a for loop
        print(char)

for num in range(10):    # loop by number using range, starts at 0,
    print(num)              # doesn't include end value 10

mylist = list(range(10))    # creating a list using a range loop
print(mylist)
mylist = list(range(5, 10))   # range(includive start, exclusive stop)
print(mylist)
mylist = list(range(2000, 2050, 4))  #range(incl start, excl stop, step size)
print(mylist)
mylist = list(range(2050, 2000, -4))  # stepping backwards
print(mylist)

total = 0
for num in range(1, 101):   # num holds the numbers in the range
    total = total + num
print(total)

total = 0
for num in range(len(mylist)):   #len() returns an int which can be used in range()
    total += num                 # num is a digit from 0 to len of list, not list element
print(total)

total = 0
for element in mylist:      # element holds the element value in list
     total += element
print(total)

total = 0
for index in range(len(mylist)):   # index holds a number between 0 and len of list
    mylist[index] *= 2     # reassigning element value at that position
    total += mylist[index]    # retrieve element value and add it to the total
print(mylist)     # has been modified!
print(total)

metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]   
for i in range(len(metals)):    # processessing parallel lists of the same length
    print(metals[i], ":", weights[i])

for index, element in enumerate(mylist):   # enumerate will allow you to 
    print(f"Index: {index}, Element: {element}")  #iterate over both index and element


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num, letter in zip(list1, list2):  # the zip function useful for iterating over
                                        # multiple sequences in parallel. It pairs elements
                                        # from each iterable together.
    print(f"Number: {num}, Letter: {letter}")


squared_numbers = [x**2 for x in range(5)] # list comprehension for single line for loops


my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():  # items() unpacks both key and value
    print(f"Key: {key}, Value: {value}")

for key in my_dict:    # iterating over a dictionary, variable holds only the key
    print("key: ", key)

for value in my_dict.values():  # the values() method accesses just the values
    print('value :  ', value)


#####    break -> use sparingly   #####
# Well chosen loop conditions can avoid the use of break
while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
        break    # exits the whil loop 
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

s = 'C3H7'
digit_index = -1 # This will be -1 until we find a digit.
for index in range(len(s)):
    #if we find a digit
    if s[index].isdigit():
        digit_index = index
        break  # this exits the for loop
print(digit_index)


#####    continue -> use sparingly    #####
# well constructed if statements can bypass the use of continue
s = 'C3H7'
total = 0  # sum of the digits
count = 0  #number of digits
for index in range(len(s)):
    if s[index].isalpha():
        continue     # continue immediately starts the next iteration of the loop
    total += int(s[index])  # only incremented if character is numeric
    count += 1     # only incremented if character is numeric
print("total atoms: ", total, "  number of different elements: ", count)


#####    pass    #####
 #   pass is a convenient way to have a syntactically correct code block that
 #   does nothing. It can be useful for temporary placeholders or situations
 #  where the structure of your code requires some content, but you don't
 #  want to perform any specific action in that part of the code.

for i in range(5):
    # Some condition
    if i == 2:
        pass  # This block does nothing for i == 2
    else:
        print(i)


x = 0
while x < 5:
    # Some condition
    if x == 2:
        pass  # This block does nothing for x == 2
    else:
        print(x)
    x += 1

#####    nested loops    #####
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
salt = []
for metal in outer:        # this will change only after the inner loop 
    for halogen in inner:    # has iterated over all its options
        salt.append(metal + halogen)  # the order of the concatenation affects element order, not list order
print(salt)   # the number of elements is len(outer) * len(inner)


def print_table(n: int) -> None:
    """Print the multiplication table for numbers 1 through n inclusive."""
    numbers = list(range(1, n + 1))  # Create a list of numbers which define the multiplication table.
    
    for i in numbers:
        print('\t' + str(i), end='')   # this prints the header row.
    print()  # End the header row.
    
    for i in numbers:
        print (i, end='')  # this prints the first column 
        for j in numbers:
            print('\t' + str(i * j), end='')  #this prints the multiplication table
        print()  # End the current row.
size = int(input("What size of multiplication table would you like? "))
print_table(size)


elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]   # Nested list
for inner_list in elements:
    print(inner_list)  # prints entire inner list

for inner_list in elements:  # entire list
    for item in inner_list:  # each element in the list
        print(item)


drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],
                         ["8:45", "12:44", "14:52", "22:17"],
                         ["8:55", "11:11", "12:34", "13:46", "15:52", "17:08", "21:15"],
                         ["9:15", "11:44", "16:28"],
                         ["10:01", "13:33", "16:45", "19:00"],
                         ["9:34", "11:16", "15:52", "20:37"],
                         ["9:01", "12:24", "18:51", "23:13"]]   # ragged lists: nested inner lists of different size
total = 0
for day in drinking_times_by_day:   # steps into the inner lists by list
    for drinking_time in day:  # accessing each item in the list by element value
        total += 1
        print(drinking_time, end='  ')
    print()
print('average drinks per day: ', round(total/len(drinking_times_by_day)))


        
#####    loops that include compound conditional expressions    #####
## Using compound conditional expressions in loops helps you write
## more concise and readable code by combining multiple conditions in a
## single line. However, it's essential to ensure that your compound conditions
##are clear and don't sacrifice readability. If the conditions become too complex,
##it might be better to break them into separate lines or use functions to
## encapsulate the logic.

print("while")
counter = 0
while counter < 10 and counter % 2 == 0:
    print(counter)
    counter += 1

print("for")
numbers = [1, 4, 7, 2, 8, 11]
for num in numbers:
    if num > 5 and num % 2 == 0:
        print(num)

