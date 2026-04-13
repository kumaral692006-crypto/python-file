import threading
import time 
def task():
    for i in range(3):
        print("running...")
        time.sleep(1)
t=threading.Thread(target=task)
t.start()
t.join()


print("this is the main program")