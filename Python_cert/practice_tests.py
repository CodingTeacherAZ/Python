'''
[Aug, 2022] Practicedump 98-381 PDF Dumps and 98-381 Exam Questions (19-34).pdf
'''
##### ======   ======    19 ##### ======   ======  
##start= input("How old were you on your start date? ")
##end = input("How old are you today/ ")
##print("Congratulations on " + str(int(end)-int(start))+ " years of service!")

###### ======   ======   20 ##### ======   ======  
##rooms ={1: 'Foyer', 2: 'Conference'}  # data types int: str
##room = input("Enter the room number: ") # data type str
##if not room in rooms:   # mismatched data types -> mismatched data types; runtime error
##    print('Room does not exist')
##else:
##    print("The room name is " + rooms[room])
##
###### ======   ======    21 ##### ======   ======  
### must accept input
### must return the average rating based on a 5-star scale
### output to 2 decimal places
##Sum = count = done = 0
##average = 0.0
##while (done != -1):
##    rating = float(input("Enter next rating (1-5) or -1 for done "))
##    if rating == -1:
##        break
##    Sum += rating
##    count += 1
##average = float(Sum/count)
##print("The average star rating for the new cofee is: " + format(average, '.2f'))

#### ======   ======    22 ##### ======   ======    
### display primes 2 to 100
##p = 2
##while p <=100:
##    is_prime = True  # if this is outside the while block, there is nothing to reset to True
##    for i in range(2, p):
##        if p % i == 0:  # check for factors  
##            is_prime = False
##            break  # as soon as a factor is found, don't bother looking for more
##    if is_prime == True:
##        print(p)
##    p = p + 1

#### ======   ======   23 ##### ======   ======  
##import sys
##try:
##    file_in = open("in.txt", 'r')
##    file_out = open("out.txt", 'w+')  #out.txt does not exist but will get created
##except IOError:
##    print("Cannot open ", file_name)  # as long as in.txt exists, this code will execute without error
##                                        # if in.txt does not exist, the IOError to say that in.txt doesn't exist
##                                        #  and an error because file_name is not defined
##else:
##    i = 1
##    for line in file_in:
##        print(line.rstrip())
##        file_out.write("line " + str(i) + ": " + line)
##        i = i + 1
##    file_in.close()
##    file_out.close()

###### ======   ======  24 ##### ======   ======  
##
### These first four comment lines are ignored for syntax checking
### The calc_power function calculates exponents   # The pound sign for each line is NOT optional
### x is the base
### y is the exponent
### The Value of x raised to y power is returned
##def calc_power(x, y):
##    comment = "#Return the value"    #This string assignment is NOT interpreted as a comment
##    return x ** y # raise x to the y power


#####  ======   ======  25 ##### ======   ======  
#### Design a decision structure to convert a numeric grade to a letter grade
#### along a 90-80-70-65 range
##
### Letter Grade Converter
##grade = int(input("Enter a numeric grade "))
##if grade >= 90:
##    letter_grade = "A"
##elif grade >= 80:
##    letter_grade = 'B'
##elif grade >= 70:
##    letter_grade = 'C'
##elif grade >= 65:
##    letter_grade = 'D'
##else:
##    letter_grade = 'F'
##print(letter_grade)

####  ======   ======     26 ##### ======   ======   
##numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
##index = 0
##while (index < 10)   # missing colon
##    print(numbers[index])
##    if numbers[index] = 6:  # should be  ==
##        break
##    else:
##        index +=1


####### ======   ======  27 ##### ======   ======  
#### Create a snippet to evaluate input and check for upper and lower case.
##name = input("Enter your name: ")
##if name.lower() == name:
##    print(name, "is all lower case.")
##elif name.upper() == name:
##    print(name, "is all upper case.")
##else:
##    print(name, 'is mixed case.')


##### ======   ======  28 ##### ======   ======
## Float is passed in,  function takes the absval, digits after the decimal are removed
#  use math.fabs() and math.floor()


####### ======   ======  29 ##### ======   ======
#### list contains 200 names, last 5 names are management, slice to display only employees
### Let 196, 197, 198, 199, 200 represent management, print 1 - 195 for employees
##integer_list = [i for i in range(1, 201)]
##print(integer_list[0:-5])
##print(integer_list[:-5])
##
### employees[0:-5]
### employees[:5]

