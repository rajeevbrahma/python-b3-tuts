# Tuples are ordered
#     To store multiple values of various datatypes
#     Can access using the index
#     "immutable / unchangeable"

# advantage of tuple over list
    # tuple is immutable
    # tuple is faster than list
    # tuple is more secure than list

# Syntax:
#    example_tuple = (1,2,3) # This is a tuple
#    example_tuple = 1,2,3  # This is also a tuple - # even if you don't use parenthesis, it will still create a tuple
#    example_tuple = ()     # This is empty tuple
#    example_tuple = tuple() # This is using tuple constructor

# constructor is a function that creates an object
# even list can also be created using constructor
# example_list = list() # create a list
# adding elements to a above list using append method but not possible using indexes
# example_list[0] = 1 # TypeError: list assignment index out of range

# create list 
list1 = []
list2 = list() # list constructor

print (type(list1))
print (type(list2))


tuple1 = (1,2,3,4) # standard initialization with braces
tuple2 = 1,2,3,4,5 # initialization without braces
empty_tuple = ()   # empty tuple intialization
tuple3 = tuple()  # using tuple constructor

print (type(tuple1))
print (type(tuple2))
print (type(tuple3))
print (type(empty_tuple))

# usage of constructor 
# constructor - is a predefined function which creates object / initialize of a specific datatype

# create a tuple
example_tuple = (1, 2, 3, 4, 5)
print(example_tuple)  # (1, 2, 3, 4, 5)

# create a tuple
example_tuple = 1, 2, 3, 4, 5
print(example_tuple)  # (1, 2, 3, 4, 5)

# create a tuple
example_tuple = ()
print(example_tuple)  # ()

# create a tuple
example_tuple = tuple()

print ("------ accessing tuple elements individually ------ ")

# here is how we can access tuple elements
# create a tuple
example_tuple = (1, 2, 3, 4, 5,(12,('h','c'),3,4),[4,'500',6],'hello')
                                                    # 012
                                                    #-3-2-1    
# access first element
print(example_tuple[0])  # 1

# access last element
print(example_tuple[-1])  # 5

# exercise how can access 'c'
print (example_tuple[5][1][1])
# same thing using negative index
print (example_tuple[-2][-2][0])

# how can we access 500
print (example_tuple[6][1])
print (type(example_tuple[6][1]))
# same thing using negative index


print ("------- accessing tuple elements of a certain range ------ ")

# selct range using positive index
# select range using negative index
# select range using positive and negative index
# use positive step
# use negative step

# access range of elements
print(example_tuple[1:4])  # (2, 3, 4)

# here is how we can change tuple elements
# create a tuple
example_tuple = (1, 2, 3, 4, 5)


print ("------ Tuples are immutable ----- ")

# create tuple
example_tuple = 1,2,3,4,5,5,6

# change element at index 0
# example_tuple[0] = 100 # uncomment it to see the error
# TypeError: 'tuple' object does not support item assignment

# change range of elements
# example_tuple[1:4] = [200, 300] # uncomment it to see the error
# TypeError: 'tuple' object does not support item assignment

# add a tuple to a tuple
# example_tuple[1:4] = (200, 300) # uncomment it to see the error
# print(example_tuple) # TypeError: 'tuple' object does not support item assignment

# use del keyword to delete tuple elements
# del example_tuple[0] # uncomment it to see the error
# TypeError: 'tuple' object doesn't support item deletion



print (" ---------- Tuple datatype converstion  ---------------- ")
# # can we convert tuple to list?
# # yes, we can convert tuple to list

tuple_1 = 1,2,3,4,5
print (tuple_1)
print (type(tuple_1))

list_converted_tuple = list(tuple_1)
print (list_converted_tuple)
print (type(list_converted_tuple))


list_1 = [1,2,3,4]
print (list_1)
print (type(list_1))

tuple_converted_list = tuple(list_1)
print (tuple_converted_list)
print (type(tuple_converted_list))

# # heterogeneous tuple
# example_tuple = (1, 2, 3, 4, 5, "hello", "world", True, 1.2)
# print(example_tuple)  # (1, 2, 3, 4, 5, 'hello', 'world', True, 1.2)

