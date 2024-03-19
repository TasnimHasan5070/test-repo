class Mathutils:
    def __init__(self,n):
        self.n=n
    def static(self):
        print(f'square={self.n*self.n}\n')
        if self.n==1:
            print("factorial 1")
        else:    
         a=list(range(1,self.n+1))
         c=1
         for i in a:
             c=i*c
         print(c) 
t=Mathutils(4)  
t.static()      
             
        
           