class student:
    def __init__(self,mark):
        self.mark=mark
    def __add__(self,other):
        return self.mark+other.mark

s1= student (80)
s2=student(90)
print("total marks",s1+s2)