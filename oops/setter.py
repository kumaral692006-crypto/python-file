class stu:
    def __init__(self,name,mark):
        self._name=name
        self._mark=mark

    def get_marks(self):
        return self._mark
    
    def set_mark(self,mark):
        if 0<=mark <=100:
            self._mark=mark
        else:
            print("invalid mark")

stud=stu("kumara",99)
stud.set_mark(105)
stud.set_mark(90)
print(stud.get_mark())
