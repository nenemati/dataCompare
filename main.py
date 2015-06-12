import csv


f = open('LoanStats3d.csv', 'rb')
reader = csv.reader(f)

for row in reader:
    print(row)
f.close()


