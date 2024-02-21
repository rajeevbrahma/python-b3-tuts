list_1 = []
dict_1 = {}
try:
    # int("hello")      # ValueError
    # print (list_1[1]) # IndexError
    # print (5 + "")     # TypeError
    # print (hello)       # NameError
    # print (5/0)         # ZeroDivisionError
    # print (dict_1["a"]) # KeyError
    import rohit        # ImportError
except ImportError:
    print ("Module not found")
except KeyError:
    print ("Dictionary key not exists")
except ZeroDivisionError:
    print ("Operation will result infinity")
except TypeError:
    print ("Invalid data type")
except NameError:
    print ("Identifier name is not defined")
except IndexError:
    print ("Index out of range")
except ValueError:
    print ("Invalid literal value")
except Exception as error:
    print (error)
    print (type(error))

# exercise 
    
# take input from the user and put in a list then add that to a dictionary element

# a + b / c 
numerator_operands = {'a':4,'b':4,'c':5,'d':6}
denominator_operand = [2,1,3,'1','5']

print (numerator_operands)
print (denominator_operand)


def equation():

    try:
        numerator_choice_1 = input("give a numerator choice  - ")
        numerator_choice_2 = input("give a numerator choice 2  - ")
        list_index = int(input("Give a list index of the denominator value  - "))
        print (numerator_operands[numerator_choice_1])
        print (numerator_operands[numerator_choice_1])
        print (denominator_operand[list_index])

        result = (numerator_operands[numerator_choice_1] + 
                numerator_operands[numerator_choice_2]) / denominator_operand[list_index]
        print (result)

    except IndexError:
        print ("You have given a value which is beyond the lenght of the list")
        equation()
    except KeyError:
        print ("You are trying to access the key which is not defined yet")
        equation()
    except TypeError:
        print ("You are considering invalid datatypes")
        equation()
    except Exception as e:
        print ("General exceptino")
        print (type(e))
        print (e)

equation()


