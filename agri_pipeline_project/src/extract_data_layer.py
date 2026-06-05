import pandas as pd
from loguru import logger
from pathlib import Path

log_dir = Path("agri_pipeline_project\logs")
log_dir.mkdir(parents=True, exist_ok=True)

log_path = log_dir / "agri_pipeline_logs.log"

logger.remove()
logger.add(log_path, rotation="5 MB")

folder_path_def = Path('agri_pipeline_project/data/raw')
def load_data(folder_path = None):
    if folder_path is None:
        folder_path = folder_path_def
    try:
        
        folder_path = Path(folder_path)
        all_files = list(folder_path.glob('*.csv'))
        df = []

        if not all_files:
            raise FileNotFoundError(
                f"No files exists under folder {folder_path}"
            )
        else:
            for file in all_files:
                file_df = pd.read_csv(file)
                file_df['file_name'] = file.name
                df.append(file_df)
            
            final_df = pd.concat(
                df,
                ignore_index= True
            )

        logger.success(
            f"Successfully loaded {len(all_files)} files..."
        )

        return final_df

    except FileNotFoundError as e:
        logger.error(e)

    except Exception as e:
        logger.exception(e)

if __name__ == "__main__":
    folder_path = Path('agri_pipeline_project/data/raw')
    loaded_data = load_data(folder_path)

    if loaded_data is not None:
        print(f'Loaded {len(loaded_data)} rows of data')