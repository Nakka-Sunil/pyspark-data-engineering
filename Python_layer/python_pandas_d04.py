import pandas as pd
from datetime import datetime 
import os 

# df = pd.read_csv(f'Python_layer\output\output_2026-05-10.csv')
# df['time'] = pd.to_datetime(df['time'])
  # print(df.head())
# df['time'] = pd.to_datetime(df['time']).dt.date
# # or keep it as datetime but extract date
# df['date'] = pd.to_datetime(df['time']).dt.date
# df['hour'] = pd.to_datetime(df['time']).dt.hour

# print(df.head(3))
folder_path = f'Python_layer\input'
files = os.listdir(folder_path)

final_file_lst = []
all_dfs = []

for file in files:
    if file.endswith('.csv'):
        final_file_lst.append(file)
# print(final_file_lst)

for file in final_file_lst:
    full_path = os.path.join(folder_path, file)
    df = pd.read_csv(full_path)
    all_dfs.append(df)

final_df = pd.concat(all_dfs)

# print(df.head())

final_df['time'] = pd.to_datetime(final_df['time'])
final_df['date'] = pd.to_datetime(final_df['time']).dt.date
final_df['hour'] = pd.to_datetime(final_df['time']).dt.hour

# q1 : Hot Temperature Rows
final_df['hot_temperature'] = final_df['temperature'].where(final_df['temperature'] > 25) 
# print(final_df.head(20))

# q2: Create Fahrenheit Column
final_df['temp_fahrenheit'] = (final_df['temperature'] * (9/5)) + 32
# print(final_df.head(10))

# q3: Find Maximum Temperature Per Day
max_temp_per_day = (
                final_df.groupby('date')['temperature']
                .max()
                # .reset_index()
)
# print(max_temp_per_day)

# q4: Find Average Temperature Per Hour
avg_temp_per_hour = (
                final_df.groupby('hour')['temperature']
                .mean()
                # .reset_index()
)

# print(round(avg_temp_per_hour,2))

# q5: Sort By Highest Temperature
final_df = final_df.sort_values(
    by = 'temperature',
    ascending = False
)
# print(final_df.head(10))

#q6:  Create Summary Table

min_temp_per_day = (
            final_df.groupby('date')['temperature']
            .min()
            # .reset_index()
)
avg_temp_per_day = (
            final_df.groupby('date')['temperature']
            .mean()
)

df_day_summary = pd.DataFrame({
    'date': max_temp_per_day.index,
    'min_temp': min_temp_per_day.values,
    'max_temp': max_temp_per_day.values,
    'avg_temp': avg_temp_per_day.values
})

df_hour_summary = pd.DataFrame({
    'date': avg_temp_per_hour.index,
    'avg_hour': avg_temp_per_hour

})

# print(df_day_summery.head())
# print(df_hour_summery.head())
df_day_summary.to_csv('Python_layer\output\day_summry_16-05-2026.csv')
df_hour_summary.to_csv('Python_layer\output\hour_summry_16-05-2026.csv')
