# How many records came in?
# How many passed?
# How many failed?
# How many duplicates removed?

import pandas as pd
from extract_data_layer import load_data
from audit_layer import audit_data
from loguru import logger
import time

df_loaded_data = pd.DataFrame(load_data())
df_audited_data = pd.DataFrame(audit_data())
print("Process is at Reconcile layer")
time.sleep(5)
logger.info("PIPELINE SUMMARY -- RECONCILE LAYER")
logger.info(f"Rows Loaded  : {len(df_loaded_data)}")
logger.info(f"Rows Cleaned : {len(df_audited_data)}")
logger.info(f"Columns      : {len(df_audited_data.columns)}")
logger.info(f'columns are  : {str(list(df_audited_data.columns))}')
