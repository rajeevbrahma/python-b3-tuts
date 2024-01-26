# list slicing is a technique to access a range of elements from a list.

# syntax :
#         variable_name[<start>:<end>:<step>] - default - entire iterable
#         start - index/position number from where you want to start
#         end - index / position number till where you wan to access
#         step - positive - same order as initialised
#                 negative - reverse order as initialised

# create a list

list1 = [1, 2, 3, 4, 5, 6, 7]
#        |  |  |  |  |  |  |
#        0  1  2  3  4  5  6  positive index  - forward direction --->
#       -7 -6 -5 -4 -3 -2 -1  negative index  - reverse direction <---

print ("------ accessing range of list elements --------")

print (list1[::])  # by default start 0, end lenght of your list, step 1

# slice list elements from index 0 to 3
print(list1[0:3])  # [1, 2, 3]
print(list1[0:3:1])  # [1, 2, 3]

# slice list elements from index 2 to 5
print(list1[2:5])  # [3, 4, 5]
print(list1[2:5:1]) # [3, 4, 5]

# slice list elements from index 2 to 5 with step 2
print(list1[2:5:2])  # [3, 5]


list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
          

print (list2[::4])

# slice list elements from index 0 to 5 with step 2
print(list1[0:5:2])  # [1, 3, 5]

# slice list elements from index 0 to 5 with step 3
print(list1[0:5:3])  # [1, 4]

# # slice list elements from index 5 to 0 with step -1
# print(list1[5:0:-1])  # [6, 5, 4, 3, 2]

# # slice list elements from index 5 to 0 with step -2
# print(list1[5:0:-2])  # [6, 4, 2]

# print (list1[0:5:-1]) # [] - empty list
# # because step is negative and start index is 0 and end index is 5
# # so, it will traverse from 0 to 5 in reverse direction
# # but there is no element at index 5 in list1
# # hence, it will return empty list

# print (list1[5:0:1]) # [] - empty list
# # because step is positive and start index is 5 and end index is 0
# # so, it will traverse from 5 to 0 in forward direction
# # but there is no element at index 5 in list1
# # hence, it will return empty list

# print (list1[::]) # [1, 2, 3, 4, 5, 6, 7]
# # default start index is 0, default end index is length of list1
# # default step is 1

# print (list1[::-1]) # [7, 6, 5, 4, 3, 2, 1]
# # default start index is length of list1, default end index is 0




