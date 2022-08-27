# Some notes about how python deals with strings.
# Based on: https://python.land/introduction-to-python/strings

subject = "World"
useful_tip = "It's best practice to use snake_case for vars in python"
about_quotes = 'Single or double quotes work.\nUse \\ to escape.'
multi_line = """
Use these wierdo triple double quotes 
to write multi line string. Really WTF!
    And identation and newlines count here.
"""
built_in_string_operations = "python has a shit load of built-ins for strings. I used .center to print this one."
f_string = f'f-strings are pretty cool {subject}'

print("Hello",subject)
print(useful_tip)
print(about_quotes)
print(multi_line)
print(built_in_string_operations.center(90, '*'))
print(f_string)