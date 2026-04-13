class booking:
    def __init__(self,price):
        self.price=price
    def __add__(self,other):
        return self.price+other.price

s1=booking(500)
s2=booking(900)
print("total cost",s1+s2)