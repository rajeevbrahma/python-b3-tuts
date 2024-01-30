# Sets are unordered collections of unique elements.
# Sets are mutable.
# Sets are not indexed.
# Sets are not subscriptable.
# Sets are not sortable.
# Sets are not sliceable.
# Sets are not comparable.
# Sets can contain different data types.

print ("------- initialization of set -------")

# create a set
example_set = {1, 2, 3, 4, 5} # using curly braces
print(example_set)  # {1, 2, 3, 4, 5}

# create a set
example_set = set()
print(example_set)  # set()

# create a set
example_set = set([1, 2, 3, 4, 5])
print(example_set)  # {1, 2, 3, 4, 5}

# create a set
example_set = set((1, 2,3,4,5,5,5,3,3,4))
print(example_set)  # {1, 2, 3, 4, 5}

# print (example_set[0]) # TypeError: 'set' object is not subscriptable

