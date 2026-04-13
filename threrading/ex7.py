import threading

def greet(name):
    print("hello",name)

t1=threading.Thread(target=greet,args=("lily",))

t1.start()
t1.join()

print("program finished")