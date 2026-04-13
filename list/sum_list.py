q=[2,5,8,9,3]
tar=11
for i in range(len(q)):
    for j in range(i+1,len(q)):
        if q[i]+q[j]==tar:
            print({i,j})
