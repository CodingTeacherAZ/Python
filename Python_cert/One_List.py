'''
1.2 Perform and analyze data and data type operations 
    For each data type:
        -construction
        -indexing
        -slicing,
        -Data type conversion
        -operations
        -methods
'''
####    construction  and data type conversions  ####
whales = [5, 4, 17, 7, 3, 2, 3, 2, 6, 4, 2, 1, 17, 7, 1, 3]
temps = [111.4, 110.6, 108.8, 102.0]
nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']


print(whales)
S = "The first item in a list is at index 0, the second at index 1, and so on.".split()
print(S)
myset = {1, "A", True}
mytuple = (144, 59, 225)
print(list(myset))
print(list(mytuple))
krypton = ['Krypton', 'Kr', -157.2, -153.4, True]  # Can contain any data type

def average(L: list) -> float:  #how to annotate the signature for a list
    ''' return the average of the values in L'''
    return sum(L)/len(L)

print(average(whales))

[[w, x], [[y], z]] = [{10, 20}, [(30,), 40]]  #Python will unpack as long as the structure on the right translates to the structure on the left
print(x)
print(y)
print(w)
print(z)

####    indexing and slicing    ####
print(S[0], whales[1], S[12], whales[13])
print(whales[-1], S[-1])
mtlist = []  # cannot index an emty list
print(nobles)
nobles[1] = 'neon'   # replaces value -->  Lists are MUTABLE
print(nobles)

useful_markers = celegans_phenotypes[0:4] 
print(celegans_phenotypes)   #slicing doesn't mutate the original, 
print(useful_markers)   # can be saved to a new list

mid = len(whales)//2
print(whales[:mid])   #omitting a start value
print(whales[mid:] )   #omitting an end value


####    operations    ####
print(len(S))         # length of
print(max(whales))  # max value in
print(max(nobles))  # max value in
print(min(temps))   # min value in
print(min(S))        # min value in
print(sum(whales))  # sum of elements, must be numeric
print(sorted(S))     # smallest to largest
print(S)              # does not mutate the original list

final = nobles + ['indium']   # list concatenation
print(final)
newlist = nobles + temps
print(newlist)
print(temps * 3)

print(whales)
del whales[0]  # removes an element at an index
print(whales)

def remove_last_item(L: list) -> list:
    '''return L with last item removed'''
    del L[-1]
    return L        # aliasing means the parameter and the list passed through the function call
                        # are pointint to the same memory location.  The list is modified!
print(useful_markers)
remove_last_item(useful_markers)
print(useful_markers)

gas = input("Enter a gas; ")
if gas in nobles:              # in operator
    print('{} is a noble'.format(gas))

print([1, 2] in [0, 1, 2, 3])  # in operator only checks for single items



life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]  # nested list
print(life[1])    # ['United States', 75.5]
print(life[1][0])     # United States  # first index is outer list, second index is inner list

canada = life[0]    # alias
canada[1] = 80.0
print(life)     # changing the value, changed the original list


####    methods    ####

whales.append(temps)  # Appends the list as a nested list in the last element
print(whales)

temps.append(115.2)   # Append single item to end of list
print(temps)

S.append("and Python rocks it")  # Appends the entire string into one element
print(S)

celegans_phenotypes.clear()  #Remove all items from list.
print(celegans_phenotypes)
 
print(nobles.copy())    # Return a shallow copy of the list.
 
print(whales.count(3))  #Return number of occurrences of value.
 
whales.extend(temps) # Each item in the appending list is added as an element in the appended list.
print(whales)

print(S.index('in'))        #Return first index of value.
print(whales.index(3))    #Raises ValueError if the value is not present.
 
nobles.insert(3,"Indium")    # Insert object before index.
print(nobles)

nobles.pop(3)  # Remove and return item at index (default last).
print(nobles)                      # Raises IndexError if list is empty or index is out of range.


whales.remove(3)     #Remove first occurrence of value.
print(whales)                                # Raises ValueError if the value is not present.
 
whales.reverse()     #Reverse *IN PLACE*.
print(whales)

nobles.sort()            # Sort the list in ascending order and return None.
print(nobles)               # list must be all the same data type
                            
people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 28)]
people.sort(key=lambda person: person[1])    #  If a key function is given, apply it once to each
print(people)           # list item and sort them,  ascending or descending, according to

                            # their function values.
temps.sort(reverse=True)    
print(temps)                        # The reverse flag can be set to sort in descending order.



    
