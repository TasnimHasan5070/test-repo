phrase=input("enter a string:")
length=len(phrase)
i=0
j=length-1
while i<j:
        if(phrase[i])==(phrase[j]):
            print("palindrome")
            break
        else:
            print("not palindrome")
            break
                   