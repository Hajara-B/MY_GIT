details={"a":"ee","b":"uu","c":"yy","d":"oo"}
dict1=dict(sorted(details.items()))
      
print("ascending order of the details is: ",dict1)
dict2=dict(sorted(details.items(),reverse=True))


print("descending order of the details is: ",dict2)
            
