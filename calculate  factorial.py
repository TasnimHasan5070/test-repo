def fact(*numbers):
    factorial=1
    for i in range(1,numbers[0]+1):
        factorial=i*factorial
    print(factorial)     
fact(4)     