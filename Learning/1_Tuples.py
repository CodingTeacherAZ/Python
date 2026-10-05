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
#######
# tuples are immutable. They can be subscripted, sliced, and looped over
# however, the objects that the tuple contains can be mutated
# Remember that tuples are generally used for scenarios where immutability is
# desirable, like representing fixed collections of values. If you need more flexibility,
# consider using lists, which are mutable and support a wider range of operations.

#####    construction    ######
tuple1 = ('A', 'C', 'G', 'T', 'value')
for base in tuple1:
    print(base)

mt_tuple = ()  #placeholder for future data, consistency in function returns of a tuple, dictionary keys, structuring code for future use

single_element_tuple = (8,)  # without the comma, this variable holds int(8)
single_element_tuple = (3+5,)   

base1, base2, base3, base4, value = tuple1  #unpacking a tuple into variables
print(base1)

def process_tuple(t):    # the comma notation is most used with functions and their calls
    pass
# process_tuple(5)  # This would result in an error
process_tuple((5,))  # This is a valid single-element tuple

#####    indexing and slicing    #####
tuple2  = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
tuple2[0][1] = 80.0   #  the tuple can not be changed but the lists inside the tuple can be

#####    Operations    ####
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
print(tuple_a == tuple_b)  #  False
print(tuple_a != tuple_b)  #  True
tuple_c = tuple_a + tuple_b  
print(tuple_c)   # (1, 2, 3, 4, 5, 6)
tuple_d = tuple_a * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple_d)
#####    methods    #####
print(tuple1.count('value'))  # Return number of occurrences of value.
print(tuple1.index('value'))   # Return first index of value. Raises ValueError if the value is not present.
