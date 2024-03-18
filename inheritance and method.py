class shape():
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2
class rectangle(shape):
    def area(self):
        area=self.d1*self.d2
        print(f'area of a rectangle:',area)
    def perimeter(self):
        perimeter=2*(self.d1+self.d2)
        print(f'perimeter of rectangle:',perimeter) 
class circle(shape):
    def area(self):
        area=3.1416*self.d1*self.d1
        print(f'area of circle:',area) 
    def perimeter(self):
        perimeter=2*3.1416*self.d1
        print(f'perimeter of a circle :',perimeter)
s=int(input("enter width value of rectangle: ")) 
t=int(input("enter length value of rectangle:"))  
p=int(input("enter radius value:"))     
a=rectangle(s,t) 
a.area() 
a.perimeter()
b=circle(p,p)
b.area()                
b.perimeter()
          