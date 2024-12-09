def fact(n):
    if n>1:
        factorial=n*fact(n-1)
        return factorial
    elif n==0 or n==1:
        return 1

a=int(input("enter a number: "))
print(f"the factorial of {a} is ",fact(a))
