import re
text="kumaravel"
r=re.findall(r"0[^a,e,i,o,u]",text)
print(r)