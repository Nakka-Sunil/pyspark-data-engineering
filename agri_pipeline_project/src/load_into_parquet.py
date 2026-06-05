import pandas as pd
from audit_layer import audit_data
import os 
from pathlib import Path
from loguru import logger

folder_path = Path(f'agri_pipeline_project\data\processed')
file_path = os.path.join(folder_path, 'processed_agri_data.parquet')
audit_data_final = pd.DataFrame(audit_data())
if not os.path.exists(file_path):
    audit_data_final.to_parquet(file_path, index=False)
    logger.info(f'Saved data into Parqet file in the location {file_path}')
    print(f'Final Data loaded into the location {file_path}')