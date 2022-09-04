#complex data types in Python:
# Tuples () -> immutable
# Dictionaries -> key-value pairs
# Lists [] -> like a tuples but mutable
# Sets {} -> like a list but no duplicates and unordered

# these data types can be declared using (), [] or {}. 
# for tuple. you can just use comma separated elements.
tuple_example = 1, 2, 'third element', True
list_example = [1, 2, 'third_element', True, True]
set_example = {1, 2, 'third_element', True, True} # will ignore last True
# or with the built-in constructors, passing any iterable type as arg.
tuple_from_constructor = tuple([1, 2, 'this is a list'])
tuple_from_constructor2 = tuple({1, 2, 'this is a tuple'})
set_from_constructor = set(tuple_example)
list_from_constructor = list(set_from_constructor)

# you can unpack an iterable using *.
pack = ['a', 'b']
unpacked = (*pack, 'c') # (a, b, c)

# multiple assignment
assignees = ['this guy', 'another guy', 'third']
first_var, second_var, third_var = assignees

# you can access tuples through their index
second_tuple_element = tuple_example[1]

# dictionaries
dict_example = {'key':'value'}
dict_example['key'] # 'value'
dict_example.get('key') # None
# dict_example['wrong-key'] # error
dict_example.get('wrong-key') # None
dict_example.get('wrong-key', 'default') # 'default'

# any hashable type can be used as a key, even types themselves
weird_dict = {int: 'a'}