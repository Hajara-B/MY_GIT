def fact():
    num=int(input("Enter your number: "))
    fact=num*fact(num-1)
    if num==0 and num==1:
        return 1
    else:
        return fact()
    
