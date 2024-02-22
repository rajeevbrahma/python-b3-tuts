""" List Methods """
example_list = ["python", "is","very", "easy", "to", "learn"]
example_list_2 = ["But", "you", "have", "to", "practice", "every", "day"]

# key - will check later
example_list.sort()
example_list.sort(reverse=True)
print (example_list)

example_list_3 = [1,2,1,2,2,3,4,5,5,6,7,8,2]

print (example_list.count("is")) # checks the count of given word in the list

example_list.extend(['and','is'])
print (example_list)

example_list_3.extend([8,9,10])
print (example_list_3)
example_list_3.extend("hello")
print (example_list_3)

example_list = [1,2,3,4,5]

example_list.append(6)   # === example_list += [7]
print (example_list)
example_list.append(7)
print (example_list)
example_list.append(8)
print (example_list)

example_list.insert(1,0)
print (example_list)

example_list.reverse()
print (example_list)

print ("---- POP ---")
example_list.pop() # default index = -1
print (example_list)
example_list.pop(1)
print (example_list)
# example_list.pop(2)
# print (example_list)
example_list = [1,2,3,1,4,4,5,2]
print ("---- REMOVE ----")
example_list.remove(1)
print (example_list)
example_list.remove(2)
print (example_list)

# example_list.clear()
# print (example_list)

print (example_list.index(2))



# exercise 

# define an empty list and populate that list with 1 to 10 numbers using while / for
# [1,2,3,4,5,6,7,8,9,10]
# l = []
# for i in range(1,11):
#     l.append(i)

l = []
i = 1
while i <= 10:
    l.append(i)
    i+=1
print (l)

# reverse the list
# [10,9,8,7,6,5,4,3,2,1]

# insert 1.1 and 1.2 in between 2 and 1
# [10,9,8,7,6,5,4,3,2,1.2,1.1,1]

# pop out the list elements one by one five times
# [10,9,8,7,6,5,4,3,2,1.2,1.1]
# [10,9,8,7,6,5,4,3,2,1.2]
# [10,9,8,7,6,5,4,3,2]
# [10,9,8,7,6,5,4,3]
# [10,9,8,7,6,5,4]

# clear the contents of the list
#[]

