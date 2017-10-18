# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 19:43:52 2017

@author: roby
"""
#importazione file csv
import csv
with open('tab_values.txt','rb') as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        date=row[0]
        symbol=row[1]
        closing_price=float(row[2])
        print(str(date) + " "+ str(symbol) + " "+ str(closing_price)+"\n")
