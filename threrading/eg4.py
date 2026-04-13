import threading
def print_numbers():
    for i in range(1,6):
        print(i)

t1=threading.Thread(target=print_numbers)
t1.start()
t1.join()
print("thread finished")