####### ======   ======  30 ####### ======   ======
### read and parse a file
### each line:  itemID price quantity
### ignore blank lines
### close file when all lines are read
##
inventory = open('inventory.txt', "r")
eof = False
while eof == False:
    line = inventory.readline()
    if line !='':
        if line !=  '\n':  # each empty line of the file is encoded as '\n', if this is the first conditional, the else block will fire
            print(line)
    else:
        print("End of file")
        
        eof = True
        inventory.close()

## if line != '\n' : if line !=''  exits at first empty line
## if line != '\n': if line !=None  exits at first empty line
## if line !='': if line !=""  prints empty/blank lines


####### ======   ======  31 ####### ======   ======
##a = 11
##b = 4
##
##print(a / b)  #regular division 11/4 => 2.75
##print(a // b)  # floor division, perform regular division and truncate at decimal => 2
##print(a % b) # peform grade-school divisiona and state the remainder => 3


######### ======   ======  32 ####### ======   ======
### Validate employee numbers of the format of  ddd-dd-dddd and having only numbers
### printTrue if the number is valid
##
##employee_number = 'sentinel' #the while choices being !='' or !='sentinel' forces sentinel here 
##parts = ''
##while employee_number != '':
##    valid = False  #common validation techniqu => assume it is not valid and see if it passes the if blocks
##    employee_number = input("Enter employee number (ddd-dd-dddd) : ")  #if the string is empty, the while loop terminates
##    parts = employee_number.split('-')
##    if len(parts) == 3:
##
##        if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4:
##            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
##                valid = True  # since the input passed through all if conditions, we now set valid to true
##    print(valid)


######### ======   ======  33 ####### ======   ======
#### You must write a script that asks the user for a value.  The value will be used
#### as a whole number in a calculation even if the user enters a decimal.
#### Which code segment should you use?
##
##totalitems = str(input("How many items would you like? "))  # all user input is strings already, this choice doesn't make sense
##totalitems = int(input("How many items would you like? "))  # if the user enters a decimal, this option raises an error
##totalitems = input("How many items would you like? ")  # this option is best to prevent crashing -> use input sanitization or validation
##totalitems = float(input("How many items would you like? "))  # this options accepts both float and int, but will raise an error for anything else


'''
combinedpdf.pdf
'''

######### ======   ======  1  ######### ======   ======  
# repeat

########### ======   ======  2  ######### ======   ======
#### if non-negative return a **(1/b)
#### if negative and even return 'Result is an imaginary number'
#### if negative and odd return -(-a)**(1/b)   <-  no options for thi
##def safe_root(a, b):
##    if a >= 0:
##        answer = a ** (1 / b)
##    else:
##        if a % 2 == 0:
##            answer = "Result is an imaginary number"
##        else:
##            answer = -(-a) ** (1 / b)
##    return answer
##
##print(safe_root(9,2))
##print(safe_root(-4,2))
##print(safe_root(-9,2))

############ ======   ======  3  ######### ======   ======
#### 18 or oder -> 'A"
#### 13 to 17 -> "T"
#### 12 or younger -> "C"
#### unknown age -> "C"
##def get_rating(age):
##    rating = ""
##    if age == None: rating = "C"
##    elif age < 13: rating = "C"
##    elif age < 18: rating = "T"
##    else: rating = "A"
##    return rating
##print(19, get_rating(19))
##print(18, get_rating(18))
##print(17, get_rating(17))
##print(16, get_rating(16))
##print(13, get_rating(13))
##print(12, get_rating(12))
##print("none", get_rating(None))

########## ======   ======  4  ######### ======   ======
## repeat


############ ======   ======  5  ######### ======   ======
### iterate through a list and escape when a target value is found
##productIDList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##index = 0
##while (index < 10 ):
##    print(productIDList[index])
##    if productIDList[index] == 6:
##        break
##    else:
##        index += 1

############ ======   ======  6  ######### ======   ======
#### repeat
#### display all primes from 2 to 100
##p = 2
##while p <= 100:
##    is_prime = True
##    for i in range(2, p):
##        if p % i == 0:
##            is_prime = False
##            break
##    if is_prime == True:
##        print(p)
##    p+=1

########## ======   ======  7  ######### ======   ======
# repeat

############ ======   ======  8  ######### ======   ======
#### Given code answer questions
##def main(a, b, c, d):
##    value = a + b * c - d
##    return value
### Which operation is evaluated first?  b*d  
### Which operation is evaluated second? addition
### which expression is the equivalent? (a + (b*c)) - d
##a = 4
##b = 5
##c = 6
##d = 7
##print(((a + (b*c)) - d) == ( a + b * c - d))


 ########## ======   ======  9  ######### ======   ======
