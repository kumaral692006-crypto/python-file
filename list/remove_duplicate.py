x=[1,2,2,3,4,4,5]
p=[]
for i in x:
    if i not in p:
        p.append(i)
print(p)