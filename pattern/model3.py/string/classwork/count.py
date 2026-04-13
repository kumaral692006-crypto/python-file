o=input("enter a sentence")
count={}
for cha in o:
    if cha in count:
        count[cha] +=1
    else:
        count[cha]=1
    
print("characters occures:")
for cha, count in count .items():
     print(f"{cha}: {count}")
        

