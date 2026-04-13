x=[2,4,5,0,1,0]
d=[]
for i in x:
    if i!=0:
        d.append(i)
zero=x.count(0)
d+=[0]*zero
print(d)

        