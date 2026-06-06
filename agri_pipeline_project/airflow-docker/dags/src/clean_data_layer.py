import pandas as pd
from loguru import logger
from src.extract_data_layer import load_data
from pathlib import Path
import os

cleaned_folder_path = Path('agri_pipeline_project/data/processed')
cleaned_data_path = os.path.join(cleaned_folder_path, 'cleaned_agri_data.csv')

def check_nulls(data, columns=None):
    """Check nulls but keep DataFrame unchanged (ETL-safe)"""

    if data is None:
        logger.error("check_nulls received None")
        raise ValueError("Cannot check nulls on None object")

    if not isinstance(data, pd.DataFrame):
        logger.error(f"check_nulls received non-DataFrame: {type(data)}")
        raise TypeError(f"Expected DataFrame, got {type(data)}")

    if data.empty:
        logger.warning("Empty DataFrame received in check_nulls")
        return data

    if columns is None:
        columns = data.columns.tolist()

    result_nulls = {}

    for col in columns:
        null_count = data[col].isnull().sum()

        if null_count > 0:
            null_percent = round((null_count / len(data)) * 100, 2)

            result_nulls[col] = {
                "nulls": null_count,
                "null_percent": null_percent
            }

            logger.info(f"{col}: {null_count} nulls ({null_percent}%)")

    if not result_nulls:
        logger.info("No null values found in dataset")
    return data

def fill_values(data, method='fill', value=None):
    """Fill or drop null values in the dataframe"""
    if data is None:
        logger.error("fill_values received None")
        raise ValueError("Cannot fill nulls on None object")
    
    if not isinstance(data, pd.DataFrame):
        logger.error(f"fill_values received non-DataFrame: {type(data)}")
        raise TypeError(f"Expected DataFrame, got {type(data)}")
    
    filled_data = data.copy()
    
    if method.lower() == 'drop':
        before_rows = len(filled_data)
        filled_data = filled_data.dropna()
        after_rows = len(filled_data)
        logger.info(f"Dropped {before_rows - after_rows} rows with null values")
    
    elif method.lower() == 'fill':
        for col in filled_data.columns:
            if filled_data[col].isnull().any():
                if value is not None:
                
                    filled_data[col] = filled_data[col].fillna(value)
                    logger.info(f"Filled nulls in '{col}' with value: {value}")
                
                elif filled_data[col].dtype in ['int64', 'float64']:
                    
                    median_val = filled_data[col].median()
                    filled_data[col] = filled_data[col].fillna(median_val)
                    logger.info(f"Filled nulls in '{col}' with median: {median_val}")
                
                else:
                
                    filled_data[col] = filled_data[col].fillna('unknown')
                    logger.info(f"Filled nulls in '{col}' with 'unknown'")
    
    logger.success(f"Null filling complete. Remaining nulls: {filled_data.isnull().sum().sum()}")
    return filled_data  

def clean_data(data):
    """Clean the dataframe"""
    if data is None:
        logger.error("clean_data received None")
        raise ValueError("Cannot clean None object")
    
    if not isinstance(data, pd.DataFrame):
        logger.error(f"clean_data received non-DataFrame: {type(data)}")
        raise TypeError(f"Expected DataFrame, got {type(data)}")
    
    cleaned_data = data.copy()
    
    object_columns = cleaned_data.select_dtypes(include=['object']).columns
    
    for col in object_columns:
        if col in cleaned_data.columns:
            cleaned_data[col] = cleaned_data[col].str.strip()
    
    logger.info('White spaces removed from the data...!')
    
    # Remove duplicates
    data_before = len(cleaned_data)
    cleaned_data = cleaned_data.drop_duplicates()
    data_after = len(cleaned_data)
    rows_removed = data_before - data_after
    if rows_removed > 0:
        logger.info(f'Removed {rows_removed} duplicate rows from entire dataset..!')
    
    # Standardize text columns (only if they exist)
    text_cols = [
        'State',
        'District',
        'Market',
        'Commodity',
        'Variety',
        'Grade'
    ]
    
    for col in text_cols:
        if col in cleaned_data.columns:
            cleaned_data[col] = cleaned_data[col].str.title()
    
    logger.info('Dataset columns were standardized..!')
    
    # Convert dates
    if 'Arrival_Date' in cleaned_data.columns:
        cleaned_data['Arrival_Date'] = pd.to_datetime(
            cleaned_data['Arrival_Date'],
            errors='coerce'
        )
        logger.info('Dates were converted..!')
    
    # Convert price columns to numeric
    price_cols = ['Min_Price', 'Max_Price', 'Modal_Price']
    
    for col in price_cols:
        if col in cleaned_data.columns:
            # Clean the price strings
            cleaned_data[col] = (
                cleaned_data[col]
                .astype(str)
                .str.replace(',', '', regex=False)
                .str.replace('₹', '', regex=False)  
                .str.replace('$', '', regex=False)
                .str.strip()
            )
            # Convert to numeric
            cleaned_data[col] = pd.to_numeric(
                cleaned_data[col],
                errors='coerce'
            )
    
    logger.info('Prices were converted to numeric..!')
    logger.success(f"Cleaning complete. Final shape: {cleaned_data.shape}")
    logger.info('Data cleaned and sent for Next Process..!')
    
    return cleaned_data

if __name__ == "__main__":
    print("Testing data pipeline functions...\n")

    loaded_data = load_data()
    if loaded_data is None or not isinstance(loaded_data, pd.DataFrame):
        print(" Failed to load data or invalid format")
        exit()

    if loaded_data.empty:
        print(" Loaded data is empty")
        exit()

    print(f"Loaded data shape: {loaded_data.shape}")

    null_info = check_nulls(loaded_data)

    if isinstance(null_info, dict) and null_info:
        print("\nNull values found:")
        for col, stats in null_info.items():
            print(f"  {col}: {stats['nulls']} nulls ({stats['null_percent']}%)")
    else:
        print("\nNo null values found.")
    print("\nHandling null values...")

    data_filled = fill_values(loaded_data)

    if data_filled is None or data_filled.empty:
        print(" Fill null returned empty/None data")
        exit()

    print(f"After filling nulls - shape: {data_filled.shape}")

    print("\nCleaning data...")

    cleaned_data = clean_data(data_filled)

    if cleaned_data is None or cleaned_data.empty:
        print(" Clean data returned empty/None")
        exit()

    print(f"Cleaned data shape: {cleaned_data.shape}")

    print("\n All cleaning operations completed successfully!")