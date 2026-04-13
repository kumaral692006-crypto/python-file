class device:
    def power(self):
        print("the charge is at 89")

class laptop(device):
    def coding (self):
        print("hp")

class phone(device):
    def call (self):
        print("oppo")

l=laptop()
p= phone()
l.power()
l.coding()
p.power()
p.call()
