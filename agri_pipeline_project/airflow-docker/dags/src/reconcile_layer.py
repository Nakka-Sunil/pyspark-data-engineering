# How many records came in?
# How many passed?
# How many failed?
# How many duplicates removed?
from loguru import logger
import time
import pandas as pd

def reconcile_data(loaded_data, audit_data):

    if loaded_data is None:
        loaded_data = []

    if audit_data is None:
        audit_data = pd.DataFrame()

    print("Process is at Reconcile layer")
    time.sleep(5)
    logger.info("PIPELINE SUMMARY -- RECONCILE LAYER")

    logger.info(f"Rows Loaded  : {len(loaded_data)}")
    logger.info(f"Rows Cleaned : {len(audit_data)}")

    if hasattr(audit_data, "columns"):
        logger.info(f"Columns: {len(audit_data.columns)}")
        logger.info(f"columns are: {list(audit_data.columns)}")

    return {
        "rows_loaded": len(loaded_data),
        "rows_cleaned": len(audit_data) if audit_data is not None else 0,
        "columns": len(audit_data.columns) if hasattr(audit_data, "columns") else 0
    }