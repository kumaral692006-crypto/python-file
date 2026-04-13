class st:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

stu=st("arun",90)
print(stu.name)
print(stu.marks)

st.name="arun"
print(stu.name)
