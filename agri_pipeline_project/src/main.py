import pandas as pd

def load_data(file_path):
    if file_path:
        dataset = pd.read_csv(file_path)
        # dataset.head(5)
        return dataset 
    return None

file_path = f'agri_pipeline_project/data/raw/2001.csv'
loaded_data = load_data(file_path)


if __name__ == "__main__":

    print('\n')
    print(f'Data loaded successfully!!! {loaded_data.shape}')
    # print(loaded_data)
