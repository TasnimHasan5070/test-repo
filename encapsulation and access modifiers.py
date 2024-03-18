class Bankaccount:
    def __init__(self):
     self.__account_numeber=12008276
     self.__balance=1000
     self.__deposit=0
    def deposit(self):
        a=int(input("enter your account_number:"))
        print("your total balance 1000")
        if a==self.__account_numeber:
            b=int(input("enter your deposit balance:"))
        print(f'your total balance:{b+self.__balance}')
        r= b+self.__balance
        self.__deposit=r
    def withdraw(self):
        c=int(input("enter your withdraw balance:"))
        print(f'after withdraw,your total balance:{self.__deposit-c}') 
         
d=Bankaccount()
d.deposit()
d.withdraw()

 
        
    