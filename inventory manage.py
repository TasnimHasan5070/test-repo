def load_inventory(**details):
    print(details)
name=["cpmputer","laptop","mobile"]
prize=[5000,67000,700]
load_inventory(**dict(zip(name,prize)))

def add_product(name): 
    items=[input("enter your need:")]
    name.extend(items)

lst=[]  
add_product(lst) 
print(lst)

 
    