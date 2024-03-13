
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
                # exercise - extract the characters
        return vowel_count_var,vowel_characters
    
    # method
    def consonant_count(self):
        """ consonant count method """
        pass


a = String("hello world") # object intialization  , argument
print (a.vowel_count())
print (a.word)
print (a.CAP_VOWELS)
   
b = String("Rohith") # object intialization
print (b.vowel_count())
print (b.word)
print (a.CAP_VOWELS)

c = String("Beulah") # object intialization
print (c.vowel_count())
print (c.word)
print (a.CAP_VOWELS)