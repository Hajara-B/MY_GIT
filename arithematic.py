num1=int(input("enter a number: "))
num2=int(input("enter anothe number: "))

print("\n          Menu \n")
print("1. Addition")
print("2. Substration")
print("3. Multiplication")
print("4. Divition\n")

choice=int(input("enter the choice: "))

if choice==1:
    sum=num1+num2
    print(f"{num1} + {num2} = {sum}")
    
elif choice==2:
    sub=num1-num2
    print(f"{num1} - {num2} = {sub}")
    
elif choice==3:
    multi=num1*num2
    print(f"{num1} * {num2} = {multi}")
    
elif choice==4:
    div=num1/num2
    print(f"{num1} / {num2} = {div}")
    
else:
    print("invalid choice, try again")

    
