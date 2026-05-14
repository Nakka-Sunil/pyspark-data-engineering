import pandas as pd
from datetime import datetime 

df = pd.read_csv(f'Python_layer\output\output_2026-05-10.csv')
df['time'] = pd.to_datetime(df['time'])
# print(df.head())
df['time'] = pd.to_datetime(df['time']).dt.date
# # or keep it as datetime but extract date
# df['date'] = pd.to_datetime(df['time']).dt.date
# df['hour'] = pd.to_datetime(df['time']).dt.hour

print(df.head(3))