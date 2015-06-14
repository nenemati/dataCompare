import csv
import pandas as pd
from pandas import DataFrame


df1 = pd.read_csv('Relocated_Vehicles.csv')
df1 = pd.read_csv('Towed_Vehicles.csv')

print df1.head(2)








#
# f = open('LoanStats3d.csv', 'rb')
# reader = csv.reader(f)
#
# for row in reader:
#     print(row)
# f.close()
#

