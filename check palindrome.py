def word(*strings):
    length=len(strings[0])
    i=0
    j=length-1
    while(i<j):
        if(strings[0][i]==strings[0][j]):
            print("palindrome")
            return
        i+=1
        j-=1
    else:
        print("not palindrome")
word("madam")        