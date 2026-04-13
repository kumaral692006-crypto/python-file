class person:
    def greet():
        print("hello from kumara")

class student(person):
    def study(self):
        print ("student is studing")

class employee(person):
    def work(self):
        print("employee is working")
    
s=student()
c=employee()
s.greet()
c.study()