'''
1.2 Perform and analyze data and data type operations 
    For each data type:
        -construction
        -Data type conversion
        -operations
        -methods
'''
### sets are an unordered, mutable collection of distinct items
## if you need to maintain order, access by index, or slice use lists or tuples

#####    consruction   #####
vowels_1 = {'a', 'e', 'i', 'o', 'u'}
vowels_2 = {'a', 'e', 'a', 'a', 'i', 'e', 'o', 'u', 'u'}
print(vowels_1)    # {'o', 'u', 'i', 'e', 'a'}
print(vowels_2)    # {'o', 'u', 'i', 'e', 'a'}
print(vowels_1 == vowels_2)   # True

empty_set = set()  # must use the constructor function to create an empty set
new_set = set({1, 5, 3})   # must use the {} to create a non-empty set with the set contsructor

set2 = set(range(10))
set1= {0, 1, 2, 3, 4}
set3 = {1, 3, 5, 7, 9}

# Creating a frozenset
fs = frozenset([1, 2, 3, 4, 5])
print(fs)        # Output: frozenset({1, 2, 3, 4, 5})

# Attempting to add an element (will result in an AttributeError)
try:
    fs.add(6)
except AttributeError as e:
    print(f"Error: {e}")
    # Output: Error: 'frozenset' object has no attribute 'add'

# Attempting to remove an element (will result in an AttributeError)
try:
    fs.remove(3)
except AttributeError as e:
    print(f"Error: {e}")
    # Output: Error: 'frozenset' object has no attribute 'remove'

# you must use a frozen set to create a set of sets
frozen_set_of_sets = frozenset([frozenset(set1), frozenset(set2), frozenset(set3)])
print(frozen_set_of_sets)

# frozen sets can contain list, tuple, set, or other collection.

# Creating a dictionary with frozenset keys
dictionary_of_sets = {
    frozenset([1, 2, 3]): 'Set 1',
    frozenset([4, 5, 6]): 'Set 2'
}
print(dictionary_of_sets[frozenset([1, 2, 3])])  # Output: Set 1

#####    Data type conversion    ####
L = [2, 3, 6, 3, 1, 7, 8, 9, 9, 1, 5, 7]
unique_entries = set(L)
print(unique_entries)    #  {1, 2, 3, 5, 6, 7, 8, 9}
new_list = list(unique_entries)
print(new_list)   # [1, 2, 3, 5, 6, 7, 8, 9]

#####   operations   #####
set1 - set2   # set1.difference(set2) -> new set
set1 <= set2  # set1.issubset(set2) -> boolean
set1 >= set2  # set1.issuperset(set2) -> boolean
set1 & set2  # set1.intersection(set2) -> new set
set1 | set2  # set1.union(set2) -> new set
set1 ^ set2  # set1.symmetric_difference(set2) -> new set

print( 9 in set2)   # using the in operator to check existence

#####    methods  #####

set1.add(9)         # add a value to a set1, has no effect if <<value>> is already in the set
set1.difference(set2)  # returns a new set containing elements that are present in set1 but not in set2 {0, 2, 4}
set1.intersection(set2) # creates new set of the overlap between set1 and set2 {1, 3, 9} 
set1.issubset(set2)   # True if  all of set 1 is contained in set 2
set1.remove(0)   # remove a <<value>> from set 1 If the element is not a member, raise a KeyError.
set1.symmetric_difference(set2)  # returns a new set containing elements that are unique to each set, excluding the elements that are common to both sets. {2, 4, 5, 7}
set1.union(set2)   # returns a new set containing all the elements of both sets
set2.clear()        # emties the set
set1.copy()      #Return a shallow copy of a set.
set1.difference_update(set2)  # remove all elements of set2 from set1.
set1.discard(3)  # Remove a <<value>> from set 1 if it is a member. Unlike set.remove(),
                    # the discard() method does not raise an exception when an element is
                    #  missing from the set.
set1.intersection_update(set2) # Update set1 with the intersection of set1 and set2.
set1.isdisjoint(set2)  #Return True if two sets have a null intersection.
set1.issuperset(set2)  #Report whether set2 contains all of set2.
set1.pop()     # Remove and return an arbitrary set element. Raises KeyError if the set is empty.
set1.symmetric_difference_update(set2) # Update set1 with the symmetric difference of itself and set2
set1.update(set2)  # Update set1 with the union of itself and set2.





