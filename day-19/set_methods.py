""" set methods """

# what is a set?
# set is a collection which is unordered and unindexed. 
# In Python sets are written with curly brackets.

# Set intialization
#1. Using curly braces
example_set = {"John",23,"UK"}

#2. Using set() constructor
example_set_2 = set(("John",23,"UK"))

print (example_set)
print (example_set_2)

example_set.add("USA")
print (example_set)

example_set_3 = {1,2,3,4,5,6}
example_set_4 = {1,2,3,4}


day1Attendance = {1,2,3,4,5,6}
day2Attendance = {1,2,3,5}
day3Attendance = {1,2,3,4}

print (day2Attendance.difference(day3Attendance))

# discard() - Remove the specified item
example_set_9 = {"John",23,"UK"}
example_set_9.discard("John")
print (example_set_9)

# remove() - Removes the specified element
example_set_23 = {"John",23,"UK"}
example_set_23.remove("John")
print (example_set_23)


day1Attendance = {1,2,3,4,5,6,7,8,9,0}
print (day1Attendance.pop())
print (day1Attendance)

# intersection() - Returns a set, that is the intersection of two other sets
day1Attendance = {1,2,3,4,5,6,7,8,9}
day2Attendance = {1,2,3,4,5,6,7}

print (day1Attendance.intersection(day2Attendance))

# union() - Return a set containing the union of sets
set1 = {1,2,3,4}
set2 = {5,6,7,8}

print (set1.union(set2))

