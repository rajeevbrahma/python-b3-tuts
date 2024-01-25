# Lists are ordered.
# Lists can contain any arbitrary objects.
# List elements can be accessed by index.
# Lists can be nested to arbitrary depth.
# Lists are mutable / modified 
#     you can use list methods to modify your list
#     you can use operators (+) to modify your list
# Lists are dynamic.



# Indexing in lists
# Indexing in lists is similar to indexing in strings.
# Indexing in lists starts from 0.
# Indexing in lists is done using square brackets [].
# Indexing in lists is done using positive and negative indexes.
# Positive indexes start from 0 and go from left to right.
# Negative indexes start from -1 and go from right to left.

# arbitrary lists of objects
# lists can contain any arbitrary objects
# lists can contain different types of objects
# lists can contain lists
# lists can contain tuples
# lists can contain dictionaries



# 1,2,3,4,5
# a,b,c,d
# list1, list2
# True, False, True

# Syntax 

list_obj = [] # empty list

num_group = [1,2,3,4,5,6,['a','b']]
            #| | | | | |     |
            #0 1 2 3 4 5     6 
                        #  |    |
                        #  0    1 

num_group[6]


float_group = [1.2,1.3,2.4]

employee_details = [
                        'First name',  # - 0
                        "Last name",   # - 1 
                        25,            # - 2 
                        237283.90,
                        True,           # - 4
                        [
                            "Spouse name",
                            24,
                            "Child1",       
                            2
                        ]
                    ]

                         # xyz
                             #x
[ 'Rohith','Buelah',    [['x1','x2'], 'y', 'z'] ] #- class room
#                          |    |
#                             |         |    | 
#                            c1        2    3
#     |        |               |   
#   chair 1   chair 2        bench 3   

class_room[2][0][1]


[ [['R1',"R2"],['RB1',"RB2"]],'Buelah',    [['x1','x2'], 'y', 'z'] ] #- class room

# access RB2
# access R1


