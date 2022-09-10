try: 
    print(2/0)
except IOError:
    print("this is not an IO error so this line will be ignored")
except ZeroDivisionError:
    print("cant divide by zero")
else:
    print("this is when everything went ok, but it's just weird")
finally:
    print("i dont care if there was an error or not")

# using a blank exception is usually not a got idea, because it catches
# system exceptions (you cant exit the program). So it's best to list the
# exceptions you expect, or in last case use except Exception.

# in python it's better to ask for forgiveness than permission.
# try and catch instead of checking if something will work before. 

# custom exceptions are created as subclasses of the Exception class.
class MyCustomError(Exception):
    pass

def raise_exception():
    # something goes wrong
    raise MyCustomError('describe what went wrong')

try:
    raise_exception()
except MyCustomError as e:
    print(e, "and catch your custom exception")