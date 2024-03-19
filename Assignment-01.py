item_name=['laptop','headphones','keyboard','mouse']
item_quantities=[10,20,15,30]
item_price=[68000,500,800,300]
items={
 "name1": item_name[0],
 "price1":str(item_price[0]),
 "quantities1":str(item_quantities[0]),
 "name2":item_name[1],
 "price2":str(item_price[1]),
  "quantities2":str(item_quantities[1]),  
  "name3": item_name[2],  
   "price3":str(item_price[2]), 
     "quantities3":str(item_quantities[2]),
     "name4": item_name[3],  
   "price4":str(item_price[3]), 
     "quantities4":str(item_quantities[3]) 
    }
x=f"product name:{items['name1']}.\nprice:{items['price1']} per set.\nquantities:{items['quantities1']} piece.\n"
y=f"product name:{items['name2']}.\nprice:{items['price2']} per set.\nquantities:{items['quantities2']} piece.\n"
z=f"product name:{items['name3']}.\nprice:{items['price3']} per set.\nquantities:{items['quantities3']} piece.\n"
a=f"product name:{items['name4']}.\nprice:{items['price4']} per set.\nquantities:{items['quantities4']} piece.\n"
print("view inventory:\n", x)  
print(y) 
print (z)                      
print(a)         
sum=0
for i in item_price: 
 sum=sum+i
print("total cost of present list:",sum)         
new=input("add any new items and its quantity in bracket:") 
item_name.insert(4,new)   
print("updated list:\n",item_name) 
remove=input("enter the item which you want to remove from the list:")    
item_index=item_name.index(remove)  
item_name.pop(item_index)
print("new list:\n",item_name )
'''sum=0
for i in item_price: 
 sum=sum+i
print("total cost of present list:",sum)'''
buyingitem=input("choose a item for buy:") 
buying_item_price=int(input("enter the buying item price:"))
item_name.remove(buyingitem)
item_price.remove(buying_item_price)
print("new inventory:/n",item_name)
sum1=0
for i in item_price:
  sum1=sum1+i
print("total cost of new list:",sum1)
                                                             