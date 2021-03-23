
import os

import pandas as pd
#import numpy

os.chdir("C:\\Users\\Satish\\Documents\\My Things\\Data Science & ML\\Teaching Python")


data = pd.read_csv("index.csv")

print(data.head())

print(data.columns[2])

print(data.iloc[:,-2:])

print()
print(data.iloc[-10:,:2])