#repeat

########## ======   ======  10  ######### ======   ======
# repeat

############ ======   ======  11  ######### ======   ======
### Evaluate the given code segments
### Code segment 1
##x1 = '20'
##y1 = 3
##a = x1 * y1    # data type: str
##
### Code segment 2
##x2 = 6
##y2 = 4
##b = x2 / y2   # data type float
##
### Code segment 3
##x3 = 2.5
##y3 = 1
##c = x3 / y3   # data type float
##
##print(1, type(a))
##print(2, type(b))
##print(3, type(c))


############ ======   ======  12  ######### ======   ======
### match the data type to int, float, str, bool
##print('+1E10  ->' , type(+1E10))   # float
##print('5.0  ->' , type(5.0))          # float
##print('"True"  ->' , type('True'))   # str
##print('False  ->' , type(False))     # bool

############ ======   ======  13  ######### ======   ======
### count letters
### Function accepts a list of words from a file
### and letter to search for
### Returns count of a particular letter in that list
##def count_letter(letter, word_list):
##    count = 0
##    for word in word_list:
##        if letter in word:
##            count +=1
##    return count
##word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "happy", "island", "jazz", "kite", "lemon", "mountain", "notebook", "orange", "parrot", "quilt", "rainbow", "sunshine", "tiger", "umbrella", "violet", "watermelon", "xylophone", "yoga", "zebra"]
### word_list is populated from a file. Code not shown
##letter = input("Which letter would you like to count?")
##letter_count = count_letter(letter, word_list)
##print("There are : ", letter_count, " instances of " + letter)
##check_count = sum(word.count(letter) for word in word_list)
##print("The letter {} actually appears {} times in the list.".format(letter, check_count))
##print(f"The letter {letter} actually appears {check_count} times in the list.")

############ ======   ======  14  ######### ======   ======
### 1.59 per night
### if return after 8 pm, charge extra day
### if rented on Sunday, cost * 0.7 for as long as they keep the video
### if rented on Thursday, cost * 0.5 for as long as they keep the video
##ontime = input(" Was the video returned before 8 pm? y or n ").lower()
##days_rented = int(input("How many days was the video rented?"))
##day_rented = input("What day was the video rented?").capitalize()
##cost_per_day = 1.59
##if ontime == "n" :
##    days_rented +=1
##if day_rented == "Sunday":
##    total = (days_rented * cost_per_day) * .7
##elif day_rented == "Thursday":
##    total = (days_rented * cost_per_day) * .5
##else:
##    total = days_rented * cost_per_day
##print("Cost of the DVD rental is : $", total)

########## ======   ======  15  ######### ======   ======
# Python Order of operations (precedence)
# Parentheses
# Exponents
# Unary positive, negative, not
# Multiplication and Division
# Addition and Subtraction
# And

############ ======   ======  16  ######### ======   ======
### match the data type to int, float, str, bool
##age = 2
##minor = False
##name = "Contoso"
##weight = 123.5
##zip = '81000'
##print('age', type(age))          # int
##print('minor', type(minor))    # bool
##print('name', type(name))     # str
##print('weight', type(weight))  # float
##print('zip', type(zip))          # str


'''
itexams_98-381_5-combined.pdf
'''

############## ======   ======  21  ######### ======   ======
### evaluate  (3 * (1 +2) ** 2 - (2 ** 2) * 3)
###   (3 * 3 ** 2 - 4 * 3)
###  (3 * 9 - 4 * 3)
### (27 - 12)
### 15
##print( (3 * (1 +2) ** 2 - (2 ** 2) * 3) )


############ ======   ======  22  ######### ======   ======
## repeat


############## ======   ======  23  ######### ======   ======
### calculate the average velocity on a fixed track of 1320 feet
### precise as possible
##distance = int(input("Enter the distance traveled: "))  # track is fixed distance, use int
##distance_miles = distance/ 5280  # division -> float
##time = float(input("Enter the time elapsed in seconds: ")) # float to allow for fractional time
##time_hours = time/3600 # division -> float
##velocity = distance_miles/time_hours
##print("The average velocity is :", velocity, "miles/hour.")

