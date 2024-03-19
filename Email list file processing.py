x=open("emails.txt","r")
p=x.readlines()
print(p)
invalid=[]
valid=[]
for i in p:
 if "@" in i:  
  valid.append(i)
else:
   invalid.append(i)
print("invalid emails are:" ,invalid)
print("valid emails are:",valid)
z=open("valid_emails.txt",'w')
for k in valid: 
 z.write(k)
r=open("inavalid_emails.txt",'w')
for t in invalid:
 r.write(t)
  
 




