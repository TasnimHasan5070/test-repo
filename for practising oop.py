class elements():
    def __init__(self,name,cost,quantity):
        self.electronics=name
        self.bag=cost
        self.kg=quantity
    def office(self):
        print(f'i want {self.electronics}\nits prize is {self.bag}\ni need {self.kg} pieces.\n')  
t=elements("AC",278000,7)    
t.office()    
print(t.electronics)