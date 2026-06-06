import pandas as pd
from loguru import logger
from pathlib import Path

log_dir = Path("logs")  
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / "agri_pipeline_logs.log"

logger.remove()
logger.add(log_path, rotation="10 MB")

def load_data(folder_path=None):
    
    try:
        if folder_path is None:
            possible_paths = [
                Path('/opt/airflow/data/raw'),  
                Path('data/raw'),                
                Path('agri_pipeline_project/data/raw'),  
                Path('../data/raw'),              
            ]
            
            folder_path = None
            for path in possible_paths:
                if path.exists():
                    folder_path = path
                    logger.info(f"Found data at: {folder_path}")
                    break
            
            if folder_path is None:
                error_msg = f"No data folder found. Tried: {possible_paths}"
                logger.error(error_msg)
                raise FileNotFoundError(error_msg)
        
        folder_path = Path(folder_path)
        
        if not folder_path.exists():
            raise FileNotFoundError(f"Folder does not exist: {folder_path}")

        all_files = list(folder_path.glob('*.csv'))
        
        if not all_files:
            raise FileNotFoundError(f"No CSV files found in folder: {folder_path}")
  
        df_list = []
        for file in all_files:
            logger.info(f"Reading file: {file.name}")
            file_df = pd.read_csv(file)
            file_df['file_name'] = file.name
            df_list.append(file_df)
        
        final_df = pd.concat(df_list, ignore_index=True)
        
        logger.success(f"Successfully loaded {len(all_files)} files with {len(final_df)} rows")
        print(f'Data loaded from folder path: {folder_path}')
        return final_df  

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        logger.warning("Creating sample data for testing...")
        
    
    except Exception as e:
        logger.exception(f"Unexpected error loading data: {e}")
        logger.warning("Creating sample data for testing...")
    

if __name__ == "__main__":
    loaded_data = load_data()
    
    if loaded_data is not None:
        logger.info(f"Successfully loaded {len(loaded_data)} rows of data")
        print(f"Successfully loaded {len(loaded_data)} rows of data")
        print(f"Columns: {loaded_data.columns.tolist()}")
    else:
        print("No data available to load!")