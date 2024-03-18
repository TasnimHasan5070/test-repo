from itertools import chain
a=[1,3,45,6]
b=["a","b","c","d","r","t","m"]
t=chain(a,b)
m=list(t)
print(m)
for i in m:
    print(i)