x=[3,4,5,6,8,2]
max=x[0]
min=x[0]

for z in x:
    if z>max:
        max=z

    elif z<min:
        min=z

print(max)
print(min)