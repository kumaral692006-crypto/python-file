class bank:
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance
    def show_info(self):
        print(f"name :{self.accountnumber},age:{self.balance}")

class savingaccount(bank):
    def __init__(self,accountnumber,balance,interest):
        super().__init__(accountnumber,balance)
        self.interest=interest
    def show_savingaccount_info(self):
        print(f"accountnumber:{self.accountnumber},balance{self.balance},interest:{self.interest}")
acc=savingaccount(123456798,25000,6)
acc.show_info()
acc.show_savingaccount_info()
