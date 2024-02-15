# global and local space examples 
# global space
x = 10
def my_func():
    # local space
    x = 20
    print ("LOCAL SPACE -")
    print(x)

print ("GLOBAL SPACE -")
print(x)
my_func()


# Output: 20
#         10

# using global keyword
x = 10
def my_func():
    global x
    x = 20
    print(x)
my_func()
print(x)

# Output: 20
#         20

# using nonlocal keyword
# nonlocal - used to declare that a variable inside a nested function 
# is not local to it, meaning it lies in the outer inclosing function
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print(x)
    inner()
    print(x)
outer()

# Output: 20
#         20





