import threading
a=int(input("enter ur number"))
def task():
    print(a**2)
t=threading.Thread(target=task) 
t.start()
print("program finished")
