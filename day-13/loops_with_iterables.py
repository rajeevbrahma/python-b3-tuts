# loops - repetetive action 
# 1. definite loop
# 2. indefinite loop
# 3. loop through the iterables (str/list/tuple/dict/set)

# for - number based loops
# while - condition based loops

# looping through different iterables

var_1 = "abcdefghijklmnopqrstuv"

# char - is the temporary variable that holds the iterable value for that instance
for char in var_1:
    print (char)

var_2 = "123456789"
for num in var_2:
    print (num)

var_3 = [1,2,3,4,5,6]

for list_element in var_3:
    print (list_element)

var_4 = {1,2,3,4}
for set_element in var_4:
    print (set_element)

var_5 = (1,2,3,4)
for tuple_element in var_5:
    print (tuple_element)

var_6 = {'a':1,'b':2,'c':3}
for dict_element in var_6:
    print (dict_element)
    print (var_6[dict_element])

