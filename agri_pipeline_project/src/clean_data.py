import pandas as pd
from loguru import logger
from extract_data import load_data
import os


def check_nulls(data, columns=None):
    result_nulls = {}
    if columns is None:
        columns = data.columns.tolist()
    
    for col in columns:
        if data[col].isnull().any():
            total_nulls = data[col].isnull().sum()
            null_percent = round((total_nulls / len(data)) * 100, 2) 
            
            result_nulls[col] = {
                'nulls': total_nulls,
                'null_percent': null_percent
            }
    return result_nulls
    
    
def fill_values(data, method='fill', value=None):

    for col in data.columns:
        if data[col].isnull().any():
            if method.lower() == 'drop':
                data = data.dropna(subset=[col])  
            
            elif method.lower() == 'fill':
                if value is not None:  
                    data[col] = data[col].fillna(value)
                elif data[col].dtype in ['int64', 'float64']:
                    data[col] = data[col].fillna(data[col].median())
                else:
                    data[col] = data[col].fillna('unknown')
    return data


# def clean_data(data):
#     return data


if __name__ == "__main__":
    loaded_data = pd.DataFrame(load_data())
    cust_cols = input('Do you want to check nulls for any specific columns -- y/n: ')
    
    if cust_cols == 'y':
        no_of_cols = int(input('How many columns that you want to check nulls for [0-11]: '))
        col_lst = []

        for val in range(no_of_cols):
            col_name = input('Enter your column name Here, values must be in [State, District, Market, Commodity, Variety, Grade, Arrival_Date, Min_Price, Max_Price, Modal_Price, Commodity_Code]: ')
            col_lst.append(col_name)
     
        final_col_lst = [col for col in col_lst if col in loaded_data.columns]
    else: 
        final_col_lst = [col for col in loaded_data.columns]

    null_info = check_nulls(loaded_data, final_col_lst)
    
    if null_info:
        for col, stats in null_info.items():
            if stats['nulls'] > 0:
                print(f"Column '{col}': {stats['nulls']} nulls ({stats['null_percent']}%)")
                print('Handling Null values...!')
                print('\n')
                fill_values(loaded_data)
    else:
        print("No null values found in the specified columns.")

    
