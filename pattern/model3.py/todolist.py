tasks=[]

while True:
    print("\n 1.add task ")
    print("2.view task")
    print("3.exit")

    choice=input("enter choice")

    if choice =="1":
       task = input("enter task")
       tasks.append(task)
       print("task added")
    
    elif choice == "2":
       print("your tasks :")
       for t in tasks:
          print("-",t)

    elif choice=="3":
       break

    else:
       print("not an proper input : ")


         