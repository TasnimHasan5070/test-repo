def paybill():
    b=["electricity","water","internet","gas"]
    print("you can pay utility bill,such as:",b)
    print(input(("choose one:")))
    a=int(input("enter your bill amount:"))   
    d=1000-a
    print("after payment your present amount",d)