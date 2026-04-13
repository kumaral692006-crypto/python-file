class animal:
    def eat(self):
        print("animal eat meat")

class lion(animal):
    def roars(self):
        print ("the lion roars")

class dog(animal):
    def  wowww(self):
        print("the dog wowwww")
    
s=lion()
c=dog()
s.eat()
s.roars()
c.wowww()
c.eat()