a=int((input("enter a number:")))
p=str(a)
if (p[0:])==(p[::-1]):
    print(True)
else:
    print(False)    