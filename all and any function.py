x=[1,2,3,6,8,9,0]
t=(i%2==0 for i in x )
print(any(list(t)))

m=(i>0 and i<5 for i in x)
print(all((m)))


