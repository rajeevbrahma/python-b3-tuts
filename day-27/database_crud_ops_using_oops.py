
# Inheritance (Multilevel, Multiple)
# Encapsulation  - when you want to restrict the access / view of attributes and methods
# your class.
# Abstraction

# Polymorphism 

# create a simple CRUD class (blueprint)

# class Mysql:
    
    # create document
    # print ("creating a document")
    # store in a dictionary
    # read document 
    # read all document
    # update document
    # delete document
# -------------
# s.no name age
# -------------
#     |    |   |
#     |    |   |
#     |    |   |
#     |    |   |

# {
#    1: {"s.no":1,"name":None,"age":None}
#    2: {"s.no":2,"name":None,"age":None}
#    3: {"s.no":3,"name":None,"age":None}
# }

# # database
# {   
    
#     # table child_data
#     "child_data":{
#         # documents / rows
#         1: {'s.no': 1, 'name': 'Mark', 'age': 3},   
#         2: {'s.no': 2, 'name': 'John', 'age': 4}, 
#         3: {'s.no': 3, 'name': 'Jean', 'age': 2}
#     },
#     # table adult_data
#     "adult_data":{
#         # documents / rows
#         1: {'s.no': 1, 'name': 'Mark', 'age': 3,'is_graduated':None}, 
#         2: {'s.no': 2, 'name': 'John', 'age': 4,'is_graduated':None}, 
#         3: {'s.no': 3, 'name': 'Jean', 'age': 2,'is_graduated':None}
#     }

# }

# system memory
mac_rb = {
            # database mysql_v1
            "mysql_v1" : {
                "auth":{"username":"admin","password":"admin@123"},
                # "child_data":{},
                # "adult_data":{}
                },
            # database mysql_v2
            "mysql_v2" :{
                "auth":{"username":"admin","password":"admin@321"}
                },
            # database mysql_v3
            "mysql_v3" :{
                "auth":{"username":"admin","password":"admin@231"}
                }
        }

class Mysql:

    # - this method will be called by default on initialization your object
    def __init__(self,db_name,username,password): # constructor
        # instance variables
        self.db_name = db_name
        self.database = mac_rb[self.db_name]

        # hidden / privates variables (encapsulation)
        self.__username = username
        self.__password = password

    # hidden / private method (encapsulation)
    def __change_password(self,password):
        self.database["auth"]["password"] = password
        return True
    
    def change_password(self,password,newpassword):
        """ change password """
        if self.database["auth"]["password"] == password:
            self.__change_password(newpassword)
        return "Wrong password"      

    def authenticate(self):
        """ authenticate """
        print (self.__username,self.__password)
        if (self.database["auth"]["username"] == self.__username) and (self.database["auth"]["password"] == self.__password):
            return True
        return False

    # create method
    def create(self,document):
        """ create """
        self.database.update({document["s.no"]:document})
        return document

    # read method
    def read(self,doc_id):
        """ read """
        return self.database.get(doc_id)

    # update method
    def update(self,doc_id,update_key_value_pair):
        """ update """
        self.database[doc_id].update(update_key_value_pair)
        return self.database[doc_id]
    
    # delete method
    def delete(self,doc_id):
        """ delete """
        del self.database[doc_id]
        return True  
    
    def read_all(self):
        """ read all """
        return self.database

mysql = Mysql("mysql_v2","admin","admin@3212")
print (mysql.authenticate())

print (mysql.change_password("admin@32","pass"))

print (mac_rb)


# encapsulation in python
# Nothing in Python Truly remains private with a small tweak we can access the hidden data

# The following line will throw an error
# print (mysql.__username) # attribute error, uncomment to see the error

# If you do tweak it like the follwing
print (mysql._Mysql__username)
print (mysql._Mysql__password) # you will still be able to access the hidden files
# This is how python is built and this justifies what i said that Python really 
# doesnt exibhit the true Private / hidden behaviour






# print (mysql)

# mysql.create({"s.no":1,"name":"Mark","age":3})
# mysql.create({"s.no":2,"name":"John","age":4})
# mysql.create({"s.no":3,"name":"Jean","age":2})

# print (mysql.read_all())
# print (mysql.read(1))
# print (mysql.delete(1))
# print (mysql.update(2,{"name":"Steve"}))
# print (mysql.read_all())






