class student:
    def __init__(self,name="unknow",mark=0):
        self.name=name
        self.mark=mark

s1=student()
s2=student("anu",88)
print(s1.name,s1.mark)
print(s2.name,s2.mark)