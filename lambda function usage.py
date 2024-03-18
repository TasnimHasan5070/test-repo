a=[("tasu",6),("prapty",5),("bravo",31),("zaum",24)]
a.sort()
print(a)
p=list(filter(lambda y:y[1]%2==0,a))
print(p)