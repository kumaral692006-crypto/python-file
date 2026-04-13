import threading

def task1():
    print("thread  1 running")
t1=threading.Thread(target=task1)
t1.start()
print("this is the main program")