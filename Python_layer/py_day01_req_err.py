import requests 
from loguru import logger
import csv

url = f'https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m'

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
    dataset = [data['longitude'], data['latitude'], data['generationtime_ms'], data['generationtime_ms'], data['elevation'], data['hourly']['time'], data['hourly']['temperature_2m']]
    return dataset

def save_to_csv(data):
    with open('Python_layer\weather_banglore.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['longitude', 'latitude','generationtime_ms','elevation','time','temperature_2m'])
        writer.writerow(data)
        logger.info('file updated successfully!!!')

if __name__ == '__main__':
    fetching_data = fetch_weather_data()
    if fetching_data:
        transform_data = transform_weather_data(fetching_data)
        save_to_csv(transform_data)