import re
t="i have 200 apples and i have 5 bannanas.My friend have 7 mangos"
result=re.findall(r"(have)",t)
print(result)

