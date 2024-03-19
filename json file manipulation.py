x=open("data.json","r")
x.close()
a=input("enter new element for stock:")
data["stock"]=["keyboard","headphone","a"]
y=open("data.json","w")
y.close()
for k in data:
    y.write(k)

