import csv
data = [
    {"Name":"Nandana","Age":20,"Gender":"Female"},
    {"Name":"Sana","Age":20,"Gender":"Female"},
    {"Name":"Hajara","Age":20,"Gender":"Female"}
]
file='dict.csv'
with open(file,'w')as store:
    writer=csv.DictWriter (store,fieldnames=['Name','Age','Gender'])
    writer.writeheader()
    writer.writerows(data)
with open(file,'r') as store:
 csv=csv.reader(store)
 for row in csv:
    print(row)
    