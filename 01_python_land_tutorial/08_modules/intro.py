# The name of a Python module is the file name without .py.
# The name of this module is "intro".
# Modules are usually imported in the beginning of files, but not necessarily.
# You can dinamically decide to import a module (really weird...)

import greeter
greeter.greet()

# you can also import a part (or parts) of a module

from greeter import greet
greet('smart importer')

# you can import everything with a wild card, but really ask yourself why
# you would want to do that

from greeter import *
greet('dumb importer')

# to use an alias

import greeter as g
g.greet('does it hurt you to type my module full name?')

# to know if a module is being run as a script, we check its name.
# __name__ contains the name of the module (defaults to __main__)

if __name__ == '__main__':
    print("this is a script (or main in an app)")