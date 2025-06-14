''' Object Oriented Programming in Python  Chapter 14

while this isn't specifically on the certification, this is essential to
Error Handling, in particular, unitttesting
'''

#####    Creating a class   ####

class Book_example_1:
    """Information about a book."""
    
ruby_book = Book_example_1()                                  # creates a book object
ruby_book.title = "Programming Ruby"             # creates a title variable inside the book object
ruby_book.authors = ['Thomas', 'Fowler', 'Hunt']    # creates an authors variable inside the book object
# these are called instance variables because they are variables inside of an instance of a class

print(ruby_book.title)
print(ruby_book.authors)
 

#####    Creating a method for the class    #####
class Book_example_2:
    """Information about a book."""
    def num_authors(self) -> int:
        """Return the number of authors of this book. """
        return len(self.authors)

ruby_book = Book_example_2()
ruby_book.title = 'Programming Ruby'
ruby_book.authors = ['Thomas', 'Fowler', 'Hunt']
print(Book_example_2.num_authors(ruby_book))
print(ruby_book.num_authors())


#####  Creating the constructor for the class   #####
from typing import List, Any

class Book:
    """Information about a book, including title, list of authors, publisher, ISBN, and price."""

    def __init__(self, title: str, authors: List[str], publisher: str,
                 isbn: str, price: float) -> None:
        """Create a new book with the given information."""
        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def num_authors(self) -> int:
        """Return the number of authors of this book."""
        return len(self.authors)

    def __str__(self) -> str:
        """Return a human-readable string representation of this Book."""
        return """Title: {0}\nAuthors: {1}\nPublisher: {2}\nISBN: {3}\nPrice: ${4}""".format(
            self.title, ', '.join(self.authors), self.publisher, self.ISBN, self.price)

    def __eq__(self, other: Any) -> bool:
        """Return True iff other is a book and this book and other have the same ISBN """
        return isinstance(other, Book) and self.ISBN == other.ISBN
    
# Create a Book object
python_book_1 = Book('Practical Programming', ['Campbell', 'Gries', 'Montojo'],
                   'Pragmatic Bookshelf', '978-1-6805026-8-8', 25.00)
python_book_2 = Book('Practical Programming', ['Campbell', 'Gries', 'Montojo'],
                   'Pragmatic Bookshelf', '978-1-6805026-8-8', 25.00)
survival_book = Book("New Programmer's Survival Manual", ['Carter'],
                     'Pragmatic Bookshelf', '978-1-93435-681-4', 19.0)

# Accessing attributes
print(python_book_1.title)
print(python_book_1.publisher)
print(python_book_1.ISBN)
print(python_book_1.price)
print(dir(python_book_1))

# Default  __str__ method returns  <__main__.Book object at 0x1053f54d0>
# We created a new __str__ method to print the Book object
print(python_book_1)

# Default == returns False unless the object is compared to itselt
# We created a new __eq__ method to compare two books
print(python_book_1 == python_book_2)
print(python_book_1 == survival_book)

### __dict__  keeps track of instance variables and their values for each instance
print(python_book_1.__dict__)
'''
{'publisher': 'Pragmatic Bookshelf', 'ISBN': '978-1-6805026-8-8',
'title': 'Practical Programming', 'price': 25.0, 'authors': ['Campbell', 'Gries', 'Montojo']}
'''

### __module__  refers to the module object in which the class was defined
print(python_book_1.__module__)
'''__main__'''

### __weakref__ us used by Python to manage when the memory for an
# object can be reused.
print(python_book_1.__weakref__)
'''None'''

#####    Encapsulation    #####
#means keeping data and the code that uses it in one
# place and hiding the details of exactly how they work together.

#####    Polymorphism   #####
# means an expression involving a variable can do different
# things depending on the type of the object to which the variable refers.
# if obj refers to a string, then obj[1:3] produces a two-character string
# however if obj refers to list, then obj[1:3] produces a two-element list
# similarly left + right can produce a number, string or list

def non_blank_lines(thing):
    """ Return the number of non-blank line in thing"""
    count = 0
    for line in thing:
        if line.strip():
            count +=1
    return count

# non_blank_lines can be applied to a list of strings, a file, or a webpage
# each of those three things knows how to be applied to a loop

#####    Inheritance   #####
# Whenever you create a class, you are using inheritance: your new class
# automatically inherits all of the attributes of class object. You can also
# declare that your new class is a subclass of some other class.

