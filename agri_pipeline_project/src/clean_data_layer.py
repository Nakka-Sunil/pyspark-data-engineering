import pandas as pd
from loguru import logger
from extract_data_layer import load_data
from pathlib import Path
import os

cleaned_folder_path = Path(f'agri_pipeline_project\data\processed')
cleaned_data_path = os.path.join(cleaned_folder_path, 'cleaned_agri_data.csv')

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

def clean_data(data):
    # Remove white spaces from object columns
    columns = data.select_dtypes(include=['object']).columns
    
    for col in columns:
        if col in data.columns:
            data[col] = data[col].str.strip()
    
    logger.info('White spaces removed from the data...!')
    
    # Remove duplicates
    data_before = len(data)
    data = data.drop_duplicates()
    data_after = len(data)
    rows_removed = data_before - data_after
    logger.info(f'Removed {rows_removed} rows from entire dataset..!')
    
    # Standardize text columns
    data_cols = [
        'State',
        'District',
        'Market',
        'Commodity',
        'Variety',
        'Grade'
    ]
    
    for col in data_cols:
        if col in data.columns:
            data[col] = data[col].str.title()
    
    logger.info('Dataset columns were standardized..!')
    
    # Convert dates
    if 'Arrival_Date' in data.columns:
        data['Arrival_Date'] = pd.to_datetime(
            data['Arrival_Date'],
            errors='coerce'
        )
        logger.info('Dates were converted..!')
    
    # Convert price columns to numeric
    price_cols = ['Min_Price', 'Max_Price', 'Modal_Price']
    
    for col in price_cols:
        if col in data.columns:
            data[col] = (
                data[col]
                .astype(str)
                .str.replace(',', '', regex=False)
                .str.replace('₹', '', regex=False)  
                .str.replace('$', '', regex=False)
            )
            data[col] = pd.to_numeric(
                data[col],
                errors='coerce'
            )
    
    logger.info('Prices were converted..!')
    
    # Return cleaned data
    logger.info('Data cleaned and sent for Next Process..!') 
    return data



if __name__ == "__main__":
    loaded_data = pd.DataFrame(load_data())
    final_col_lst = [col for col in loaded_data.columns]

    null_info = check_nulls(loaded_data, final_col_lst)
    
    if null_info:
        for col, stats in null_info.items():
            if stats['nulls'] > 0:
                print(f"Column '{col}': {stats['nulls']} nulls ({stats['null_percent']}%)")
                logger.info('Nulls check completed..!')
                print('Handling Null values...!')
                print('\n')
                data_filled = fill_values(loaded_data)
    
    cleaned_data = clean_data(data_filled)
    # cleaned_data.to_csv(
    #     cleaned_data_path,
    #     index=False
    # )





    


