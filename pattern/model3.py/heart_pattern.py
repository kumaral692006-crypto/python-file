for i in range(19):
    for j in range (20):

        if(i == 0 and j % 5 !=0)or\
          (i == 1 and j % 5 ==0)or\
          (i-j ==4)or\
          (i+ j ==18):
            print("0",end=" ")
        else:
            print(" ",end=" ")

    print()
        
    
       