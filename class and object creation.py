class car():
 def __init__(self,make,model,year) :
        self.make=make
        self.model=model
        self.year=year
 def display(self):
     print(f'This car made in {self.make}.\nmodel number:{self.model}.\nyear:{self.year}.\n') 
a=input("enter a new yer when toyota come with its new version:")      
t=car("japan",1201,2022) 
m=car("russia","24/A",a)
t.display() 
m.display()        