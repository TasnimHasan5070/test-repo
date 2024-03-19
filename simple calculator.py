num1=input(print("enter number1"))
num2=input(print("enter number2"))
operator=input(print("enter a operator"))
if(operator=="+"):
    print(int(num1)+int(num2))
elif(operator=="-"):
    print(int(num1)-int(num2))
elif(operator=="*"):
    print(int(num1)*int(num2))
elif(operator=="/"):
    print(int(num1)/int(num2))
else:
    print("you pressed a wrong key")