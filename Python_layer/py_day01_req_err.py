import requests 
from loguru import logger
import csv
import json
import os
from datetime import datetime


date = datetime.now().strftime('%Y-%m-%d')

with open('Python_layer\config.json','r') as file:
    config = json.load(file)
    # print(config)

log_dir = os.path.join('Python_layer', config['log_folder'])
os.makedirs(log_dir, exist_ok=True)
full_log_path = os.path.join(log_dir, 'weather_logs.txt')
logger.remove()
logger.add(full_log_path, rotation="10 MB")

long = config['longitude']
lat = config['latitude']

url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m'

def fetch_weather_data():
    try:
        logger.info('API call started!!!')
        response = requests.get(url)
        response.raise_for_status()
        # print(response.status_code)
        # print(response.text)
        data = response.json()
        # print(data)
    except Exception as e:
        logger.error(f'Something went wrong : {e}')
        return None
    
    return data
    
def transform_weather_data(data):
    dataset = []
    time = data['hourly']['time']
    temps = data['hourly']['temperature_2m']
    for time, temp in zip(time,temps):
        dataset.append([time,temp])
    return dataset

def save_to_csv(data, date):
    output_dir = os.path.join('Python_layer', config['output_folder'])
    os.makedirs(output_dir, exist_ok=True)
    full_output_path = os.path.join(output_dir, f'output_{date}.csv')

    with open(full_output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['time', 'temperature_2m'])
        writer.writerows(data)
    logger.info('File saved successfully!')
            
if __name__ == '__main__':
    fetching_data = fetch_weather_data()
    if fetching_data:
        transform_data = transform_weather_data(fetching_data)
        save_to_csv(transform_data, date)