try:
    op=2105
    att= 4
    while att>0:
        op=int(input("enter pin"))

        if att ==op:
            print("done go ")
            break 
        else:
            attemots=1
            print("wrong pin",att)
    if att==0:
        raise Exception("card blocked")
except ValueError:
    print("invalid ")
    if att==0:
      raise Exception("card blocked")