################ ======   ======  23  ######### ======   ======
### identify the math functions to be used
##import math
##def math_it(x: float) -> int:
##    """
##    x, a float is passed into the function
##    Take the abs value of the float
##    remove any decimals after the integer
##    examples:
##    >>>math_it(-12.4)
##    12
##    >>>math_it(17.8)
##    17
##    """
##    step1 = math.fabs(x)
##    step2 = math.floor(step1)
##    return step2
##print(math_it(-12.4))
##print(math_it(17.8))

################## ======   ======  25  ######### ======   ======
###  Identify how to import the math module squareroot function as an alias
##from math import sqrt as squareRoot

################## ======   ======  1 ######### ======   ======
# repeat

################## ======   ======  2  ######### ======   ======
#repeat

################## ======   ======  3  ######### ======   ======
#repeat

################## ======   ======  4 ######### ======   ======
# repeat

################## ======   ======  5  ######### ======   ======
#repeat

################## ======   ======  6 ######### ======   ======
# repeat

################## ======   ======  7  ######### ======   ======
#repeat

################## ======   ======  8 ######### ======   ======
# repeat

################## ======   ======  9  ######### ======   ======
#repeat

################## ======   ======  10 ######### ======   ======
# repeat

################## ======   ======  11  ######### ======   ======
#repeat

################## ======   ======  12 ######### ======   ======
# repeat

################## ======   ======  13  ######### ======   ======
#repeat

################## ======   ======  14  ######### ======   ======
#repeat

################## ======   ======  15  ######### ======   ======
#repeat

################## ======   ======  16  ######### ======   ======
#repeat

################## ======   ======  17  ######### ======   ======
#repeat

#################### ======   ======  18  ######### ======   ======
### given code, analyze and select answers
##numList = [1, 2, 3, 4, 5]
##alphaList = ['a', 'b', 'c', 'd', 'e']
##print(numList is alphaList)    # False
##print(numList == alphaList)   # False
##numList = alphaList  #numList just became an alias of alphaList,
##                        #they both point to the same location in memory
##                        # modifying one will 'modify' both
##print(numList is alphaList)    # True
##print(numList == alphaList)   # True

################## ======   ======  19  ######### ======   ======
#repeat

#################### ======   ======  20  ######### ======   ======
### b equal a multiplied by negative one, then raised to the second power
### a is the input, b is the output
##a = eval(input("Enter a number for the equation: "))
##b = (-a) ** 2
##print(b)

'''
gratisexam.com-Microsoft.PracticeTest.98-381.v2018-08-10.by.Benson.20q.pdf
'''
################## ======   ======  1  ######### ======   ======
#repeat

################## ======   ======  2  ######### ======   ======
#repeat

################## ======   ======  3  ######### ======   ======
#repeat

################## ======   ======  4  ######### ======   ======
#repeat

################## ======   ======  5  ######### ======   ======
#repeat

################## ======   ======  6  ######### ======   ======
#repeat

################## ======   ======  7  ######### ======   ======
#repeat

################## ======   ======  8  ######### ======   ======
#repeat

################## ======   ======  9  ######### ======   ======
#repeat

################## ======   ======  10  ######### ======   ======
#repeat

################## ======   ======  11  ######### ======   ======
#repeat

################## ======   ======  12  ######### ======   ======
#repeat

#################### ======   ======  13  ######### ======   ======
### random integer min of 5 and max of 11
##import random
##print(random.randint(5, 11))
##print(random.randrange(5, 12, 1))

###################### ======   ======  14  ######### ======   ======
### working with files
### return None if the file does not exist
### return the first line if the file does exist
##import os
##def get_first_line(filename, mode):
##    if os.path.isfile(filename):                # first check if it exists
##        with open(filename, 'r') as file:      # with will open, execute, and close
##            return file.readline()              # read the first line
##    else:
##        return None                         # do this if the file does NOT exist
##print(get_first_line('in.txt', 'r'))        

###################### ======   ======  15  ######### ======   ======
# repeat

######################## ======   ======  16  ######### ======   ======
### select the missing line for the given code
##print("What is your name? ")
##name = input()      # input gets data from the user, must be stored in a variable for re-use
##print(name)

######################## ======   ======  17  ######### ======   ======
### read and write data to a text file
### If the file doesn't exist, create it
### if the file exists, remove contents first
##open('local_data', "w+")  # 'w' is write only, 'w+' is read-write
##                            # both create and overwrite

