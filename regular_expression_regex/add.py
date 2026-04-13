import re

text="ab acb abdb"
result=re.findall("a+b",text)
print(result)