import matplotlib as plt
import numpy as py
import pandas as pd
import csv

data = pd.read_csv('food_imports.csv')

data = data.drop(columns=['Unnamed: 1', 'Unnamed: 2'], index=[0, 1, 3])
data = data.set_index('Unnamed: 0')

year_list = list(data)
values_list = data.values.tolist()

#print(values_list)
#print(year_list)

print(data)