######################## ======   ======  18  ######### ======   ======
### read a data file and prints each line
### correct the indentation of the code 
##import os
##def read_file(file):
##    line = None
##    if os.path.isfile(file):
##        data = open(file, 'r')
##        while line != '':
##            line = data.readline()
##            print(line)
##read_file('in.txt')

######################## ======   ======  19  ######### ======   ======
### repeat
### evaluate the code to determine if it is correct
import sys
try:
    file_in = open('in.txt', 'r')
    file_out = open('out.txt', 'w+')  # file DNE but 'w+' will create one 
except IOError:
    print('cannot open', file_name)  # file_name DNE
else:
    i = 1
    for line in file_in:
        print(line.rstrip())
        file_out.write("line " + str(i) + ": " + line)
        i = i + 1
    file_in.close()
    file_out.close()
##
### the underline code says "The code will execute without error"
### This is true.
### However, if, for any reason, the TRY block fails (like 'in.txt' DNE),
### the except block has a runtime error in the variable name

###################### ======   ======  20  ######### ======   ======
## how to document your code
# place the notes after a # on any line

'''
gratisexam.com-Microsoft.Braindumps.98-381.v2018-07-27.by.Donna.21q.pdf
'''
################## ======   ======  1 ######### ======   ======
# repeat

################## ======   ======  2  ######### ======   ======
#repeat

################## ======   ======  3  ######### ======   ======
#repeat

################## ======   ======  4 ######### ======   ======
# repeat

################## ======   ======  5  ######### ======   ======
#repeat

################## ======   ======  6 ######### ======   ======
# repeat

################## ======   ======  7  ######### ======   ======
#repeat

################## ======   ======  8 ######### ======   ======
# repeat

################## ======   ======  9  ######### ======   ======
#repeat

################## ======   ======  10 ######### ======   ======
# repeat

################## ======   ======  11  ######### ======   ======
#repeat

################## ======   ======  12 ######### ======   ======
# repeat

################## ======   ======  13  ######### ======   ======
#repeat

################## ======   ======  14  ######### ======   ======
#repeat

################## ======   ======  15  ######### ======   ======
#repeat

################## ======   ======  16  ######### ======   ======
#repeat

################## ======   ======  17  ######### ======   ======
#repeat

################## ======   ======  18  ######### ======   ======
#repeat

################## ======   ======  19  ######### ======   ======
#repeat

################## ======   ======  20  ######### ======   ======
#repeat

#################### ======   ======  21  ######### ======   ======
### user logs the number of hours biked
### program sends messages based on the number miles logged
##def get_name():
##    name = input("What is your name? ")
##    return name
##def calc_calories(miles, calories_per_mile):
##    calories = miles * calories_per_mile
##    return calories
##distance = int(input("How many miles did you bike this week? "))
##burn_rate = 50
##biker = get_name()
##calories_burned = calc_calories(distance, burn_rate)
##print(biker, ', you burned about', calories_burned, "calores.")

'''
gratisexam.com-Microsoft.Braindumps.98-381.v2018-07-27.by.Donna.21q.pdf
'''
################## ======   ======  1 ######### ======   ======
# repeat

################## ======   ======  2  ######### ======   ======
#repeat

################## ======   ======  3  ######### ======   ======
#repeat

################## ======   ======  4 ######### ======   ======
# repeat

################## ======   ======  5  ######### ======   ======
#repeat

################## ======   ======  6 ######### ======   ======
# repeat

################## ======   ======  7  ######### ======   ======
#repeat

################## ======   ======  8 ######### ======   ======
# repeat

################## ======   ======  9  ######### ======   ======
#repeat

################## ======   ======  10 ######### ======   ======
# repeat

################## ======   ======  11  ######### ======   ======
#repeat

################## ======   ======  12 ######### ======   ======
# repeat

################## ======   ======  13  ######### ======   ======
#repeat

################## ======   ======  14  ######### ======   ======
#repeat

################## ======   ======  15  ######### ======   ======
#repeat

################## ======   ======  16  ######### ======   ======
#repeat

################## ======   ======  17  ######### ======   ======
#repeat

################## ======   ======  18  ######### ======   ======
#repeat

################## ======   ======  19  ######### ======   ======
#repeat

################## ======   ======  20  ######### ======   ======
#repeat

################## ======   ======  21  ######### ======   ======
#repeat

################## ======   ======  22  ######### ======   ======
#repeat

################## ======   ======  23  ######### ======   ======
#r Yes - No questions about try-except-finally
# A try statement can have one or more except clauses to handle
    # different types of exceptions.
