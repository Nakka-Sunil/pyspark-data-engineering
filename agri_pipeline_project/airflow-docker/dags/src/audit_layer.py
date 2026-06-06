import pandas as pd
from loguru import logger
from datetime import datetime
from uuid import uuid4

def audit_data(df):
    if df is None or df.empty:
        logger.warning("No data received in audit layer")
        return df

    if 'file_name' not in df.columns:
        logger.warning("file_name column missing. Skipping file audit.")
        files = []
    else:
        files = df['file_name'].unique().tolist()

    logger.info(f"All loaded files are: {files}")

    df = df.copy()
    df['timestamp'] = datetime.now()
    df['load_id'] = str(uuid4())

    logger.info("Audit columns added successfully")

    return df