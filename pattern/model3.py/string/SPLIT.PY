T=input("enter ur word")
y=T.split()
longest=""
for v in y:
    if len(v)>len(longest):
        longest=v
print(v)

