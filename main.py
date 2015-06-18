__author__ = 'nemanemati'

import pandas as pd
import numpy as np
import csv

relocated = pd.read_csv('Relocated_Vehicles.csv') #read in
towed = pd.read_csv('Towed_Vehicles.csv') #read in
TOTAL_l = len(relocated) #total
TOTAL_t = len(towed)

towed_makes = towed.groupby('Make')
relocated_makes = relocated.groupby('Make')

towed_perc = towed_makes.apply(lambda x: len(x) / float(TOTAL_t))
relocated_perc = relocated_makes.apply(lambda x: len(x) / float(TOTAL_l))

make_mapper = pd.Series(index=towed_perc.index)
for name1 in make_mapper.index:
    for name2 in relocated_perc.index:
        if name1.lower() in name2.lower():
            make_mapper[name1] = name2
            #checks if shorter name is in longer name

relocated_perc = make_mapper.map(relocated_perc)
corr = relocated_perc.corr(towed_perc)
print corr  # positively correlated, so cars that are likely to be towed are also likely to be relocated
