import csv

def read_csv_file(file):
    with open(file, 'r') as store:
        csv_reader = csv.reader(store)
        for row in csv_reader:
            print(row)

file = 'row.csv'
read_csv_file(file)


