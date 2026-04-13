class person:
    def detail(self):
        print("person detail")
class employee(person):
    def details(self):
        print("employee detail")

class manager(employee):
    def details(self):
        print("manager details")

p=person()
e=employee()
m=manager()
p.details()
e.details()
m.details()