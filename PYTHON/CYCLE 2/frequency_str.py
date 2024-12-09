def frequency():
    word=input("enter your word: ")
    letter=input("enter the letter: ")
    new=len(word)
    count=0
    for i in range(new):
        if word[i]==letter:
           count+=1
    print(f"the count of the letter {letter} is {count}")         
frequency()    