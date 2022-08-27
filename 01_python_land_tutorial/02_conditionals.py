# booleans, conditionals and logical operators.
# based on https://python.land/introduction-to-python/python-boolean-and-operators

bools_start_with_upper_case = True

if bools_start_with_upper_case:
    print('sad but true')
else:
    print("i'm just an unreachable else clause")

lie = False

if bools_start_with_upper_case and not lie:
    print('python uses the words "and", "or" and "not"')

can_do_weird_operations = True

if can_do_weird_operations + 1 == 2:
    print('this is so weird')