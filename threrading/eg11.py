import threading 

def task1():
    print("iam playing circket")
def task2():
    print("i had done my work ")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()
t1.join()
t2.join()

print("task done")


