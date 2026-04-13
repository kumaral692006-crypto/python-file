def constant_time(arr):
    print("\nO(1)-constant time example")

    if len(arr)>0:
        print("first element:",arr[0])
    else:
        print("array is empty")
arr=list(map(int,input("enter element sepereated")))
constant_time(arr)
