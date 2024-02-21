# Different types of exception handling

try:
    # file handlnig error
    # database connection error
    # value error

    # print ("Your code block, expecting some exception")
    print (int("hello"))
    
except Exception:
    print ("Catch the exception or correct it")
else:
    print ("if nothing caught")
finally:
    print ("it always exectues")

print ("continue with other lines of program")


def integer_input():
    try:
        number = int(input("give me a random integer"))
    except Exception as e:
        print ("Got an exception")
        print (e)
        print (type(e))
        integer_input()
    
integer_input() 


