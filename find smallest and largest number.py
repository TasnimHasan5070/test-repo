number1=input(print("enter number1:"))
number2=input(print("enter number2:"))
number3=input(print("enter number3:"))
if(int(number1)>int(number2)>int(number3)):
 print("number1 is the largest number and number3 is the smallest number")
elif((int(number2)>int(number3))>int(number1)):
    print("number2 is the largest number")
else:
    print("number3 is the largest number")