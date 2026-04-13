class bank:
    def __init__(self,name,balance):
        self._name= name 
        self._balance=balance

acc = bank("kumara",1000)
class bank:
    def __init__(self,name,balance):
        self._name= name 
        self._balance=balance

    def get_balance(self):
        return self._balance
    def get_name(self):
        return self._name
    
acc=bank("kumara",10000000)
print(acc.get_balance())
print(acc.get_name())