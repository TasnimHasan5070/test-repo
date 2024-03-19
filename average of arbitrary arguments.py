def ave(*numbers):
   sum=0
   a=len(numbers)
   for i in numbers:
       sum=sum+i
       average=sum/a
   print(average) 
ave(1,2,3,4)     
       