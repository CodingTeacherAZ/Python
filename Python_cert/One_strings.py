'''
1.2 Perform and analyze data and data type operations 
    For each data type:
        -Data type conversion
        -indexing
        -slicing
        -construction  
        -operations
        -methods
'''
#### User Input #### 
species = input("Enter the species: ")   #getting input from the keyboard
print(species)
number = input("Enter a number: ")
print(type(number))  #  user input is a string
number = int(input("Enter a number: "))
print(type(number))  #  typecast on input to int - can be problematic - best to use try-excpet

#### Data type conversion #### 
print('Four score and ' + str(7) + ' years ago.')  # string concatenation
print(int('11'))      # typecasting to int
print(float('56.32'))   # cast to float
print(float('-324'))   # cast to float
print("A C 5 True".split())   # convert to list
print(list("A C 5 True"))  # cast to list
print(set("A C 5 True"))  # cast to set
print(tuple("A C 5 True"))  # cast to tuple

#### Slicing and Indexing ####
S = "    the {} QuicK \nbrOWn foxes \rr4n 4w4Y b4 THE 5un {}  "
print(S[10:35])
print(S[10:-1])
print(S[45])   # indexing starts at 0
print(S[::-1])  # reverse string using indexing
print(S[-27])  # negative indexing starts at -1

#### Operations #### 
print('AT' * 5)    # string repetition returns empty string if the in is 0 or less
sequence = 'ATTGTCCCCC'
print(len(sequence))
new_sequence = sequence + 'GGCCTCCTGC'
print(new_sequence * 2)

#### Escape Characters #### 
print("That's better")   # change quote marks
print('She said, "That\'s better"')   # escape character \
print(len('\''))   # two characters but len 1

text_with_newline = "Line 1\nLine 2\nLine 3"   # no space between lines
text_with_carriage_return = "Line 1\rLine 2\rLine3" # space between lines
text_with_crlf = "Line 1\r\nLine 2\r\nLine 3"  # commonly used in Windows

print(text_with_newline)
print(text_with_carriage_return)
print(text_with_crlf)

#### multiline strings #### 
numbers = '''one
two
three'''
print(numbers)     # multiline string

#### Print and Comma Operator in Print #### 
print(1, 2, 3)  # comma inserts a space
print(1, "two", 3.0, True)  # comma can handle mixed data types
radius = 5
print("The diameter of the circle is", radius * 2, "cm.") 
print('a', 'b', 'c', sep=', ', end=' :)')
print('a', 'b', 'c', sep=' *  ', end='')  #notice how this line appears directly after
print("...bango")

def convert_to_celsius(fahrenheit: float) -> float:
    """ Return the number of Celsius degrees equivalent to fahrenheit degrees.
    Example:
    convert_to_celsius(75) -> 23.88888888888889
    """
    return round((fahrenheit - 32.0) * 5.0 / 9.0, 1)
print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')

############ String methods ########
# use in and not in to check existence
print('fox?', "fox" in S)
print('doll?',"doll" not in S)
print(len(S))   # len()
print(S.capitalize())  #make the first character have uppercase and the rest lowercase.

print(S.casefold())    # Return a version of the string suitable for caseless comparisons.

print(S.center(20, '*')) # Return a centered string of length width. Padding is done using the
                        # specified fill character (default is a space).

print(S[3:-5].count('he'))  #Return the number of non-overlapping occurrences of substring sub
                          # in string S[start:end]. Optional arguments start and end are interpreted
                          # as in slice notation.

print(S. encode()) #Encode the string using the codec registered for encoding.
                          # encoding='utf-8', errors='strict'

print(S.endswith('k')) # Return True if S ends with the specified suffix, False otherwise.

print(S.expandtabs()) # Return a copy where all tab characters are expanded using spaces.
                          #If tabsize is not given, a tab size of 8 characters is assumed.

print(S.find("q")) #Return the lowest index in S where substring sub is found.
                      #Optional arguments start and end are interpreted as in slice notation.
                      # Return -1 on failure.

print(S.format(5, "arose")) #Return a formatted version of S, using substitutions
                                  #from args and kwargs. The substitutions are identified
                                  # by braces {} in the string.

# Using format_map with a dictionary
person = {"name": "Alice", "age": 30, "city": "Wonderland"}
info_string = "Name: {name}, Age: {age}, City: {city}".format_map(person)
print(info_string)
    #Return a formatted version of S, using substitutions from mapping.
    #The substitutions are identified by braces{} in the string

print(S.index("t"))     #Return the lowest index in S where substring sub is found,
print( S[:-1].index("t"))    # such that sub is contained within S[start:end].  Optional
                            #arguments start and end are interpreted as in slice notation.
      
print(S.isalnum())  #Return True if the string is an alpha-numeric string, False otherwise.
    
print(S.isalpha())  #Return True if the string is an alphabetic string, False otherwise.
  
print(S.isascii())  #Return True if all characters in the string are ASCII, False otherwise.
      
print(S.isdecimal())    # Return True if the string is a decimal string, False otherwise.

print(S.isdigit())  #Return True if the string is a digit string, False otherwise.
    
print(S.isidentifier()) # test whether a string is a reserved identifier
                          #Return True if the string is a valid Python identifier, False otherwise.

print(S.islower())  # Return True if the string is a lowercase string, False otherwise.
    
print(S.isnumeric())   # Return True if the string is a numeric string, False otherwise.

print(S.isprintable())    # Return True if the string is printable, False otherwise.

print(S.isspace())  #Return True if the string is a whitespace string, False otherwise.
  
print(S.istitle())  #Return True if the string is a title-cased string, False otherwise.

