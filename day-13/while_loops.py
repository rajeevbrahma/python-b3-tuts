# while (condition):
#  statements

i = 0 # initialization
while i <= 10: # condition
    print (i)
    i+=1  # increment

a = [1,2,3,4,5,6]

print (a)

i = 0
while len(a) > 0: # cond - run through the list till the lenght of the list is greater than 0
    print (a[i])
    del a[i]

print (a)    

# modify the above program to delete only even number indexed elements