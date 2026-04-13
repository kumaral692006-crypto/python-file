class father:
     def skills_father(self):
          print("father's skills:driving")
class mother:
     def skills_mother(self):
          print("mother's skills:cooking")
class child(father,mother):
     def skills_child(self):
          print("child's skills:coding")

c=child()
c.skills_father()
c.skills_mother()
c.skills_child()
          
     