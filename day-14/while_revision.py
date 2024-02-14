# run from numbers 1 to 100 and get me divisibles of 5 in a list 

i = 1 # initialization
output_list = []
while i <= 100: 
    if i%5 == 0:
        output_list += [i]
    i+=1

print (output_list)

while True: # you will stay in the loop forever
    print ("hello there !!")

while False: # you will never enter into the loop 
    print ("hello there !!")
