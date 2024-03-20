
# Polymorphism Example

class Animal:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Animal({self.name})"
    
    def speak(self):
        print (self.name + " says something")


class Dog(Animal):
    
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Dog({self.name})"

    def speak(self):
        print (self.name + " says woof")
        
class Cat(Animal):
        
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Cat({self.name})"

    def speak(self):
        print (self.name + " says meow")

    

dog = Dog("Tommy")
cat = Cat("Kitty")

print (dog.__str__())
print (cat.__str__())

dog.speak()
cat.speak()



class Math:

    def add(self,a,b):
        return a+b

class Calc1(Math):

    def add(self,a,b):
        return a*2 + b*2
    
class Calc2(Math):

    def add(self,a,b):
        return a*3 + b*3
c1 = Calc1()
print (c1.add(1,2))

c2 = Calc2()
print (c2.add(1,2))






