# access list elements using index

# create a list
list1 = [1, 2, 3, 4, 5, 6, 7]
#        |  |  |  |  |  |  |
#        0  1  2  3  4  5  6  positive index  -->
#       -7 -6 -5 -4 -3 -2 -1  negative index  <--


# access list elements using index
print(list1[0])  # 1
print(list1[1])  # 2

# access list elements using negative index
print(list1[-1])  # 7
print(list1[-2])  # 6


# nested list
list2 = [1, 2, 3, 4, [5, 6, 7, 8]]
#                     |  |  |  |
#                     0  1  2  3  positive index    inner level index
#        |  |  |  |       |
#        0  1  2  3       4       positive index    outer level index             

#       -8 -7 -6 -5  -4 -3 -2 -1  negative index

# access list elements using index
print(list2[0])  # 1
print(list2[1])  # 2
print(list2[2])  # 3

print (list2[4][0]) # 5
print (list2[4][1]) # 6

print (list2[4][-1]) # 8
print (list2[4][-2]) # 7


# access list elements using negative index
print(list2[-1])  # [5, 6, 7, 8]


