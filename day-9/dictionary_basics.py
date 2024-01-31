# Dictionary Basics
# We can store multiple values of various datatypes in a dictionary. 
# We can access the values using the keys. Dictionaries are mutable.

# We can store the data in key value pairs.They are changeable and duplicates are not allowed
#     example :{
#         key:value
#     }
#     "key"   - allowed data types : numbers,strings
#     "value" - allowed data types : numbers,strings,lists,dictionaries,boolean,set,tuple,none

#     A Dictionary will have 
#             word : and its respective meaning

#     Like the same way dictioinaries in Python will be have 
#         key_name : and its associated value

#     How can we relate dictionaries with List

#     In list we associate list elements with the index and dictionaries we associate
#     dictionary values with keys.

#     In list we are accessing list elements with its respective index number
#     In dictionary we can access values with its respective key name

#    Symbol ":" (colon) will be used to seperate key and its value

#    In List we seperate each element with symbol ","(comma) In the same way we 
#    seperate dictionary elements using same symbol "," (comma) 
  
#   List Example:
#         ["Eric","Clapton",78,'30 Mar']
#             0       1      2    3
#         {
#             "first_name":"Eric",
#             "last_name":"Clapton",
#             "age":78,
#             "dob":"30 Mar"
#         }


# details = [["X",23,32423.23,True]
#  .
#  .
#  .
#  ]

# {
#     "name":"x",
#     "age":23,
#     "salary":234234.4
#     "is_married":True
# }

# create dictionary

dict1 = {1:'a'} # dictionary definition
dict2 = {1:'a',2:'b'}
dict3 = {'a':'A','b':'B'}
list1 = [1,2,3,4]
dict4 = {0:1,1:2,2:3,3:4}

print (list1[2])
print (dict4[2])
print (dict3['b'])

# bank details xy finances
# 5 customers 
# i want to store those 5 customer details in a dictinary
# name, date of birth, salary, address, family details, is_insured
customer1 = ["x","01-01-1990",232343.2,[3,"a street","c city"],["father a","mother m"],True]
customer2 = ["x","01-01-1992",232343.2,[3,"a street","c city"],["father a","mother m"],True]
customer3 = ["x","01-01-1993",232343.2,[3,"a street","c city"],["father a","mother m"],True]
customer4 = ["x","01-01-1994",232343.2,[3,"a street","c city"],["father a","mother m"],True]
customer5 = ["x","01-01-1995",232343.2,[3,"a street","c city"],["father a","mother m"],True]

# example for defining list of lists
xy_finances_bank_customer_details = [customer1,customer2,customer3,customer4,customer5]

customer1 = {
    "name":"Rohan",
    "dob":"01-01-1990",
    "salary" : 23849234.23,
    "address":{
        "d_no":45,
        "street":"ak street",
        "city":"My city"
    },
    "is_insured":True
}

addrs = "address"
customer2 = {
    "name":"Roshan",
    "dob":"01-01-1991",
    "salary" : 8923892.23,
    "balane" : 200,
    addrs:{
        "d_no":46,
        "street":"ak street",
        "city":"My city"
    },
    "is_insured":True,
    # captures only credit or debit
    # account activity - type, date, amounts
    # all the account activities are grouped together in a list
    # the following is called as list of dictionaries
    "recent_account_activity":[
        {
            "type":"debit",
            "date":"01-22-2024",                                # - 0  
            "amount":200,
            "same_bank":False
        }, # each activity is stored in the dictionary format
        {
            "type":"credit",
            "date":"01-21-2024",
            "amount":400,                                       # - 1
            "same_bank":True
        }, # each activity is stored in the dictionary format
    ]
}

xy_bank_account_details = {
    982001:customer1,
    982002:customer2
}
# access customer 2
print (xy_bank_account_details[982002])
# access customer 1 address
# print (xy_bank_account_details[982001][addrs]["city"])

# customer 2 recent activity
print (xy_bank_account_details[982002]["recent_account_activity"])
print (type(xy_bank_account_details[982002]["recent_account_activity"]))
print (xy_bank_account_details[982002]["recent_account_activity"][0])
print (type(xy_bank_account_details[982002]["recent_account_activity"][0]))
print (xy_bank_account_details[982002]["recent_account_activity"][1])
print (type(xy_bank_account_details[982002]["recent_account_activity"][0]["amount"]))


