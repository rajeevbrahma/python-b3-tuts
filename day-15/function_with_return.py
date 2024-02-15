# Function default return 

def default_return():
    print ("Default return")
    # return "something in return" # commenting  this line will return None by defualt

print (default_return())




# Fuction with return

print ("------ SIMPLE FUNCTION WITH RETURN---------")
def func_with_return():
    return 4

return_value = func_with_return()
print (return_value)

# Function with return
print ("------- FUNCTION WITH PARAMETERS AND RETURN ----------")
def add(a, b):
    return a + b
    print ("This is never executed")

result = add(10, 20)

print(result)

# Output: 30

# The return statement is used to exit a function and go back to the place from where it was called.
# The return statement can be used to return multiple values from a function.
print ("------- FUNCTION WITH PARAMETERS AND RETURN MULTIPLE VALUES ----------")

def add_sub(a, b):
    return a + b, a - b

result = add_sub(10, 20)

print(result)

# Output: (30, -10)

# The type of the return value is a tuple and we can use tuple unpacking to get the individual values.

add, sub = add_sub(10, 20)

print(add)
print(sub)

# exercise : write a function to give back square of a given number

print ("------- FUNCTION SCOPE--------")

# global space / global scope
result_list = []
    

def square_of_a_number(number):
    # function scope / local space / local scope
    # print (result_list) 
    global result_list
    result_list += [number * number]
    # print (result_list)
    return result_list

# print (result_list)
print (square_of_a_number(4))
print (square_of_a_number(5))
print (square_of_a_number(6))


# OUTPUT : [16,25,36]

