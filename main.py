import csv


f = open('name.csv', 'rb')
reader = csv.reader(f)

for row in reader:
    print(row)
f.close()


