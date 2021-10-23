import pandas as pd
import csv

df = pd.read_csv('final.csv')

del df['Star_name.2']
del df['Distance.2']
del df['Mass.2']
del df['Radius.2']
del df['Luminosity']

df.to_csv("main.csv")