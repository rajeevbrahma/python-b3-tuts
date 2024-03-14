

class Atm:
    def __init__(self,ac,pin):
        self.__pin = pin 
        self.ac = ac 

    def __change_pin(self,pin):
        pass


atm = Atm(1,123)
print (atm.ac)
print (atm._Atm__pin)

# print (atm.__pin)