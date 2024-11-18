a=input("enter your word: ")



if a[:-3]=="ing":
    a+="ily"
    
elif a[:-3]=="ly":
    a+="ing"


print(a)
