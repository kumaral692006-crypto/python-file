def dec(fun):
    def wrap():
        print("before exe")
        fun()
        print("after exe")
    return wrap

def greet():
    print("hello!")
greet= dec(greet)
greet()