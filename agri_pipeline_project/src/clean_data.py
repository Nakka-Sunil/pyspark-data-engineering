from main import loaded_data
import pandas as pd
from datetime import datetime

ds_karnataka = loaded_data[loaded_data["State"] == "Karnataka"]
ds_AndhraPradesh = loaded_data[loaded_data["State"] == "Andhra Pradesh"]
ds_tamilnadu = loaded_data[loaded_data["State"] == "Tamil Nadu"]
ds_Telangana = loaded_data[loaded_data["State"] == "Telangana"]

#print(f'Total records of Karnataka dataset are:  {len(ds_karnataka)}')

timestamp = datetime.now().strftime("%Y%m%d")
# print(timestamp)
def load_processed_data(ds):
    processed_dir = 'agri_pipeline_project/data/processed'

# Get unique states and save each as separate file
    for state in loaded_data['State'].unique():
        state_df = loaded_data[loaded_data["State"] == state]
        
        # Create filename from state name
        filename = state.replace(" ", "_").lower()
        filepath = f'{processed_dir}/{filename}.csv'
        
        # state_df.to_parquet(filepath, index=False)
        print(f"Saved {state}: {len(state_df)} records to {filepath}")

    return None

if __name__ == "__main__":
    processed_data = load_processed_data(ds_karnataka)
    print(processed_data)