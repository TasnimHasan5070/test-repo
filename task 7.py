from user_information import user_information
from send_money import send_money
from payment import payment
from cashout import cashout
from pay_bill import paybill
from my_bkash import my_bkash
def command():
   x="1.send money\n2.payment\n3.cashout\n4.paybill\n5.mybkash\n" 
   return x
x=command()
print(x)
user_information()
user_choice=int(input("enter your command:"))
if(user_choice==1):
   send_money()  
elif(user_choice==2):
   payment()
elif(user_choice==3):
   cashout()
elif(user_choice==4):
   paybill()
elif(user_choice==5):
   my_bkash()
else:
   print("you have pressed a wrong key")