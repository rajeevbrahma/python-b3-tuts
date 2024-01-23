"""
    Memory Management in Python
    How to declare a variable in Python
    Static and Dynamic Typing
    Memory block example of object a example
    Garbage collection in Python

"""
# How to declare a variable in Python:
a = 3
b = 4
c = 3
d = 3

# Memory optimization in Python
#   Python optimizes memory usage by reusing objects.
#   For example, when we create the object a = 3,
#   Python allocates memory for it and stores the value 3.
#   If we create another variable b and set it equal to a,
#   Python doesn't allocate memory for the new variable.
#   Instead, it uses the same memory location where the value of a is stored.
#   This is because the value of a is an integer, which is a primitive type.
#   Primitive types are immutable, so their value cannot be changed.
#   Therefore, there is no risk of changing the value of a when we set b = a.
#   This is called memory optimization.


print ('a -> ',a,id(a))
print ('b -> ',b,id(b))
print ('c -> ',c,id(c))
print ('d -> ',a,id(d))

# Why everything is an object in Python?

#    Memory block example of object a example
#     _______________________
#    | type      |   int     |
#    | ----------------------|
#    | value     |   3       |
#    |-----------------------|
#    | id/address|   1234233 |
#    |-----------------------|
#    | reference |   3       |
#     -----------------------

#    Memory block example of object a example
#     _______________________
#    | type      |   int     |
#    | ----------------------|
#    | value     |   4       |
#    |-----------------------|
#    | id/address|   1234223 |
#    |-----------------------|
#    | reference |   1       |
#     -----------------------


#  a c d     b       - variable name
#  | | |     |
#   [3]     [4] []   - memory block
#    1       2   3   - memory block number

a = 4
c = 5
d = 5

print ('a -> ',a,id(a))
print ('c -> ',c,id(c))
print ('d -> ',a,id(d))

#         a b  c d    - variable name
#         | |  | |    
#  [3]    [4]  [5]    - memory block
#   1      2    3     - memory block number


# Static and Dynamic Typing
#   Static typing means that the type of a variable is known at compile time.
#   Dynamic typing means that the type of a variable is known at run time.
#   Python is a dynamically typed language.
#   In Python, we may assign different types to the same variable.

a = 3
print ('a -> ',a,id(a))
a = 'hello'
print ('a -> ',a,id(a))

# Garbage collection in Python :
#   When the number of references to an object becomes zero, 
#   the object is destroyed automatically, and the memory occupied by it is 
#   made available for future use.
