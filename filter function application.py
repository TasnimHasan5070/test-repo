a=(input("enter some integers with space  for a list: "))
t=a.split(" ")
r=(list(filter(lambda x:int(x)%2==0,t)))
print(r)