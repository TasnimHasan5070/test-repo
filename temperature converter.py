c=input(print("enter celcius temperature:"))
f=input(print("enter farenhite temperature"))
l=input(print("enter conversion statement:"))
if(l=="celciustofarenhite"):
 celcius_to_farenhite=((int(f)-32)*5)/9
 print(celcius_to_farenhite)
elif(l=="farenhitetocelcius"):
 farenhite_to_celcius=(((int(c)*9)+32))/5
 print(farenhite_to_celcius)
else:
 print("enter celciustofarenhite statement  or farenhitetocelcius statement")
    