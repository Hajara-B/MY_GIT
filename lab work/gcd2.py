a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if a>b:
    small=b
else:
    small=a
for i in range(small,0,-1):
    if a%i==0 and b%i==0:
        gcd=i
        break
print("the gcd of a and b is ",i)
    
    
    
    

    
      
      
