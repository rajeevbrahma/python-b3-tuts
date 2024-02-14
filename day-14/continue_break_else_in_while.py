# continue - will skip that instance
# break - will stop the loop
# else

# else:
while False:
    print ("hello there")
else:
    print ("it didnt enter the loop")

i = 1 # initialization
output_list = []
while i <= 100: 
    if i%5 == 0:
        output_list += [i]
    i+=1
else:
    print ("i is out of range",i)

# continue 

i = 1

print ("----- CONTINUE WHILE ------")
while i < 51:     
    if i % 2 == 0:
        i+=1
        continue
    print (i)
    i+=1
    

# continue 
print ("----- CONTINUE-------") 
list_1 = [1,2,3,4,5,6,7,8,9]
for elem in list_1:
    if elem % 2 == 0:
        continue
    print (elem)


print ("------ BREAK ------")
# break
while i < 10:
    if i == 5:
        break
    print (i)
    i+=1
