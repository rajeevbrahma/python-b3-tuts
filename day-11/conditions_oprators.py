
a = [1,2,3,4,5,6]

if 4 in a: # - True
    print ("Yes")
else:
    print ("No")

python_class = ['R','B','S','M']
if 'R' in python_class:
    print ("Yes he/she is present") 
else:
    print ("No he/she is not")

a = int(input("Enter any number"))
b = int(input("Enter any number"))

if a is b:
    print ("Yes they refer to the same memory location")
else:
    print ("No they are at different memory locations")

if 0 & 7:
    print ("Yes")
else:
    print ("No")

# Any value will be considered as a True boolean value
# no value / empty strings / 0 this represent False
    

# 1 / "hello" / [1] / (1,) / {1} / {1:1} - True
# 0 / ""    / [] / () / {} / {} - False

if ([1,2]):
    print ("List has values")
else:
    print ("list is empty")