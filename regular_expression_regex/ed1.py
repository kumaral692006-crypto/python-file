import re

text ="spider man homecoming peter "
pattern="peter"

result=re.search(pattern,text)

if re:
    print("match found")
else:
    print("match not found")


