from main import loaded_data
import pandas as pd
import os
# from datetime import datetime
from pathlib import Path

ds_karnataka = loaded_data[loaded_data["State"] == "Karnataka"]
ds_andhra_pradesh = loaded_data[loaded_data["State"] == "Andhra Pradesh"]
ds_tamil_nadu = loaded_data[loaded_data["State"] == "Tamil Nadu"]
ds_telangana = loaded_data[loaded_data["State"] == "Telangana"]

# timestamp = datetime.now().strftime("%Y%m%d")

def load_processed_data():
    processed_dir = Path('agri_pipeline_project\processed')

    states_data = {
        "karnataka": ds_karnataka,
        "andhra_pradesh": ds_andhra_pradesh,
        "tamil_nadu": ds_tamil_nadu,
        "telangana": ds_telangana
    }

    for state_name, state_df in states_data.items():

        filepath = f'{processed_dir}\{state_name}.csv'
        old_count = len(state_df)

        if os.path.exists(filepath):
            existing_data = pd.read_csv(filepath)

            combined_data = pd.concat(
                [existing_data, state_df],
                ignore_index = True
            )
            print('Dropping duplicates...!')
            print('\n')
            combined_data = combined_data.drop_duplicates(
                subset = ['State','District','Market','Commodity','Variety','Grade','Arrival_Date']
            )
            print('*'*70)
            print(f'Data Updated!!! old count is: {old_count} and new count is: {len(combined_data)}')
        
        else:
            combined_data = state_df
            print(f"Data doesn't exist for the state {state_name}, Inserting for the first time!!!")
            print('\n')
        # Save file
        combined_data.to_csv(filepath, index=False)

        print(f"Saved {state_name}: {len(state_df)} records to {filepath}")
        print('*'*70)
        print('\n')

    return None


if __name__ == "__main__":
    processed_data = load_processed_data()
    print(processed_data)