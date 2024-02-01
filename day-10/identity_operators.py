# Identity operator 
# is, is not
# checks whether two operands(variables / literal) shares the exact
# same location
# It returns True when the operands share the same location, false 
# when they are not

# identity operator checks for identity, not equality
# a is b checks whether a and b are the same object
# a == b checks whether a and b have the same value

# a = 3
# b = 3

# [3] - memblock - 23423423
# ||
# ab

# a = 3000
# b = 3000

# [3000] - a  # memblock - 23847923
# [3000] - b  # memblock - 29374237  

a = 4
b = 4
print (a is b)

a = 'hello'
b = 'hello'
print (a is b)

c = 'This is python tutorial!'
d = 'This is python tutorial!'
# print (c == d)
print (c is d)

a = [1,2,3]
b = [1,2,3]
print (a is b)  # False because they are not the same object in memory location 
# but they are equal in value and type 
# a and b are two different objects that have the same data, but occupy different memory locations.
# a and b are equal objects, but not identical objects.

a = [1,2,3]
b = a
print (a is b) # True

a = {'a':1, 'b':2}
b = {'a':1, 'b':2}
print ("Dictionary - ")
print (a is b)

a = {'a':1, 'b':2}
b = a
print (a is b)


# a = tuple([1,2])
a = (1,2)
b = (1,2)
print ("Tuple - ")
print (a is b)

a = (1,2,3)
b = a
print (a is b)

a = 4
b = 4
print (a is not b)
