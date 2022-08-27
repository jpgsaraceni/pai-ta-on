# for and while loops.
# based on https://python.land/introduction-to-python/python-for-loop

for letter in "string":
    print(letter)

# lists can contain different var types
example_list = ['element1', 'element2', True, 10]
for element in example_list:
    print(element)

while True:
    print("uh oh infinite loop")
    break # only allow 1 loop