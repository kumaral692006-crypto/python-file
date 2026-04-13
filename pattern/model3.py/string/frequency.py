f=input("enter your text")

max_char=""
max_count=0

for ch in f:
    count=f.count(ch)

    if count>max_count:
        max_count=count
        max_char=ch

print("most frequency character:",max_char)
