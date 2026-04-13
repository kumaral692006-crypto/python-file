class person:
    def greet_person(self):
        print("name:kumara")

class employee(person):
    def greet_employee(self):
        print("salary: 1000000")

class manager(employee):
    def greet_manager(self):
        print("deparment: BME")

c=manager()
c.greet_person()
c.greet_employee()
c.greet_manager()