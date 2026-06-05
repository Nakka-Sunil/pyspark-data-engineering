import pandas as pd
from extract_data_layer import load_data
from loguru import logger
from datetime import datetime
from uuid import uuid4

df_loaded_data = pd.DataFrame(load_data())
files = df_loaded_data['file_name'].unique()
# print(files)
def audit_data(df = None):
    if df is None: 
        df = df_loaded_data
        logger.info(f'All loaded files are: {"," .join(files), }')

        #loaded Timestamp
        df['timestamp'] = datetime.now()

        #uuID
        df['load_id'] = uuid4()
        logger.info('Audit columns were added..Moving to reconcile Now..!')
        return df

    else: 
        logger.info(f'No Data received in Audit layer..!')
        return 

if __name__ == "__main__":
    audit_data(df_loaded_data)
