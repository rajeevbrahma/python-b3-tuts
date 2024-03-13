
class Atm:  # This is Atm class
    """ This is a Atm Blueprint class """
    def __init__(self,arg_name):  # special / magic / dunder method / constructor
        self.atm_name = arg_name  # property / attribute, instance variable
        # self.__pin = None
        # self.__balance = None

    def withdraw(self):  # methods / behaviour definition
        """ withdraw """
        print ("You have selected Withdraw operation")

    def deposit(self):  # method / behaviour definition
        """ deposit """
        print ("You have selected deposit operation")

    def check_balnce(self):
        """ check blanace"""
        print ("You have selected check balance operation")

class HdfcAtm(Atm):
    
    def card_to_card_transfer(self):
        """ card to card transfer """
        print ("You have selected card to card transfer")



atm = Atm()
hdfcAtm = HdfcAtm()

