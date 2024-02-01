# Frozenset is just an immutable version of a normal set

# create a frozenset
example_frozenset = frozenset([1, 2, 3, 4, 5])
print(example_frozenset)  # frozenset({1, 2, 3, 4, 5})

# print (example_frozenset[0]) # TypeError: 'frozenset' object is not subscriptable

# add an element to a frozenset
# example_frozenset.add(6) # AttributeError: 'frozenset' object has no attribute 'add'

# remove an element from a frozenset
# example_frozenset.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'

# delete a frozenset
# del example_frozenset # NameError: name 'example_frozenset' is not defined


