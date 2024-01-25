# # Using built-in functions to convert one data type to another

# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean


before_conversion = "3"

# math_op = 2 +before_conversion
# print (math_op)                   # unsupported operation, we need to convert


print (before_conversion)
print (type(before_conversion))
after_conversion = int(before_conversion)
print (after_conversion)
print (type(after_conversion))

# # b = int(4.2) 



# Example 1
num = 10
print (num)
print(type(num))
num = float(num)
print (num)
print(type(num))

# Example 2
num = 10.5
print (num)
print(type(num))
num = int(num)
print (num)
print(type(num))

# Example 3
num = 10.5
print (num)
print(type(num))
num = str(num)
print (num)
print(type(num))

# Example 4
num = 10.5
print (num)
print(type(num))
num = bool(num)
print (num)
print (type(num))

# Example 5
num = 0
print (num)
print(type(num))
num = bool(num)
print (num)
print (type(num))



# [1]      / []
# "Hello"     / ""
# 1           / 0 
# 1.0
