from functools import partial
def volume(x,y,z):
    return x*y*z
a=partial(volume,5)
print(a(6,7))