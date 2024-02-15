# ((7+4)-3)*4

import calculator # this way we are importing the whole module


print (calculator.add(7,4))
print (calculator.sub(7,4))
print (calculator.mul(7,4))

# print (calculator.mul(calculator.sub(calculator.add(7,4),3),4))

from calculator import add,sub # this way you can choose what to import

print (add(5,4))
print (sub(5,4))

import calculator as c # aliasing the module
from calculator import add as a # aliasing the modules specific function

print (c.add(5,4))

import math
import time 
print (time.time())
