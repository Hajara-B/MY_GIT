def exchange(n):
    if len(n)<2:
        print(n)
    else:
        b=n[-1]+n[1:-1]+n[0]
    return b

    
a=input("Enter the string: ")
print("the new string is: ",exchange(a))
