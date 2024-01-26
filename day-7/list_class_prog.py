# create a list 

list1 = [1,2,3,4,5,[10,['h',[89,76]],11],6,7,8,9]
#                             | |
#                             0 1
#                             -2-1
#                            -----       
#                        |     |   
#                        0     1
#                        -2    -1
#                      -------------  
#                   |        |        |
#                   0        1        2
#                   -3      -2       -1
#                   --------------------                 
#        | | | | |           |           | | | |
#        0 1 2 3 4           5           6 7 8 9
#       -10-9-8-7-6          -5          -4-3-2-1

# accessing list elements
# syntax :
#     list_variable[index_position_number]

print (list1[5][1][1][0])


list1 = [1,2,3,4,5,[10,['h',[12,13],14],11],6,7,8,9]

print ("----- NEGATIVE INDEX -  ACCESSING LIST ELEMENTS ------")

# negative indexing

list1 = [1,2,3,4,5,6,7,8,9]

print (list1[-2])
print (list1[-8])











# #                        |   |           
# #                        0   1
# #                          |
# #                          0     
# #                   |      |     |
# #                   0      1     2 
# #       |  | | | |         |        |  | | |
# #       0  1 2 3 4         5        6  7 8 9  

# list1 5 1 0 0



# chocalates 

# dairy milk, five star, dairy milk, bicuits, [box full of dairy milk], 