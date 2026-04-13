a=input("enter the word")

upper=0
lower=0
digit=0
special=0

for ch in a:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
          special+=1
        
print("upper case:",upper)
print("lower case:",lower)
print("digit case:",digit)
print("spical case:",special)

