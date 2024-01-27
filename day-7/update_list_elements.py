# lists are mutable
# we can change the elements of a list using index

# create a list
list1 = [1, 2, 3, 4, 5]

# How to update a list element ?

print (list1)
list1[2] *= 2
# please try all the other possible assignment operators here 
# please try all the comparison operators here
print (list1[1] > list1[3])
print (list1)


# change element at index which is not present in list
# list1[5] = 600 # uncomment this line to see the error
# IndexError: list assignment index out of range

# change element at index -1
list1[-1] = 500
print(list1)  # [100, 2, 300, 4, 500]

# a  - identifier / variable / placeholder
#  """a"""/ "a" / 'a' - string literal representation

# How to update a range of list elements

list1 = ['a','b','c','d','e']
#          0   1   2   3   4 
# change range of elements
list1[1:3] = ['A','B']
print(list1)  #['a', 'A', 'B', 'd', 'e']

list1[:] = ['A','B',"C"]
print (list1)

# create list 
list1 = [1,2,3,4,5]
# add a list to a list
list1[1:4] = [[200, 300]]
print(list1)  

# use operators to change list elements
list1[1:4] = ['Rohth', 'Beulah'] * 10
print(list1)  # [100, 200, 300, 200, 300]
# * operator to repeat list elements
list1 = [1, 2, 3, 4, 5]
list2 = list1 * 2
print(list2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# + operator to add two lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
list3 = list1 + list2
print (" + OPERATOR")
print(list3)  # [1, 2, 3, 4, 5, 6, 7, 8]


# use del keyword to delete list elements
list1 = [1, 2, 3, 4, 5]
del list1[0]
print(list1)  # [2, 3, 4, 5]

# use del keyword to delete list elements
list1 = [1, 2, 3, 4, 5]
del list1[1:3]
print(list1)  # [1, 4, 5]

# use del keyword to delete list elements
list1 = [1, 2, 3, 4, 5]
del list1[1:5:2]
print(list1)  # [1, 3, 5]

# use del keyword to delete list elements
list1 = [1, 2, 3, 4, 5]
del list1[::2]
print(list1)  # [2, 4]



# what happens when i try to delete an element which is not present in list
list1 = [1, 2, 3, 4, 5]
del list1[6]
# IndexError: list assignment index out of range


# # what happens when i try to do following 
# list1[:] = 1 # UNCOMMENT TO SEE THE ERROR
# print(list1)  # TypeError: can only assign an iterable

# what happens in this case
list1[:] = "HELLO WORLD"
print (list1)


# following list
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# repeat 1 to 9 again in the above list by replacing 10 to 15
# OUTPUT - [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# now from the above output delete the last 9 digits
# out put - [1,2,3,4,5,6,7,8,9]
# now extend the above list with the following [10,11,12,13,14,15]
# repeat the entire list 2 times
