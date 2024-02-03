# Logical Operators

# Logical operators are used to combine conditional statements.

# Operator	Description	Example
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Example 
x = 5
print (x > 3 and x < 10) # True
print (x > 3 or x < 4) # True
print (not(x > 3 and x < 10)) # False

print ((1>2 and (3<4 or 4<3)))

# exercise
# use all the datatypes to build different comparison statements
# and combine them with the logical operators.

print ('o' in 'hello' and 'o' in 'aeiou')
