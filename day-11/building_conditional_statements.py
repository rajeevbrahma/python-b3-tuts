# if it rains and no electricity
#     will go by petrol car 
    
# if it rains and electricity
#     will go by electric car

# if it rains or even drizzle
#     will go by car 

# if it not rains 
#     will go by walk 




# if (it rains and no electricity):
#     will go by petrol car
# elif (it rains and electricity):
#     will go by electric car
# else:
#     pass


# check if a given number is odd and divisible by 5

# step 1 - get the number (input) from the user
# step 2 - check if the number is odd or not 
# step 3 - check if the number is divisible by 5 or not 

number = int(input("Please enter a number - "))

# number/2 - quotient 
# number%2 - reminder
odd_number_check     = number % 2  # ideal case - 1
divisible_by_5_check = number % 5  # ideal case - 0

print (odd_number_check)
print (divisible_by_5_check)

# beginners logic
if odd_number_check == 1:
    print ("Number is ODD")
if divisible_by_5_check == 0:
    print ("Number is Divisible by 5")

# logic - 2
if odd_number_check == 1 and divisible_by_5_check == 0 :
    print ("Number is ODD and Number is Divisible by 5")
else:
    print ("Its not")

# number is even and divisible by 6
