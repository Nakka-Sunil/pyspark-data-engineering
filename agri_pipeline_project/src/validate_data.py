import pandas as pd
from loguru import logger
import os
from pathlib import Path

file_path = Path('agri_pipeline_project/data/processed/cleaned_agri_data.csv')
df_agri_data = None

try:
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
    logger.info(f"File exists. Size: {file_size} bytes")
    
    # Check if file is empty
    if file_size == 0:
        logger.error("File is completely empty (0 bytes)")

    elif file_size > 0:
        df_agri_data = pd.read_csv(file_path)
        logger.info(f"Successfully loaded data from {file_path}")
    else:
        raise FileNotFoundError(f"File not found at {file_path}")

except FileNotFoundError as e:
    logger.error(f"Source file doesn't exist at the path {file_path}: {e}")
except Exception as e:
    logger.error(f'Unknown exception occurred: {e}')

def validate_data(df):
    
    if df is None or df.empty:
        logger.error("No data to validate")
        return None
    
    print('**' * 50)
    print('Checks were started....!')
    
    # 1. DUPLICATE CHECK
    logger.info('Checking for duplicates..!')
    initial_rows = len(df)
    dup_count_series = df.duplicated(keep='first')
    dup_count = dup_count_series.sum()  # Count of duplicates
    
    dup_proportion = (dup_count / initial_rows) * 100 if initial_rows > 0 else 0
    
    if dup_count > 0:
        logger.info(f'Data has {dup_count} duplicates ({dup_proportion:.2f}% proportion)')
        logger.info('Dropping duplicates (first occurrence will be retained)..!')
        df = df.drop_duplicates(keep='first')
        logger.info(f'Rows after dropping duplicates: {len(df)}')
    else:
        logger.info('No duplicates present in the dataset..!')
    
    # 2. NEGATIVE PRICE CHECK
    col_lst = ['Min_Price', 'Max_Price', 'Modal_Price']
    group_cols = ['State', 'District', 'Market', 'Commodity']
    
    for col in col_lst:
        if col in df.columns:
            # Check if column has any negative values
            if (df[col] < 0).any():
                negative_count = (df[col] < 0).sum()
                logger.info(f'Column "{col}" has {negative_count} negative values')
                logger.info(f'Replacing negatives with group mean (by {", ".join(group_cols)})')
                
                # Replace negatives with group mean of positive values
                df[col] = df.groupby(group_cols)[col].transform(
                    lambda x: x.where(x >= 0, x[x > 0].mean())
                )
                
                # Handle groups with no positive values (use overall mean)
                if df[col].isna().any():
                    overall_mean = df[df[col] > 0][col].mean()
                    df[col] = df[col].fillna(overall_mean)
                
                logger.info(f'Negative values replaced in column "{col}"')
            else:
                logger.info(f'No negative values found in column "{col}"')
        else:
            logger.warning(f'Column "{col}" not found in DataFrame')


    # Empty Commodity Names

    # Invalid Dates
    logger.info(f'Validation complete. Final row count: {len(df)}')
    print('**' * 50)
    return df.head(5)

if __name__ == "__main__":
    if df_agri_data is not None:
        valid_data = validate_data(df_agri_data)
        if valid_data is not None:
            print("\nFirst 5 rows of validated data:")
            print(valid_data)

    else:
        logger.error("Cannot validate: No data loaded")