a=input("enter a file name:")
try:
 z=open(a,"r")
except FileNotFoundError:
 print("file doesnot exist")
else:
   print("file already exist")
try:
  p=open("first programming.txt","r")
except IOError:
    print("file has already open in another python file")
else:
  print("file opened successfully")
      
  