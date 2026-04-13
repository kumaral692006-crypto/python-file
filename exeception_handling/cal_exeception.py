try:
    x=int(input("enter first number"))
    y=int(input("enter second number"))
    print("choose operation:+,-,*,/")
    op=input("enter operator")

    if op =="+":
        print("result",x+y)
    elif op=="-":
        print("result",x+y)
    elif op=="*":
        print("result",x+y)
    elif op=="/":
        print("result",x/y)
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:                                                                                  
    print("enter a valid number")

else:
    print("no error occured while calculation")