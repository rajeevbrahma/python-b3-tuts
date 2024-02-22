def count(word):
    count = 0
    for letter in word:
        count+=1
    return count

string_var = "hello world"
print (count(string_var))

numeric_string = "123"

print (string_var.count("l"))
print (string_var.capitalize())
print (string_var.upper())
print (string_var.find("o"))

print (numeric_string.isnumeric())


# Examples of methods

EXAMPLE_SENTENCE_1 = "Python is very easy to learn"
EXAMPLE_SENTENCE_2 = " But you have to practice every day "
FULL_CAPITAL_SENTENCE = "PYTHON IS VERY EASY TO LEARN"
SMALL_CAPITAL_SENTENCE = "python is very easy to learn"
MIXED_CASE_SENTENCE = "PyThOn Is VeRy EaSy To LeArN"
NUMERIC_STRING = "1234567890"

print(EXAMPLE_SENTENCE_1.capitalize()) # turns the first letter of first word into upper case
print(SMALL_CAPITAL_SENTENCE.upper()) # turns all the letters into upper case
print(FULL_CAPITAL_SENTENCE.lower()) # turns all the letters into lower case
print(EXAMPLE_SENTENCE_1.title()) # turns the first letter of every word into upper case

# turns the first letter of every word into upper case and vice versa
print(MIXED_CASE_SENTENCE.swapcase())

print(EXAMPLE_SENTENCE_1.casefold()) # turns all the letters into lower case


EXAMPLE_SENTENCE_4 = "Hello world"

# print(EXAMPLE_SENTENCE_4.center(17,"*")) # adds given number of spaces before the center of the string
# print(EXAMPLE_SENTENCE_4.center(29,"*")) # adds given character before the center of the string

EXAMPLE_SENTENCE_3 = "Python is easy to learn and easy  to code and easy to understand"

print(EXAMPLE_SENTENCE_3.replace("easy","super easy",1)) # replaces the given word with the given word
print(EXAMPLE_SENTENCE_3.replace("easy","super easy",3)) # replaces the given word with the given word


print(EXAMPLE_SENTENCE_1.startswith("P")) # returns True if the string starts with the given character
print(EXAMPLE_SENTENCE_1.endswith("n")) # returns True if the string ends with the given character
print(EXAMPLE_SENTENCE_1.isalnum()) # returns True if the string is alphanumeric
print(EXAMPLE_SENTENCE_1.isalpha()) # returns True if the string is alphabetic
print(EXAMPLE_SENTENCE_1.isdecimal()) # returns True if the string is decimal
print(NUMERIC_STRING.isdecimal()) # returns True if the string is decimal
print(EXAMPLE_SENTENCE_1.isdigit()) # returns True if the string is digit
print(NUMERIC_STRING.isdigit()) # returns True if the string is digit

print(EXAMPLE_SENTENCE_1.islower()) # returns True if the string is lower case


print (EXAMPLE_SENTENCE_1.find("t"))  # Returns the index of a char in the string
print (EXAMPLE_SENTENCE_1.index("t")) # Returns the index of a char in the string
print (EXAMPLE_SENTENCE_2.strip())   # Removes white space at begining or ending of a string 

EXAMPLE_SENTENCE_5 = "This is a python class and we are learning methods"
# space is the default sperator
print (EXAMPLE_SENTENCE_5.split())   # splits the string into a list of words

EXAMPLE_SENTENCE_6 = "FAJKSFO/ASDIF9/89AS8F"
print (EXAMPLE_SENTENCE_6.split("/"))   # splits the string into a list of words


print(" ".join(["Python", "is", "easy", "to", "understand"]))  # joins every character with the given character (space in this example)

print(" ".join("hello"))  # joins every character with the given character (space in this example)

print ("hello" + "world")

# function definition
def count():
    pass 

# # class definition
# class String:

#     # method definition
#     def count():
#         pass
#     def upper():
#         pass 

# s = String()

# s.count()
# s.upper()

