class technical:
     def coding (self):
          print("technical skills:codiung")
class non_technical:
     def non_technical(self):
          print("non_technical skills:project managment")
class employee(technical ,non_technical):
     def __init__(self,name):
          self.name=name
     def show_name(self):
          print(f"employee name:{self.name}")


emp=employee("gokul")
emp.show_name()
emp.coding()
emp.non_technical()
          
     