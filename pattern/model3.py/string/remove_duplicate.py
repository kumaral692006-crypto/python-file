w=input("enter ur word")
b= ""
for ch in w:
    if ch not in b:
           b += ch
print(b)