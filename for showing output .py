x=open("first programming.txt",'r')
y=open("for showing output.txt",'w')
y.write(x.read())
x.close()
y.close()
a=input("enter a file name:")
try:
 z=open(a,"r")
except FileNotFoundError:
 print("file doesnot exist")
else:
   print("file already exist")


