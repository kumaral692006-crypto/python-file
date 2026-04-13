import threading
def show_name():
    print(threading.current_thread().name)
t1=threading.Thread(target=show_name)
t2=threading.Thread(target=show_name)

t1.start()
t2.start()
t1.join()
t2.join()


print("program finished")

