from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def start(seelf):
        pass

class upi(payment):
    def start (self):
        print("mode of payment")

class creditcard(payment):
    def start (self):
        print("mode of payment: creditcard")
 
class debitcard(payment):
    def start (self):
        print("mode of payment: debitcard ")

s=upi()
s.start()

c=creditcard()
c.start()

d=debitcard()
d.start()