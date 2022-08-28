# the content of this file is executed when 
# its containing package (or a subpackage of that package)
# is imported.

# This file is usually used to import other packages.

print("You've imported mypackage!")

def packfunc():
    print("don't worry")

from .subpackage import * # relative import
subpackage.subfunc()
