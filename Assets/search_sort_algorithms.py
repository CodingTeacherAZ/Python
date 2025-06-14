'''' Search and Sort Algorithms  :  Chapter 13 '''
import time
from typing import Callable, List, Any
import random
import bisect

#########################################################################################
#########################################################################################
#####  Search Functions ####
###  Test cases
''''
Element Present:

The element is present in the list.
The element appears multiple times in the list.
Element Absent:

The element is not present in the list.
The list is empty.
List Characteristics:

The list is sorted in ascending order.
The list is sorted in descending order.
The list is unsorted.
The list contains duplicates.
The list contains strings or objects.
'''

## Find, Remove, Find.
def find_remove_find(L: list) -> tuple:
    """Return a tuple of the indices of the two smallest values in list L.
    Time complexity should be O(n)
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_remove_find(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Find the index of the minimum and remove it 
    smallest_value = min(L)
    smallest_index = L.index(smallest_value)
    L.remove(smallest_value)
   
    # Find the index of the new minimum item in the list
    next_smallest_value = min(L)
    next_smallest_index = L.index(next_smallest_value)
    
    # Put the smallest item back in the list
    L.insert(smallest_index, smallest_value)
    
    # Because the list changed size, we may need to fix the value in 
    # second_smallest_index in case it was affected by the removal and reinsertion:
    if smallest_index <= next_smallest_index:
        next_smallest_index +=1
   
    # Return the two indices
    return (smallest_index, next_smallest_index)

items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]


### Sort, identify minimums, get indices.
def sort_identify_index(L: list) -> tuple:
    """Return a tuple of the indices of the two smallest values in list L.
    Time complextity shoudl be O(n log n)
    
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> sort_indentifymins_getindex(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Sort a copy of L <- NEVER mutate the contents of the parameters unless the docstring says to
    temp_list = sorted(L)  #sort() method changes L, sorted() function returns a sorted copy

    # Get the two smallest numbers
    smallest_value = temp_list[0]
    next_smallest_value = temp_list[1]
    
    # Find their indices in the original list L
    smallest_index = L.index(smallest_value)
    next_smallest_index = L.index(next_smallest_value)
    
    # Return the two indices
    return (smallest_index, next_smallest_index)



#####   Walk through the list   ##### 
def walk_through_list(L: list) -> tuple:
    """Return a tuple of the indices of the two smallest values in list L.
    Time complexity should be O(n)
    Second most efficient
    
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> walk_through_list(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # Set up min value variables using the first two items in the list
    if L[0] < L[1]:
        smallest_index, next_smallest_index = 0, 1
    else:
        smallest_index, next_smallest_index = 1, 0

    # Examine each value in the list in order
    for current_index in range(2, len(L)):
        
        # if L[current_index] is smaller than both, update both
        if L[current_index] < L[smallest_index]:
            next_smallest_index = smallest_index
            smallest_index = current_index
        
        # if L[index] is between both, update next_smallest
        elif L[current_index] < L[next_smallest_index]:
            next_smallest_index = current_index
        # if L[index] is larger than both, ignore
        
    # Return the two indices
    return(smallest_index, next_smallest_index)



#####    Timing Functions    #####

def time_find(test_this_function: Callable, lst: List) -> float:
    """Return how many milliseconds test_this_function took to execute.
    """
    time1 = time.perf_counter()
    test_this_function(lst)
    time2 = time.perf_counter()
    return (time2 - time1) * 1000.0


def repeat_testing(number_of_tests: int, test_list_length: int)-> None:
    ''' Performs a number_of_tests calling the time_find function on the
    three functions to find the minimum two values functions on a random
    list of test_list_length'''
    frf_list = []
    sii_list = []
    wtl_list = []
    for i in range(number_of_tests):
        test_list = [random.uniform(0, 1) for _ in range(test_list_length)]

        time_frf = time_find(find_remove_find, test_list)
        time_sii = time_find(sort_identify_index, test_list)
        time_wtl = time_find(walk_through_list, test_list)
        frf_list.append(time_frf)
        sii_list.append(time_sii)
        wtl_list.append(time_wtl)

    frf_ave = sum(frf_list)/len(frf_list)
    sii_ave = sum(sii_list)/len(sii_list)
    wtl_ave = sum(wtl_list)/len(wtl_list)

    print(' "Across 150 tests, Find_remove_find" took an average of  {:.4f} ms. '.format(frf_ave))
    print(' "Across 150 tests, sort_identify_index" took an average of {:.4f} ms. '.format(sii_ave))
    print(' "Across 150 tests, walk_through_list" took an average of {:.4f} ms. '.format(wtl_ave))
    return

# repeat_testing(150, 20000)
'''
 "Across 150 tests, Find_remove_find" took an average of  0.4165 ms. 
 "Across 150 tests, sort_identify_index" took an average of 2.0057 ms. 
 "Across 150 tests, walk_through_list" took an average of 0.6722 ms.
 '''


#########################################################################################
#########################################################################################
#####    List Search Algorithms    #####

# Linear searches start at index zero and looks at each item one by one
# At each index, we ask:  Is this the value we are looking for?


### while_loop_version has an overall time complexity O(n)
##  Across 150 tests, while_loop_search took an average of 1.0102 ms. 
def while_loop_version(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
"""
    i = 0  # control variable mapped to the index
    # Keep going until we reach the end of the list or until we find the value
    while i != len(lst) and lst[i] != value:
        i = i + 1
    # If we fell off the end of the list, we didn't find the value
    if i == len(lst):
        return -1
    else:
        return i

### for_loop_version has an overall time complexity of O(n)
## Across 150 tests, for_loop_search took an average of  0.3779 ms. 

def for_loop_version(lst: list, value: Any) -> int:
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


### the overall time complexity of sentinel_search is O(n)
##  Across 150 tests, sentinel took an average of 0.4259 ms. 

def sentinel_search(lst: list, value: Any) -> int:
    # this method appends the value to the end of the list
    # which guarantees we will find it and guarantees we will not
    # over index the list in the while loop
    # then removes the value from the list before exit

    # Add the sentinel.
    lst.append(value)
    i = 0
    # Keep going until we find value.
    while lst[i] != value: i=i+1

    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i

#### Timing Functions  #####
def time_it(test_this_function: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """Return how many milliseconds test_this_function took to execute.
    """
    time1 = time.perf_counter()
    test_this_function(L, v)
    time2 = time.perf_counter()
    return (time2 - time1) * 1000.0


def repeat_test(number_of_tests: int, test_list_length: int)-> None:
    ''' Performs a number_of_tests calling the time_find function on the
    three functions to find the minimum two values functions on a random
    list of test_list_length'''
    for_list = []
    while_list = []
    sentinel_list = []
    value = random.uniform(0,1)
    for i in range(number_of_tests):
        test_list = [random.uniform(0, 1) for _ in range(test_list_length)]

        time_for = time_it(for_loop_version, test_list, value)
        time_while =  time_it(while_loop_version, test_list, value)
        time_sentinel =  time_it(sentinel_search, test_list, value)
        for_list.append(time_for)
        while_list.append(time_while)
        sentinel_list.append(time_sentinel)

    for_ave = sum(for_list)/len(for_list)
    while_ave = sum(while_list)/len(while_list)
    sentinel_ave = sum(sentinel_list)/len(sentinel_list)

    print(' Across {} tests, for_loop_search took an average of  {:.4f} ms. '.format(number_of_tests, for_ave))
    print(' Across {} tests, while_loop_search took an average of {:.4f} ms. '.format(number_of_tests, while_ave))
    print(' Across {} tests, sentinel took an average of {:.4f} ms. '.format(number_of_tests, sentinel_ave))
    return

# repeat_test(150, 20000)
'''
 Across 150 tests, for_loop_search took an average of  0.3796 ms. 
 Across 150 tests, while_loop_search took an average of 1.0119 ms. 
 Across 150 tests, sentinel took an average of 0.4286 ms.
 '''

###########    Binary Search    ################
## needs a sorted list and performs a half-splitting technique
## to see if the element is larger or smaller than the value

## Across 150 tests, binary_search took an average of  0.0018 ms. 

def binary_search(L: list, v: Any) -> int:
    # mark the left adn right indices of the unknown section
    left = 0
    right = len(L) - 1
    while left != right + 1:
        middle = (left + right)// 2
        if L[middle] < v:
            left= middle + 1
        else:
            right = middle - 1
    if 0 <= left < len(L) and L[left] == v:
        return left
    else:
        return -1

#### built in binary search
##  Across 150 tests, built_in_binary_search took an average of  0.0005 ms. . 
from bisect import bisect_left

def built_in_binary_search(arr, x):
    index = bisect_left(arr, x)
    if index != len(arr) and arr[index] == x:
        return index
    else:
        return -1



#### Timing Functions  #####
def time_binary(test_this_function: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """Return how many milliseconds test_this_function took to execute.
    """
    time1 = time.perf_counter()
    test_this_function(L, v)
    time2 = time.perf_counter()
    return (time2 - time1) * 1000.0

def multiple_tests(number_of_tests: int, test_list_length: int)-> None:
    ''' Performs a number_of_tests calling the time_find function on the
    three functions to find the minimum two values functions on a random
    list of test_list_length'''
    binary_list = []
    built_in_list =[]
    
    value = random.uniform(0,1)
    for i in range(number_of_tests):
        test_list = [random.uniform(0, 1) for _ in range(test_list_length)]
        test_list.sort()
        time = time_binary(binary_search, test_list, value)
        time2 = time_binary(built_in_binary_search, test_list, value)
        binary_list.append(time)
        built_in_list.append(time2)

    binary_ave = sum(binary_list)/len(binary_list)
    built_in_ave = sum(built_in_list) / len(built_in_list)

    print(' Across {} tests, binary_search took an average of  {:.4f} ms. '.format(number_of_tests, binary_ave))
    print(' Across {} tests, built_in_binary_search took an average of  {:.4f} ms. '.format(number_of_tests, built_in_ave))
    return

# multiple_tests(150, 20000)

#########################################################################################
#########################################################################################
######  Sorting Functions   ########
### Test sets
'''
L = [3, 4, 7, -1, 2, 5] # unsorted 
L = [-1, 2, 3, 4, 5, 7]  # sorted in ascending order
L = [7, 5, 4, 3, 2, -1] # sorted in descending order
L = [] # empty 
L = [1] #  length 1
L = [2, 1] # min # for swapping
L = [1, 2]  #sorted min # for swapping
L = [3, 3, 3]  #  same values
L = [-5, 3, 0, 3, -6, 2, 1, 1] #  with duplicates
L = [random.randint(1, 100) for _ in range(10)]  # Randomized input with 10 elements
L = ['banana', 'apple', 'orange', 'grape', 'kiwi'] # list of strings

'''

##  simple but inefficient  ###

def find_largest(n: int, L: list) -> list:
    ''' return a list of the n largest values in list L
    in order from smallest to largest'''
    copy = sorted(L)
    return copy[-n:]

def find_min(L: list, b: int) -> int:
    '''Precondition: L[b:] is not empty
    b marks the index of the smallest value so far
    Return the index of the smallest value in L[b:]
    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    '''
    smallest = b # The index of the smallest value so far
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            smallest = i
        i += 1
    return smallest

def insert(L:list, b:int)->None:
    '''Precondition: L[0,b] is already sorted
    Insert L[b] where it belongs in L[0: b+1]
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    '''
    # find where to insert L[b] by searching backwards from L[b]
    # for a smaller item.
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i -= 1
    # move L[b] to index i, shifting the following values to the right
    value = L[b]
    del L[b]
    L.insert(i, value)
   
#####    Selection Sort    #####  
# search the unknown section for the smallest item
# move it to the index i

def selection_sort(L: list) -> None:
    ''' Reorder the items in L from the smallest to the largest'''
    i = 0
    while i != len(L):
        smallest = find_min(L, i)  # finds the index of the smallest value in L[i:]
        L[i], L[smallest] = L[smallest], L[i]  # Swap that smallest with L[i]
        i += 1

#####    Insertion Sorting    #####  
# takes the next item at index i and inserts it
# where it belongs in the sorted section

def insertion_sort(L: list) -> None:
    '''Reorder the items in L from smallerst to largest'''
    i = 0
    while i != len(L):
        insert(L, i) # insert L[i] where it belongs in L[0: i + 1]
        i +=1

#####    Bubble Sorting   #####
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


##  more efficient but harder to understand and implement
# merge sort, quick sort, heap sort

#####    Merge Sort   #####
# given two lists, produce a new sorted list by comparing elements

def merge(L1: list, L2: list) -> list:
    """Merge sorted lists L1 and L2 into a new list and
    return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1= 0  # initialize L1 index
    i2 = 0 # initialize L2 index

    # for each pair of items in L1[i1] and L2[i2]
    # copy the smaller into newL
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

    # gather any leftover items from the two sections
    # note that one of them will be empty because of
    # loop condition

    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

def mergesort(L: list) -> None: 
    """Merge sorted lists L1 and L2 into a new list and return that new list.
    time complexity is O(n log_2 n)  where n is the number of items in L
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    # Take list L and make a list of one-item lists from it
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    # Initialize index i at 0
    i = 0
    
    # As long as there are two lists (at indices i and i+1)
    # lmerge them, and append the new list to the list of lists
    # increment i by 2
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # copy the last of the merged lists back into the parameter L
    if len(workspace) != 0:
        L[:] = workspace[-1][:]  
  

#####     Binary Sort    #####
def binary_sort(values: list) -> list:
    """ Return a sorted version of the values (This does not mutate values).
    for smaller lists the time complexity is O(n log_2 n)
    but for very large lists the time complexity is O(n^2)
    """
    result = []
    for v in values:
        bisect.insort_left(result, v)
    return result

def built_in(L: list) -> None:
    """Call list.sort --- we need our own function to do this so
    that we can treat it as we treat our own sorts.
    best case time complexity O(n)
    worst case time complexity O(n log n)
    """
    L.sort()

## timing functions
def print_times(L: list) -> None:
    """Print the number of milliseconds it takes for
    selection sort, insertion sort, and list.sort to run.
    """

    print(len(L), end='\t')
    for func in (selection_sort, bubble_sort, insertion_sort, binary_sort, mergesort, built_in):
        if func in (selection_sort, bubble_sort, insertion_sort ) and len(L) > 10000:
            continue
        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
            
    print() # Print a newline.

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000, 100000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)

    
''''
times in milliseconds
len(L)     selection  bubble insertion binary   merge    sort()
10	    0.0	    0.0	    0.0	    0.0	    0.0	    0.0	
1000	   27.0	   22.7	    9.1	    0.2	    1.1	    0.1	
2000	   99.9	   93.8	   36.8	    0.7	    2.6	    0.1	
3000	  223.4	  216.1	   81.0	    1.7	    4.3	    0.2	
4000	  396.9	  388.9	  147.6	    2.4	    5.0	    0.3	
5000	  619.4	  610.5	  226.3	    3.6	    6.4	    0.4	
10000	 2482.4	 2468.6	  907.0	   14.8	   14.4	    0.8	
100000	    --         --         --       1185.2	  190.4	   11.7	

Selection Sort, Bubble Sort, and Insertion Sort:
These are generally less efficient sorting algorithms with a time complexity of O(n^2).
As expected, their execution times increase significantly as the input size grows.

Binary Search:
Binary search is a searching algorithm, not a sorting algorithm.
It has a time complexity of O(log n).
It's significantly faster than the sorting algorithms for larger input sizes, as expected.

Merge Sort:
Merge sort is a more efficient sorting algorithm with a time complexity of O(n log n).
Its execution time is reasonable even for larger input sizes.

Built-in sort() Function:
The built-in sorting function (perhaps list.sort() in Python) is highly optimized
and efficient.
It outperforms other sorting algorithms significantly, even for large input sizes.
Observation for 100,000 elements:

The execution times for Selection Sort, Bubble Sort, and Insertion Sort have become
impractical for such a large input size.
Merge Sort and the built-in sort() function, while slower than the previous input sizes,
are still reasonable.	
'''
      
























































