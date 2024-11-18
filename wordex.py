def exchange(a):
  
    if len(a)<2:
        print(a)
    else:
        print(a[-1]+a[1:-1]+a[0])
a=input("Enter a word")
s=exchange(a)
print(s)
