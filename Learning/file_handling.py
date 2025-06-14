from typing import TextIO, Set, List, Any, Dict
from io import StringIO  #not used since I'm not including examples in my docstrings
import time_series

def smallest_value(reader: TextIO) -> int:
    '''Read and process a TSDL reader and return the smallest value
    after the time_series header'''

    line = time_series.skip_header(reader).strip()

    # line contains the first data value
    # this is the smallest found so far
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)
    return smallest

if __name__ == "__main__":
    with open('hebron_full.txt', 'r') as input_file:
        print(smallest_value(input_file))


def find_largest(line: str) -> int:
    ''' return the largest value in a line,
    which is a whitespace-delimited string
    of non-negative integers that end with '.'.'''

    largest = -1
    for value in line.split():
        if value[-1] == '.':
            value = int(value[:-1])
        else:
            value = int(value)
        largest = max(largest, value)
    return largest

def process_file(reader: TextIO) -> int:
    """ read and process TSDL reader, which must start with
    a time_series heaer.  Return the largest value after the
    header. There may be multiple pieces of data on each line """

    line = time_series.skip_header(reader).strip()
    largest = find_largest(line)

    for line in reader:
        large = find_largest(line)
        largest = max(largest, large)
    return largest

if __name__ == "__main__":
    with open('hopedale_full.txt', 'r') as input_file:
        print(process_file(input_file))
        
def read_molecule(reader: TextIO) -> list:
    """ read a single molecule from the PDB reader and return it,
    or return None to signal the end of the file.  The first item in
    the result is the name of the compound; each list containst an
    atom type and X, Y, Z coordinates of that atom """

    line = reader.readline()
    if not line:
        return None

    #get name of molecule
    parts = line.split()    # convert string to list
    name = parts[1]

    # all other lines are either 'END' or "ATOM num atom_type x y z"
    molecule = [name]  # create a list to hold the data, first element is the name

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()   # convert string to list
            molecule.append(parts[2:])  # append atom_type x y z
    return molecule


def read_all_molecules(reader: TextIO) -> list:
    """ read zero or more molecules from PDB reader, return a list
    of the molecule information. """

    result = []  # create an empty list to hold the molecule

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:   # None is falsey
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('pdb.txt','r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)

def observe_birds(observation_file: TextIO) -> Set[str]:
    ''' Return a set of the bird specieslisted in observation_file
    which has one bird per line '''
    birds_observed = set()
    for line in observation_file:
        bird = line.strip()
        birds_observed.add(bird)  #since sets don't contain duplicates, you can add with no effect

    return birds_observed

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open("observations.txt") as observation_file:
        observed_birds = observe_birds(observation_file)
        for species in observed_birds:
            print(species)

def count_birds(observation_file: TextIO) -> List[List[Any]]:
    ''' in this function, we are trying to avoid using a dictionary to keep
    count of the birds observed.  This is complex and inefficient.
    Considering the worst case for each line, the overall time complexity of
    the function is O(n*m), where n is the number of lines in the file,
    and m is the number of distinct bird species observed.
    Dictionary time complexity  O(n).
    Dictionary will be more efficient as the number bird species observed increases.
    
    Return a set of the bird species listed in observation_file, which has
    one bird species per line'''
    bird_counts = []
    for line in observation_file:
        bird = line.strip()     # recall this removes the \n from each line
        found = False
        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
        if not found:
            bird_counts.append([bird, 1])
    return bird_counts

if __name__ == '__main__':
    with open('observations.txt') as observation_file:
              bird_counts = count_birds(observation_file)
              for entry in bird_counts:
                  print(entry[0], entry[1])


def count_birds2(observation_file: TextIO) -> Dict[str, int]:
     ''' Redo the count_birds function using a dictionary

    Return a set of the bird species listed in the observation_file, which has one
    bird per line '''
     bird_dict = {}
     for line in observation_file:
         bird = line.strip()
         if bird in bird_dict:
             bird_dict[bird] += 1
         else:
             bird_dict[bird] = 1
     return bird_dict

if  __name__ =="__main__":
    with open('observations.txt') as observation_file:
        bird_observations = count_birds2(observation_file)
        for bird, observations in bird_observations.items():
            print(bird, observations)


def count_birds3(observation_file: TextIO) -> Dict[str, int]:
    '''  We get slick and refactor the count_birds2 with a .get method.
    The code is shorter but may be less readable.'''
    
    bird_dict = {}
    for line in observation_file:
        bird = line.strip()
        bird_dict[bird] = bird_dict.get(bird, 0) +1
    return bird_dict
if  __name__ =="__main__":
    with open('observations.txt') as observation_file:
        bird_observations = count_birds3(observation_file)
        for bird, observations in bird_observations.items():
            print(bird, observations)

