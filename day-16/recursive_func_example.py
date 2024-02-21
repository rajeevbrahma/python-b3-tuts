# # Factorial of a given number
# def factorial_of_a_number(number):
#     """ factorial of a number """
#     if number>1:
#         return number * factorial_of_a_number(number-1)
#     return 1

# print (factorial_of_a_number(4))


# # recursive function to produce list of even numbers
# def produce_even_numbers(number, even_numbers):
#     """ produce even numbers """
#     if number<10:
#         even_numbers.append(number)
#         number+=2
#         produce_even_numbers(number, even_numbers)
#     return even_numbers

# print (produce_even_numbers(3, []))


# # recursive function to produce list of even numbers
# def produce_5_multiples(number, even_numbers):
#     """ produce even numbers """
#     if number<20:
#         number+=1
#         if number%5==0:
#             even_numbers.append(number)
#         produce_5_multiples(number, even_numbers)
#     return even_numbers

# print (produce_5_multiples(1, []))

# # recursive function to produce list of even numbers
# def produce_5_multiples_reverse(number, even_numbers):
#     """ produce even numbers """
#     if number<20:
#         number+=1
#         produce_5_multiples_reverse(number, even_numbers)
#     return even_numbers.append(number) if number%5==0 else even_numbers

# print (produce_5_multiples_reverse(1, []))


# definition - global space
def func():
    print ("func called")
    
    def func2(): # is func local space
        print ("func2 called")
    
    func2() # is func local space

func() # call - global space


# definition - global space
def func3(limit):
    print ("func3 called")

    if limit < 5 :
        func3(limit+1) # in func3 local space
    return None

func3(1) # call - global space

# factorial number = 5! - 5*4*3*2*1 = 120

def factorial_number(number):
    
    result = 1
    for i in range(number,1,-1):
        result *= i
        
    print (result)

factorial_number(5)

