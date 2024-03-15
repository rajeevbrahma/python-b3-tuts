
# decorator - is a special function which helps you to 
# modify / extend any method behaviour



#   def validate_input(self,a,b):
#         if (type(a) != int or type(b)!=int):
#             return False
#         return True

class Arth:

    # @validate_input    
    def add(self,a,b):
        return (a+b) 
    
    def sub(self,a,b):
        return (a-b)

arth = Arth()
print (arth.add(1,2))
# print (arth.add(1,"2"))


# decorator definition
def example_decorator(func):
#   # wrapper definition which contains the logic either to extend / modify the function/method behavior
    
    # extend wrapper func
    def extend_func():
        func()  
        print ("This is extend function logic")
    return extend_func

    # # modify wrapper func
    # def modify_func():
    #     print ("This is modified actual function logic")
    # return modify_func


@example_decorator
def hello():
    print ("Hello World")
    
hello()