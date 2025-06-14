from OOP import Molecule
from OOP import Atom
from typing import TextIO

def read_molecule(r: TextIO) -> Molecule:
    '''  Read a single molecule from r and return it
    or return None to signal the end of the file '''

    # If there isn't another line, we are at the end of the file
    line = r.readline()
    if not line:
        return None

    # Name of the moleule: "COMPND name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num kind x y z"
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(int(num), kind, float(x), float(y), float(z))

    return molecule



ammonia = Molecule("AMMONIA")
ammonia.add(Atom(1, "N", 0.257, -0.363, 0.0))
ammonia.add(Atom(2, "H", 0.257, 0.727, 0.0))
ammonia.add(Atom(3, "H", 0.771, -0.727, 0.890))
ammonia.add(Atom(4, "H", 0.771, -0.727, -0.890))
ammonia.translate(0, 0, 0.2)
print(ammonia)

        
