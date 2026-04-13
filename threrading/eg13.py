import threading
def square(n):
    for i in range (1,n+1):
        print(i*1)
num=int(input("enter a number"))
t1=threading.Thread(target=square,args=(num,)) 
t1.start()
t1.join()
print("program finished")