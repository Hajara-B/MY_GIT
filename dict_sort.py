my_dict={"name":"abc","place":"pqr","age":18,"college":"xyz"}
sort_ascend=dict(sorted(my_dict.items()))
print("The Sorted Dictionary in Ascending Order is",sort_ascend)
sort_descend=dict(sorted(my_dict.items(),reverse=True))
print("The Sorted Dictionary in Descending Order is",sort_descend)