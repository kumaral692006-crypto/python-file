import threading 

def check_even(n):
    if n%2==0:
        print("even number")
    else:
        print('odd number')

num=int(input("enter ur number"))
t1=threading.Thread(target=check_even,args=(num,)) 
t1.start()
t1.join()
print("program finished")