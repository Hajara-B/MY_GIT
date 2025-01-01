import csv
def csv_column(file,column):
    with open(file,'r') as store:
         csv_readers=csv.reader(store)
         for row in csv_readers:
              columns=[row[i] for i in column]
              print(columns)
column_input = input("Enter the column indices ")
column = [int(i) for i in column_input.split(',')]
file="column.csv"
csv_column(file,column)