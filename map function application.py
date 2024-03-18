def c_to_f(c):
    return ((9*c)/5)+32
c=[40,36,80,75,80]
a=list(map(c_to_f,c))
print(a)