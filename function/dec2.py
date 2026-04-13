def dec(fun):
    def wrap(name):
        print("before exe")
        fun(name)
        print("after exe")
    return wrap

@dec
def greet(name):
    print(f"hello{name}")

greet("kumara")