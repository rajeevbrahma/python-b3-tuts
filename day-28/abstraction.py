
# Abstraction Example

from abc import ABC, abstractmethod

class BaseCalculator(ABC):
    
    @abstractmethod
    def addition(self,a,b):
        pass

    @abstractmethod
    def subtraction(self,a,b):
        pass

    @abstractmethod
    def multiplication(self,a,b):
        pass

    @abstractmethod
    def division(self,a,b):
        pass

class SimpleCalculator(BaseCalculator):
    
    def addition(self,a,b):
        print (a+b)

    def subtraction(self,a,b):
        print (a-b)

    def multiplication(self,a,b):
        print (a*b)

    def division(self,a,b):
        print (a/b)

simpleCalculator = SimpleCalculator()
simpleCalculator.addition(2,3)
simpleCalculator.subtraction(4,2)
simpleCalculator.multiplication(2,3)
simpleCalculator.division(4,2)
