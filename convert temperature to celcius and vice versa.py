a=(input("enter your command:"))           #enter c to f or f to c
if a == "f":
 b=float(input("enter celcius degree:"))
 fer=((9*b/5)+32)
 print(fer)
else:
 d=float(input("enter farenhite degree:"))   
 cel=(((d-32)*5)/9)
 print(cel)