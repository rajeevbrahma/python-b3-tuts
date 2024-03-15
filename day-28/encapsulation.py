class Bank:

    def __init__(self):
        self.__secret_pin = None
        self.ac = None

    def __change_password(self):
        pass 

hdfcBank = Bank()
print (hdfcBank.ac)
# print (hdfcBank.__secret_pin) # it cannot accessible
print (hdfcBank._Bank__secret_pin)