print(S.isupper())  #Return True if the string is an uppercase string, False otherwise.
    
print(S.join(["HALLO","THERE!"]))  #Concatenate any number of strings.
                                        #Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

print(S.ljust(25,"~"))   # Return a left-justified string of length width.
   
print(S.lower())    #Return a copy of the string converted to lowercase.

print(S.lstrip())   #Return a copy of the string with leading whitespace removed.
    
print(S.lstrip("e"))     #If chars is given, remove characters in chars instead.

s = "Hello, World!"
print(s.removeprefix("Hello"))  #Return a str with the given prefix string removed if present.
                                    # If the string starts with the prefix string,
                                      # return string[len(prefix):]. Otherwise, return a copy of
                                        # the original string.

print(s.removesuffix("World!"))  #Return a str with the given suffix string removed if present.
                                    # If the string ends with the suffix string and that suffix is
                                      # not empty, return string[:-len(suffix)]. Otherwise, return
                                      # a copy of the original string.

print(S.replace("4", "a"))  # Return a copy with all occurrences of substring old replaced by new.
                                      # count: Maximum number of occurrences to replace.
                                      # -1 (the default value) means replace all occurrences.
                                      # If the optional argument count is given, only the first count
                                      # occurrences are replaced.

sentence = "Python is powerful and Python is easy to learn"
print(sentence.rfind("Python"))
                       # S.rfind(sub[, start[, end]]) -> int
                        #  Returns the highest index (position) of the last occurrence of
                          # the substring in the string. If the substring is not found, it returns -1.
                          # Optional arguments start and end are interpreted as in slice notation.

print(sentence.rindex("Python"))   #  S.rindex(sub[, start[, end]]) -> int
                                      # Returns the highest index (position) of the last occurrence
                                      # of the substring in the string. If the substring is not found,
                                      # it raises a ValueError. Optional
                                    # optional arguments start and end are interpreted as in slice notation.
# the main difference is in how they handle cases where the substring is not found.
#rfind() returns -1, while rindex() raises a ValueError. If you are unsure whether the substring
#will be present in the string, you might prefer to use rfind() and check for -1, or use rindex()
# within a try-except block to handle the potential ValueError.
      
print(S.rjust(25, '~'))     # Return a right-justified string of length width.
                        #Padding is done using the specified fill character (default is a space).

print(S.rpartition("Q")) # Partition the string into three parts using the given separator.
                        # This will search for the separator in the string, starting at the end.
                        # If the separator is found, returns a 3-tuple containing the part before
                        # the separator, the separator itself, and the part after it.
                        #  If the separator is not found, returns a 3-tuple containing two
                        # empty strings and the original string.

print(S.partition("x"))  # Partition the string into three parts using the given separator.
                            # If the separator is not found, returns a 3-tuple containing
                              # the original string and two empty strings.

print(S.rsplit("e")) #Return a list of the substrings in the string, using sep as the separator string.
                     #The separator used to split the string.
                    # When set to None (the default value), will split on any whitespace
                   # character (including \\n \\r \\t \\f and spaces) and will discard
                   #  empty strings from the result.
                  # maxsplit:  Maximum number of splits (starting from the left).
                  #  -1 (the default value) means no limit.
                  # Splitting starts at the end of the string and works to the front.

print(S.split("4")) # Return a list of the substrings in the string, using sep as the separator string.
                     # The separator used to split the string. When set to None
                     # (the default value), will split on any whitespace character
                     # (including \\n \\r \\t \\f and spaces) and will discard empty strings from
                     # the result.
                      # maxsplit: Maximum number of splits (starting from the left).
                       # -1 (the default value) means no limit.
    
                      #  Note, str.split() is mainly useful for data that has been intentionally
                      #  delimited.  With natural text that includes punctuation, consider using
                      #  the regular expression module.
# partition() and rpartition() split the string based on the first and last occurrence of the
# separator, respectively.
# rsplit() splits the string into a list of substrings from the right based on the separator.
# partition() and rpartition() always return a tuple with three elements, while rsplit() returns
# a list of substrings.

print(S.rstrip())  #Return a copy of the string with trailing whitespace removed.
                    # If chars is given and not None, remove characters in chars instead.

print(S.splitlines()) # Return a list of the lines in the string, breaking at line boundaries.
                    # Line breaks are not included in the resulting list unless keepends
                    # is given and true.

print(s.startswith(("P","p")))  #S.startswith(prefix[, start[, end]]) -> bool
                        # Return True if S starts with the specified prefix, False otherwise.
                       # With optional start, test S beginning at that position.
                       #  With optional end, stop comparing S at that position.
                        #   prefix can also be a tuple of strings to try.

print(S.strip())  #Return a copy of the string with leading and trailing whitespace removed.
                    # If chars is given and not None, remove characters in chars instead.

print(S.swapcase()) #Convert uppercase characters to lowercase and lowercase characters to uppercase.

print(S.title())  #Return a version of the string where words start with uppercased characters
                # and all remaining cased characters have lower case.

# Define a translation table
translation_table = str.maketrans("aeiou", "12345")
original_string = "Hello, world! This is a translation example."
print(original_string.translate(translation_table))  #Replace each character in the string using
                #the given translation table.
                # Translation table, which must be a mapping of Unicode ordinals to
                # Unicode ordinals, strings, or None.
                # The table must implement lookup/indexing via __getitem__, for instance a
                # dictionary or list.  If this operation raises LookupError, the character is
                # left untouched.  Characters mapped to None are deleted.

print(S.upper())  #Return a copy of the string converted to uppercase.

print(S.zfill(25)) # Pad a numeric string with zeros on the left, to fill a field of the given width.
  
