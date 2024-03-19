class shape:
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
class triangle(shape): 
 def __init__(self, d1, d2,d3):
  self.d1=d1
  self.d2=d2
  self.d3=d3
 def area(self):
   area=self.d1*self.d2*0.5 
   print(f'area of a triangle:',area) 
 def perimeter(self):
    perimeter=self.d1+self.d2+self.d3
    print(f'perimeter of a triangle:',perimeter)
class rectangle(shape):
    def area(self):
        area=self.d1*self.d2
        print(f'area of a rectangle:',area)
    def perimeter(self):
        perimeter=2*(self.d1+self.d2)
        print(f'perimeter of rectangle:',perimeter) 
class ellipse(shape) :
    def area(self):
        area= 3.1416*self.d1*self.d2
        print(f'area of an ellipse',area)    
c=int(input("enter a length for rectangle:")) 
d=int(input("enter a width for rectangle:"))
tas=rectangle(c,d)
tas.area()
tas.perimeter()
f=int(input("enter a length of major axis for ellipse:"))
g=int(input("enter a length of minor axis for ellipse:"))     
m=ellipse(f,g)
m.area()
a=shape(1,2) 
print(a.d2)

b=triangle(1,2,3) 
b.area()
b.perimeter()


     

                     