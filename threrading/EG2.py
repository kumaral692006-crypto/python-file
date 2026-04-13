import threading

def task1():
    print("thread 1 running")
def task2():
    print("thread 2 running")
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

print("this is the main program")
