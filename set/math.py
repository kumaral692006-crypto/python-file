#union 
w={2,3,4,5}
p={1,5,6,7,8}
q=w.union(p)
print(q)

#intersection
a={2,4,3,5}
b={2,4,1,6}
c=a.intersection(b)
print(c)

#difference
d={1,3,5,6}
e={1,3,2,4,5}
f=d.difference(e)
print(f)

#symentric 
g={9,8,7,6}
h={8,9,10,11}
i=g.symmetric_difference(h)
print(i)