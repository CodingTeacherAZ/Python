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
# as of 3.7, dictionaries are ordered  
#####    construction    #####
dict1 = {
    'key': 'value',
    'canada goose': 3,
    'northern fulmar': 1
    }
dict2 = {
     'northern fulmar': 1,
     'key' : 'value',
     'canada goose' : 3
     }

print(dict1 == dict2)  # even though they are ordered, this is still True

mt_dict = {}   # creates an emtpy dictionary, empty dictionaries can't be indexed

squares = {x: x*x for x in range(1, 6)}  # dictionary comprehension: A concise way to create dictionaries

        ## collisions: 
        ## dict1 = {'a' : 1, 'b' : '1',  'c' : 1}
        ## if you invert this dictionary, making the values the keys, it is unclear what value to associate to it
bird_observations = {'canada goose': 5, 'northern fulmar': 1, 'long-tailed jaeger': 2, 'snow goose': 1}

observation_of_birds = {}
for bird, count in bird_observations.items():
    if count in observation_of_birds:   # checking the key
        observation_of_birds[count].append(bird)   #dict['key']  IS the value, to the value we append
    else:
        observation_of_birds[count] = [bird]   # create the value as a key
print(observation_of_birds)   # {1: ['northern fulmar', 'snow goose'], 2: ['long-tailed jaeger'], 5: ['canada goose']}
        




tuple1 = ('cactus wren', 5)    #this is used in the methods below
#####    working with dictionaries    #####
dict1['northern fulmar']   # dict[key] -> value   access the value, KeyError raised if key isn't present
dict1['snow goose'] = 33  # dict[key] = value    create a new key: value pair 
dict1['northern fulmar'] = 9   # dict[key] = value    also updates the value of existing keys

print('eagle' in dict1)     #  check existence of a key

for bird in dict1:     # loops over keys
    print(bird)

for bird, count in dict1.items():   # unpacks keys, values
    print(bird, count)

     ## handling Key Erros using the get method
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using get to retrieve the value for 'b'
value = my_dict.get('b', 'Key not found')
print(value)  # Output: 2

# Using get for a key that doesn't exist
value = my_dict.get('z', 'Key not found')
print(value)  # Output: 'Key not found'

#####    operations  and methods   #####
del dict1[<<key>>]       # remove a <<key>> : value pair, KeyError raised if key isn't in the dictionary
<<key>> in dict1       # checks for the existence of <<key>> in dict1's keys
dict1.clear()                # return None.  Remove all items from D.

dict1.copy()             # return  a shallow copy of D

dict1.get(<<key>>) # Return the value for <<key>> if key is in the dictionary, else default.

dict1.items()       # return a list of sets of key:value pairs;  used to unpack key, value in loops

dict1.keys()     # return a list of keys;  used to loop over the keys of a dictionary

dict1.pop(<<key>>)     # return value; removes specified  <<key> and return the corresponding value. # If the key is not found, return the default if given; otherwise, # raise a KeyError.

dict1.popitem()   # Remove and return a (key, value) pair as a 2-tuple.  Pairs are returned in LIFO (last-in, first-out) order.  Raises KeyError if the dict is empty.

dict1.setdefault(<<key>>, <<value>>)  # Insert key with a value of default if key is not in the dictionary.  Return the value for key if key is in the dictionary, else default == None. The setdefault() method is useful when you want to ensure that a key is present in the dictionary, and if it's not, you want to set a default value for that key. If the key already exists in the dictionary, setdefault() returns its current value without modifying it. If the key is not present, it inserts the key with the specified default value and returns that value. 

dict1.update(dict2, tuple1)  # Returns None. updates dict1 with elements from dict2 and tuple1. Common items are updated, new items are created in dict1

d1.values() # return a list of values; used to loop over values of a dictionary
