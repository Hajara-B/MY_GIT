original_list=[0,1,2,3,4,5,6,7,8,9]
new_list = []
for num in original_list:
    if num % 2 != 0:
        new_list.append(num)
print("New list without even numbers:", new_list)
