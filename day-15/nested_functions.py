
y = 20 # global space 

def outer():
    print ("This is outer function")
    x = 10 # outer function scope
    def inner():
        global y
        nonlocal x
        y+=10
        x+=10   # inner / nested function scope
        print (x)
        print (y)
        print ("This is inner function")

    inner()

outer()

# inner() # inner function is not accessible in the global space
# as it is defined in a function space