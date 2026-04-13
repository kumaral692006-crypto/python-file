class dog:
    def __init__(self):
        print("dog braks")
class cat:
    def __init__(self):
        print("cat meow")

def make_sound(obj):
    obj.sound()


d=dog()
c=cat()
make_sound(d)
make_sound(c)


    