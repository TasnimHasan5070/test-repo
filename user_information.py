def user_information():
    info={
        "name":"tasnim hasan",
        "phone number":"123",
        "password":"123"
    }
    y=[input("1.enter your name:"),input("2.enter phone number:"),input("3.enter password:")]
    for i in y:
      if  i not in info.values():
         return info  
    print("your balance:10000")

      
