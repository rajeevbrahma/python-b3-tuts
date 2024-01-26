# Defining multiple values to multiple variables

# Syntax:
#    variable1, variable2, variable3 ... = value1, value2, value3 ...

a = 1
b = 2
c = 3

# Example:
a, b, c = 1, 2, 3

print (a) # 1
print (b) # 2
print (c) # 3

# advantage of defining multiple values to multiple variables
# you can swap values of two variables in one line
# without using any third variable

print ("---------- SWAPPING NUMBERS ----------")
# swap values of two variables
a, b = 1, 2
print (a) # 1
print (b) # 2

# swap values of two variables
a, b = b, a
print (a) # 2
print (b) # 1

print ("-------- SAME VALUE TO MULTIPLE VARAIBELS")
# assign same value to multiple variables
a = b = c = 1
print (a) # 1
print (b) # 1
print (c) # 1


