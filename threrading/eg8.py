import threading 
import time 

def fast():
    for i in range(3):
        print("fast thread")
        time.sleep(1)
def slow():
    for i in range(3):
        print("slow thread")

t1=threading.Thread(target=fast)
t2=threading.Thread(target=slow)
t1.start()
t2.start()
t1.join()
t2.join()