# A try statement can have a finally clause withot an except clause
    # and the finally block is executed wether an exception occurs or not..
# A try statement can have a finally clause and an execpt clause. The try and
    # finally blocks are always executed.  If an exception occcurs, the appropriate
    # except clause will execute.
# A try statement may NOT have more than one finally clause. An attempt
    # to include more than one would raise a syntax error.

################## ======   ======  24  ######### ======   ======
#repeat



'''
PCAP
'''

################## ======   ======  1 ######### ======   ======
# print(2 ** 3 ** 2 ** 1)   # E. 512
#  the exponentian operator works from right to left
# 2 ** 1 == 2
# 3 ** 2 == 9
# 2 ** 9 == 512

#################### ======   ======  2  ######### ======   ======
#### If you want to build a string that reads:
#### Peter's sister's name's "Anna"
#### which of the following literals would you use? (Select all that apply)
##print("Peter's sister's name's \"Anna\"")
##print('Peter\'s sister\'s name\'s \"Anna\"')

# A and B
#################### ======   ======  3  ######### ======   ======
###What is the expected output of the following snippet?
##i = 250
##while len(str(i)) > 72:
##    i *= 2
##else:
##    i //= 2
##print(i)
####A. 125
### loop  i    leni   while?  newi  else?  print
###  1   250   3       F              125   125


#################### ======   ======  4 ######### ======   ======
###What snippet would you insert in the line indicated below:
##n = 0
##while n < 4:
##    n += 1
##    print(n, end=" ")  # C.
##
###to print the following string to the monitor after the loop finishes its
###execution:
# >>> 1 2 3 4


################## ======   ======  5  ######### ======   ======
# What is the value type returned after executing the following snippet?
x = 0                   # int
y = 2                   # int
z = len("Python")      # int == 6
x = y > z               # D. bool
print(x)


#################### ======   ======  6 ######### ======   ======
### What will the final value of the Val variable be when the following snippet
### finishes its execution?
##Val = 1      # binary 0001
##Val2 = 0     # binary 0000
### ^ is the bitwise XOR which will compare each digit in binary.
### for any a ^ b,  XOR returns 1 if  a == b , 0 if a != b
##Val = Val ^ Val2    # 1 ^ 0   Val = 0
##Val2 = Val ^ Val2   #  0 ^ 0   Val2 = 1
##Val = Val ^ Val2    # 0 ^ 1  Val = 0
##print(Val)
####A. 0

#################### ======   ======  7  ######### ======   ======
### Which line can be used instead of the comment to cause the snippet to
### produce the following expected output? (Select all that apply)
###Expected output:
### 0, 1, 2
### Code:
z, y, x = 2, 1, 0    # x = 0, y = 1 , z = 2
x, z = z, y          # x = 2, y =1, z = 1
y = y - z           # x = 2, y = 0, z = 1
x, y, z = y, z, x
print(x, y, z)


z, y, x = 2, 1, 0    # x = 0, y = 1 , z = 2
x, z = z, y          # x = 2, y =1, z = 1
y = y - z           # x = 2, y = 0, z = 1
z, y, x = x, z, y
print(x, y, z)

z, y, x = 2, 1, 0    # x = 0, y = 1 , z = 2
x, z = z, y          # x = 2, y =1, z = 1
y = y - z           # x = 2, y = 0, z = 1
y, z, x = x, z, y
print(x, y, z)
##

####A. x, y, z = y, z, x
####B. z, y, x = x, z, y


################## ======   ======  9  ######### ======   ======
### How many stars (*) does the following snippet print?
##i = 10
##while i > 0 :
##    i -= 3
##    print("*")
##    if i <= 3:
##        break
##else:
##    print("*")
###  loop    i     while  newi   printed  if   printed
###   1      10       T       7     *        F
###   2       7        T       4    *        F
###   3       7        T       1            T     *
####A. three

#################### ======   ======  10 ######### ======   ======
###How many lines does each of the following code examples output when run
### separately?
### Example 1
##for i in range(1, 4, 2):   # i = 1, 3
##    print("*")              # two lines 
##
### Example 2
##for i in range(1, 4, 2):   # i = 1, 3 
##    print("*", end="")     # one line
##
### Example 3
##for i in range(1, 4, 2):   # i = 1, 3
##    print("*", end="**")   # one  line
##
### Example 4
##for i in range(1, 4, 2):   # i = 1, 3
##    print("*", end="**")
##print("***")                # one line


