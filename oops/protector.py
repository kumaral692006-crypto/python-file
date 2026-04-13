class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary

emp=employee("kumara",50000)
print(emp._salary)
class manager(employee):
    def show_salary(self):
        print(f"salary:{self._salary}")

mgr=manager("kumara",50000)
mgr.show_salary()