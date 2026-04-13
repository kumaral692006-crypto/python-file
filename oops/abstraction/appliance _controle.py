from abc import ABC, abstractmethod

class appliance(ABC):
    @abstractmethod
    def start(self):
        pass

class fan(appliance):
    def start (self):
        print("fan turn on")

class ac(appliance):
    def start (self):
        print("ac is on ")
 
class washingmachine(appliance):
    def start (self):
        print("washingmachine trun on")

s=fan()
s.start()

c=ac()
c.start()

d=washingmachine()
d.start()