################## ======   ======  11 ######### ======   ======
##Which of the following statements are true? (Select all that apply)
## FALSE   A. UNICODE is the name of an operating system                                        
## FALSE   B. UTF-8 is the name of a data transmission device                                     
## FALSE   C. ASCII is an acronym for Automatic Systems of Computer Inner Interoperability  
## TRUE    D. The Python Language Reference is the official reference manual that describes the syntax and semantics of the Python language
## FALSE   E. Python strings are immutable, which means they cannot be sliced
## FALSE   F. Python strings are mutable, which means they can be sliced
## TRUE   G. Lists and strings in Python can be sliced


#################### ======   ======  12  ######### ======   ======
###What is the result of the following comparison?
##x = "20"
##y = "30"
##string1 = '20'
##string2 = '30'
##print(x > y)    # False print(ord('2'), ord('3'))


#################### ======   ======  13  ######### ======   ======
###What is the expected output of the following snippet?
##s = "Hello, Python!"
##print(s[-14:15])    # start at index -14 and go forward to index 14(inclusive)
####A. Hello, Python!


#################### ======   ======  14 ######### ======   ======
### What is the expected output of the following snippet?
##lst = ["A", "B", "C", 2, 4]
##del lst[0:-2]
##print(lst)
####A. [2, 4]


#################### ======   ======  15  ######### ======   ======
### What is the expected output of the following snippet?
##dict = { 'a': 1, 'b': 2, 'c': 3 }
##for item in dict:            # if no method is applied, the variable stores the key only
##    print(item)
### A. a
###    b
###    c


#################### ======   ======  16 ######### ======   ======
### What is the expected output of the following snippet?
##s = 'python'
##for i in range(len(s)):
##    i = s[i].upper()
##print(s, end="")    # the print command is outside the loop, so what is in variable s is printed
### C. python


#################### ======   ======  17  ######### ======   ======
### What is the expected output of the following snippet?
##lst = [i // i for i in range(0,4)]         # division by zero
##print(lst)
##sum = 0
##for n in lst:
##sum += n
##print(sum)

##E. The program will cause a runtime exception


################## ======   ======  18 ######### ======   ======
### How many stars (*) will the following snippet send to the console?
##lst = [[c for c in range(r)] for r in range(3)]    # lst = [[], [0], [0, 1]]
##for x in lst:                   # iterates over lst by element value, 3 elements
##    for y in x:                 #iterates over lst-elements by value, empty, then 0, then 0, 1
##        if y < 2:               # The empty list causes
##            print('*', end='')
####A. One
####B. Two
####C. Three
####D. Four
####E. The program will cause a runtime exception/error


################## ======   ======  19  ######### ======   ======
#repeat

################## ======   ======  20 ######### ======   ======
# repeat

################## ======   ======  21 ######### ======   ======
# repeat

################## ======   ======  22  ######### ======   ======
#repeat

################## ======   ======  23  ######### ======   ======
#repeat

################## ======   ======  24 ######### ======   ======
# repeat

################## ======   ======  25  ######### ======   ======
#repeat

################## ======   ======  26 ######### ======   ======
# repeat

################## ======   ======  27  ######### ======   ======
#repeat

################## ======   ======  28 ######### ======   ======
# repeat

################## ======   ======  29  ######### ======   ======
#repeat

################## ======   ======  30 ######### ======   ======
# repeat

################## ======   ======  31 ######### ======   ======
# repeat

################## ======   ======  32  ######### ======   ======
#repeat

################## ======   ======  33  ######### ======   ======
#repeat

################## ======   ======  34 ######### ======   ======
# repeat

################## ======   ======  35  ######### ======   ======
#repeat

################## ======   ======  36 ######### ======   ======
# repeat

################## ======   ======  37  ######### ======   ======
#repeat

################## ======   ======  38 ######### ======   ======
# repeat

################## ======   ======  39  ######### ======   ======
#repeat

################## ======   ======  40 ######### ======   ======
# repeat

'''
98-381 Python Programming Practice Test
'''
################## ======   ======  46 ######### ======   ======
def print_table(file):
    data = open(file, 'r')
    for record in data:
        fields = record.split(",")
        print("{0:10}{1:5.1f}{2:7.2f}".format(fields[0], eval(fields[1]), eval(fields[2])))

print_table("in.txt")
