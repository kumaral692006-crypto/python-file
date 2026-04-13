
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class ATM(Bank):
    def withdraw(self, amount):
        print("Withdraw from ATM:", amount)

class Online(Bank):
    def withdraw(self, amount):
        print("Withdraw using Online Banking:", amount)

class CashCounter(Bank):
    def withdraw(self, amount):
        print("Withdraw from Bank Counter:", amount)


# object creation
a = ATM()
a.withdraw(1000)

b = Online()
b.withdraw(2000)

c = CashCounter()
c.withdraw(500)