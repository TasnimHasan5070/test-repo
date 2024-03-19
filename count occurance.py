def count(*numbers):
   i=0
   length=len((numbers))
   j=length-1
   count=0
   while(i<j):
      if(numbers[i]==numbers[j]):
         print(numbers[i],numbers[j])
         count+=1
      i+=1
      j-=1
count(1,4,7,1,9)
print(count())
                               