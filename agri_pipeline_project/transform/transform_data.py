import sqlite3 as sql
import pandas as pd 
from pathlib import Path 
from loguru import logger
import time

try:
    ap_data_path = Path('agri_pipeline_project/data/processed/andhra_pradesh.csv')
    db_path = Path('agri_pipeline_project/sql/agri_database/agri_pipeline_db.db')
    df_andhra = pd.read_csv(ap_data_path)

except Exception as e:
    logger.error(f'Error occured while loading the data...! {e}')

try:
    db_conn = sql.connect(db_path)
    logger.info('Please wait, Connecting to the Database... ')
    print('\n')
    time.sleep(5)
except Exception as e:
    logger.error('Failed to connect to the database, Error occured..! {e}')

print('**'*60)
print('\n')
logger.success('Database connected Successfully...!')
print('\n')
print('**'*60)

df_andhra.to_sql(
    name='andhra_market_data',
    con=db_conn,
    if_exists= 'replace',
    index= True
)

try:

    sql_query = """
        SELECT
            COMMODITY,
            AVG(MODAL_PRICE) AS avg_modal_price
            FROM andhra_market_data
            GROUP BY COMMODITY
            ORDER BY avg_modal_price DESC
            LIMIT 10;
    """
    sql_result = pd.read_sql(sql_query, con=db_conn)
    print('\n')
    print(sql_result)
    print('\n')

    sql_query2 = """
        SELECT DISTRICT, 
               AVG(MODAL_PRICE) AS avg_modal_price
        FROM andhra_market_data
        GROUP BY DISTRICT
        HAVING avg_modal_price > 3000
        ORDER BY avg_modal_price DESC;
    """
    sql_result2 = pd.read_sql(sql_query2, con=db_conn)
    print('\n')
    print(sql_result2)
    print('\n')

    sql_query3 = """
        SELECT COMMODITY, MARKET, MODAL_PRICE,
            DENSE_RANK() OVER(PARTITION BY COMMODITY ORDER BY MODAL_PRICE DESC) AS price_rank
        FROM andhra_market_data
        ORDER BY price_rank;
    """
    sql_result3 = pd.read_sql(sql_query3, con=db_conn)
    print('\n')
    print(sql_result3)
    print('\n')

except Exception as e:
    logger.error(f'An exception occured... {e}')

finally:
    db_conn.close()
    logger.info('Database connection closed...!')