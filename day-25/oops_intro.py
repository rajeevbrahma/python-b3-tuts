"""

    Programming 
    - every business logic - functions
    - object oriented programming - we define classes and we intiate objects of those classes

    oops - just another way of writing your code
    advantages oops - it can be modular, reusable


    # Inheritance - A class can inherit attributes and methods from another class
        Multiple, Multilevel
    # Encapsulation - Hiding the private details of a class from other objects
    # Polymorphism - A concept of using common operation in different ways for different data input
    # Abstraction - Hiding the implementation details from the user
`
    Class variable,
    Instance variable

    class method
    static method

"""

# basic class Blueprint

# class <ClassName>: 

# dunder methods
# __init__
# __repr__
# __str__


class Human:
    # Attributes - Variables of this class
    # Methods - Functions/ Actions of this class
    def __init__(self,name,age):
        # this method will be called by default on initialization of an object of this class
        self.name = name    # attributes
        self.age = age      # variables / attributes

    # reguarl methods
    def talk(self):
        print (self.name,"Talking")
        # print (f"{self.name}, Talking")
        # print ("%s Talking,"%(self.name))
        # print ("{name}, Talking".format(name=self.name))

    def walk(self):
        print (self.name,"Walking")


mark = Human("Mark",25)
june = Human("June",23)
print (type(mark),type(june))
print (mark.name,mark.age)
print (june.name,june.age)
june.talk()
mark.talk()
june.walk()

# #Inheritance
# class Engineer(Human):
#     pass


# Multilevel inheritance
class DhirubhaAmbani:
    pass 

class MukeshAmbani(DhirubhaAmbani):
    pass

class AnanthAmbani(MukeshAmbani):
    pass

class Mark(Human):
    pass 

class June(Human):
    pass

# Multiple inheritance
class Joseph(Mark,June):
    pass

# Base class
class H2:

    def can_burn(self):
        print ("can burn")
# Base class
class O:
    def can_breathe(self):
        print ("can breathe")

# Derived class from H2 and O - Multiple Inheritance
class H2O(H2,O):
    pass







class Animal:

    def __init__(self):
        pass
    
    def eat(self):
        pass

    def run(self):
        pass

animal_1= Animal()
animal_2= Animal()
animal_3= Animal()
animal_4= Animal()
animal_5= Animal()










# class Car:
#     pass









