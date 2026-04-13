class person:
    def greet(self):
        print("hello from person")

class student(person):
    def study (self):
        print("student is studying")

class employee(person):
    def work(self):
        print("employee is working")

class intern(student,employee):
    def intern_task(self):
        print("intern is doing assigned task")

a= student()
b=employee()
a.greet()
b.greet()
a.study()
b.work()
