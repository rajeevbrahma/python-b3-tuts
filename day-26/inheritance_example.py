
# parent class
class String:
    """ CUSTOM STRING CLASS DEFINITION """

    CAP_VOWELS = "AEIOU"        # class variable
    SMALL_VOWELS = "aeiou"      # class variable

    def __init__(self,word):   # parameter
        self.word = word # variable / identifier -  intance variable
    
    # method
    def vowel_count(self):
        """ VOWEL COUNT """
        vowel_count_var = 0         # method variable
        vowel_characters = ""
        for char in self.word:
            if char in self.CAP_VOWELS or char in self.SMALL_VOWELS:
                vowel_count_var+=1
                vowel_characters += char +","
        vowel_characters = vowel_characters[:-1]
        return vowel_count_var,vowel_characters

class StringV2(String): # child class
    pass

a = StringV2("hello world")
print (a.vowel_count())
print (a.word)
print (a.CAP_VOWELS)

class StringV3(String): # child class with some added methods
    
    def __init__(self,word,char):
        super().__init__(word)
        self.char = char

    def repititive_count_of_a_given_char(self):
        """ repititive count of a char """
        char_count = 0
        for char in self.word:
            if self.char == char:
                char_count +=1
        return char_count

# a = StringV3("hello world",'o')
# print (a.word)
# print (a.char)
# print (a.repititive_count_of_a_given_char())

# b = StringV3("Tomato",'a')
# print (b.word)
# print (b.char)
# print (b.repititive_count_of_a_given_char())

class StringV4(StringV3):
    pass

a = StringV4("hello",'h')


# project - automate
# 1. Develop an API to accept bank deposits, withdrawl
# 2. Develop a script to extract information from excel sheet and insert that into the database. 
    
# csv file 

# s.no, firstname, lastname, email, phonenumber, is_graduated
