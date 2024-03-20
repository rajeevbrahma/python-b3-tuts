

account_data = {

    1234:{"balance":2326723,"name":"Mark"},
    1235:{"balance":2839,"name":"Bruno"},

}

class Atm:

    @staticmethod
    def convert_to_usd(money):
        return money/80

    def show_balance(self,ac_no):
        print (account_data[ac_no]["balance"])

    def show_balance_in_usd(self,ac_no):
        print (self.convert_to_usd(account_data[ac_no]["balance"]))

atm = Atm()
atm.show_balance(1234)
atm.show_balance(1235)
atm.show_balance_in_usd(1234)
print (atm.convert_to_usd(782372))
