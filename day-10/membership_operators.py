# Membership opeartor

# in, not in

# checks whether operand 2 is part of operand 1 (varaiables / literal)

# condition : operands should be iterable (strings/lists/tuples/set)

# it returns True when it finds operand 2 in operand 1 and returns false
# when not found

# invalid usage
a = 56
b = 6
# b in a # TypeError: argument of type 'int' is not iterable
# membership operator cannot be used with int type variables 
# because int type is not iterable

# valid usage
a = 'hello'
b = 'H'
print (b in a) # True

# Example with list 
a = [1,2,3,4,5]
b = 3.0
print (b in a) # True

# Example with tuple
a = (1,2,3,4,5)
b = 3
print (b in a) # True

# Example with set
a = {1,2,3,4,5}
b = 3
print (b in a) # True

# Example with dictionary
a = {'a':1, 'b':2}
b = 'a'
c = 2
print (b in a) # True
print (c in a) # This will return False as we dont look for values for in operator
# in this case, it checks whether the key is present in the dictionary or not
# it does not check for the value

# The not in operator is the opposite of in.
a = 'hello'
b = 'h'
print (b not in a) # False


# exercise 
owels = "aeiou AEIOU"
a ='a'

