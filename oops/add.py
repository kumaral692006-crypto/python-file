class cart:
    def __init__(self):
        self.total=0
    def add(self,price):
        self.total+=price

    def show(self):
        print("total",self.total)

c=cart()
c.add(100)
c.add(200)
c.show()
