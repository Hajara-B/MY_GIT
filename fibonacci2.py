def fibno(n):
    a,b = 0,1
    for i in range(n):
        print(a)
        a,b = b,a+b
c=int(input("enter the limit: "))
fibno(c)
