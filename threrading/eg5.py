import threading

def number ():
    for i in range(1,6):
        print("number",i)
def letter():
    for c in ['A','B','C','D','E']:
        print("letter",c)

t1=threading.Thread(target=number)
t2=threading.Thread(target=letter)

t1.start()
t2.start()
t1.join()
t2.join()

print("this is the main program")