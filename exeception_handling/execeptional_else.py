try:
    num=int(input("enter number"))
    print(10/num)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print("no error accurred")