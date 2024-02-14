#  Functions are a way to group code together and give it a name.
#     Functions are a way to reuse code.
#     Functions are a way to make your code more 
#         1. readable.
#         2. testable.
#         3. modular.
#         4. debuggable.
#         5. maintainable.
    

#     Syntax:
#     def function_name():
#         # code goes here
#         # code goes here
    
#     function_name() # calling the function
#     function_name() # calling the function again

# GLOBAL SPACE

# function definition
def simple_function():
    # LOCAL SPACE
    print ("This is a simple function example")
    print ("This is a simple function example")
    
simple_function() # function call

def function_not_yet_defined():
    pass

def add(op1,op2): # op1 , op2 - parameters
    print (op1+op2)

add(1,2) # function call with arguments
add(3,4)
add(5,4)
# add(5,6,8)


def sub(op1,op2): # op1 , op2 - parameters
    print (op1-op2)

# condition always make sure your first argument is greater than second argument
sub(2,1) # function call with arguments
sub(1,2)



def sub_keyword_arguments(op1,op2):
    print (op1-op2)

sub_keyword_arguments(op1=2,op2=1)
sub_keyword_arguments(op2=1,op1=2)

print ("----- ARBITRARY POSITIONAL ARGUMENTS -------")
def add_arbitrary_positional_arguments(*ops):
    result = 0
    # ops[0]
    for i in ops:
        print (i)
        result += i
    print ("RESULT -- ")
    print (result)

add_arbitrary_positional_arguments(1,2,3)
print ("\n")
add_arbitrary_positional_arguments(1,2)
print ("\n")
add_arbitrary_positional_arguments(1)
print ("\n")
add_arbitrary_positional_arguments(1,2,3,4,5)
print ("\n")    

print ("----- ARBITRARY KEYWORD ARGUMENTS -------")
def add_arbitrary_keyword_arguments(**ops):
    result = 0
    # print (ops["op1"])
    for i in ops:
        # print (i) # you will print only the keyword
        print (ops[i])
        result += ops[i]
    print ("RESULT -- ")
    print (result)

add_arbitrary_keyword_arguments(op1=1,op2=2,op3=3)
print ("\n")
add_arbitrary_keyword_arguments(op1=1,op2=2)
print ("\n")
add_arbitrary_keyword_arguments(op1=1)
print ("\n")
add_arbitrary_keyword_arguments(op1=1,op2=2,op3=3)
print ("\n") 

# exercise 
# can you define a function which takes multiple arguments and store in list 
