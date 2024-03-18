from functools import reduce
p=[1,3,4,5,6,7]
x=reduce(lambda a,b:a*b,p)
print(x)
def mul(a,b):
    return a*b
r=reduce(mul,p)
print(r)

