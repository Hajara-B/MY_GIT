def swap(a,b):
   c=b[0]+a[1:]+a[0]+b[1:]
   return c
    


a=input("enter the first string: ")
b=input("enter the second string: ")
print("new str is ",swap(a,b))
