class vechical:
    def start(self):
        print("vehical starting")
class car(vechical):
    def start(self):
        print("car engine starting")
v=vechical()
c=car()

v.start()
c.start()