""" Dictionary methods """

# Dictionary methods
# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and value
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair

# Dictionary intialization
#1 . Using curly braces
example_dictionary = {
    "name":"Jonh",
    "age":23,
    "country":"UK"
}


print (example_dictionary["name"])
print (example_dictionary.get("name")) # get method

a = {1:1,2:2}
print (a.get(1))

print (example_dictionary.keys())
print (example_dictionary.values())

# updating dictionary / dictionary element
example_dictionary["name"] = "John"
print (example_dictionary)

example_dictionary.update({"name":"John S"})
print (example_dictionary)

example_dictionary.update({
    "address":{
        'house_number': '#342', 
        'city': 'City', 
        'state': 'State'
    },
    "contact":2384792374
})
print (example_dictionary)

# output - {
#  'name': 'John S', 
#  'age': 23, 
#  'country': 'UK', 
#  'address': {
#         'house_number': '#342', 
#         'city': 'City', 
#         'state': 'State'
#         }, 
#   'contact': 2384792374
# }

print (example_dictionary["address"]["city"])
example_dictionary["address"].update({
    'city':"X"
})
print (example_dictionary)

# pop() - Removes the element with the specified key
example_dictionary.pop("contact")
print (example_dictionary)

example_dictionary["address"].pop("state")
print (example_dictionary)

# example_dictionary.update({"1":"2"})
# print (example_dictionary)

# popitem() - Removes the last inserted key-value pair
example_dictionary.popitem()
print (example_dictionary)

example_dictionary_2 = dict.fromkeys([1,2,3])
print (example_dictionary_2)

example_dictionary_2 = dict.fromkeys(["name","age","country"]) # by default your values is None
print (example_dictionary_2)

example_dictionary_2 = dict.fromkeys(("name","age","country"),"x")
print (example_dictionary_2)

example_dictionary_2 = dict.fromkeys("hello",1)
print (example_dictionary_2)

example_dictionary_3 = {"1":1,"2":2}

# setdefault() - 
# Returns the value of the specified key. 
# If the key does not exist: insert the key, with the specified value

example_dictionary_3.setdefault("3")
print (example_dictionary_3)

example_dictionary_3.setdefault("4","Four")
print (example_dictionary_3)

print (example_dictionary_3.setdefault("4",6))
print (example_dictionary_3)

