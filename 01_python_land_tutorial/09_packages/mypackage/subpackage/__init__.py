print("You've imported the subpackage!")

def subfunc():
    print('python is ok with import cycles')

import mypackage
mypackage.packfunc()