class Member:
    ''' A member of a university '''
    def __init__ (self, name: str, address: str, email: str) -> None:
        """ Create a new member """
        self.name = name
        self.address = address
        self.email = email

    def __str__(self) -> str:
        '''Return a string representation of this member'''
        return '{}\n{}\n{}'.format(self.name, self.address, self.email)

class Faculty(Member):
    """ A faculty member at the university """
    def __init__(self, name: str, address: str, email: str, f_num: str) -> None:
        """ Create a new faculty member with an empty list of courses"""
        super().__init__(name, address, email)
        self.faculty_number = f_num
        self.courses_teaching = []

    def __str__(self) -> str:
        member_string = super().__str__()
        return '''{}\n{}\nCourses: {}'''.format(member_string, self.faculty_number, ', '.join(self.courses_teaching))

class Student(Member):
    """ A student member at the university """
    def __init__(self, name: str, address: str, email: str, s_num: str) -> None:
        """ Create a new student member with an empty list of courses"""
        super().__init__(name, address, email)
        self.student_number = s_num
        self.courses_taking = []

pallas = Faculty('Pallas Kennedy', 'Mesa', 'pkennedy@evit.edu', '1234')
pallas.courses_teaching = ['Computer Science', "Culinary Science", "Fashion Design"]
jen = Student('Jennifer Campbell' , 'Tempe', 'jcamp4321@evit.edu', '4321')
print(pallas.name)
print(pallas.email)
print(pallas.faculty_number)
print(jen.name)
print(jen.email)
print(jen.student_number)
print(pallas)
print(jen)


####  Class Atom
class Atom:
    ''' An atom with a number, symbol, and coordinates '''
    def __init__(self, num: int, sym: str, x: float, y: float, z: float) -> None:
        """ Create an Atom with a number nm, string symbol, and three
            float coordinates (x, y, z)
        """
        self.number = num
        self.symbol = sym
        self.center = (x, y, z)

    def __str__(self) -> str:
        """ Return a string representation of this Atom in this format:
            (SYMBOL, X, Y< Z)
        """
        return '({0}, {1}, {2}, {3})'.format(self.symbol, self.center[0], self.center[1], self.center[2])

    def __repr__(self) ->str:
        """ Return a string representation of this Atom in this format:
            Atom(NUMBER, "SYMBOL", X, Y, Z)
        """
        return 'Atom({0}, "{1}" {2}, {3}, {4})'.format(self.number, self.symbol,self.center[0], self.center[1], self.center[2])

    def translate(self, x, y, z):
        self.center = (self.center[0] + x, self.center[1] + y, self.center[2] + z)
        


class Molecule:
    ''' A molecule with a name and list of Atoms '''
    def __init__(self, name: str) -> None:
        """ Create a Molecule named name with no Atoms """
        self.name = name
        self.atoms = []

    def add(self, a: Atom) -> None:
        """ Add a to my list of Atoms """
        self.atoms.append(a)

    def translate(self, x: float, y: float, z: float) -> None:
        """ Move this Molecule, including all atoms by (x, y, z)
        """
        for atom in self.atoms:
            atom.translate(x, y, z)

    def __str__(self) -> str:
        """ return a string representation of this Molecule in the format:
            (NAME, (ATOM1, ATOM2, ...))
        """
        res = ''
        for atom in self.atoms:
            res = res + str(atom) + ", "

        # strip off the last comma
        res = res[:-2]
        return '({0}, ({1}))'.format(self.name, res)

    def __repr__(self) -> str:
        """ Return a string representation of this molecule in the format:
            Molecule("NAME", (ATOM1, ATOM2, ...))
        """
        res = ' '
        for atom in self.atoms:
            res = res + repr(atom) + ', '

        # strip the last comma
        res = res[:-2]
        return 'Molecule("{0}", ({1}))'.format(self.name, res)

class Country:
    def __init__(self, name: str, pop: int, area: int) -> None:
        self.name = name
        self.population = pop
        self.area = area

    def is_larger(self, country2):
        return self.area > country2.area

    def population_density(self):
        return self.population/self.area
    
    def __str__(self):
        return '{0} has a population of {1} and is {2} square kilometers'.format(self.name, self.population, self.area)

    def __repr__(self):
        return 'Country("{0}", {1}, {2})'.format(self.name, self.population, self.area)

class Continent(Country):
    def __init__(self, name, countries):
        super().__init__(name, 0, 0) 
        self.countries = countries

    def total_population(self):
        total = 0
        for country in self.countries:
            total += country.population
        return total


    
    









