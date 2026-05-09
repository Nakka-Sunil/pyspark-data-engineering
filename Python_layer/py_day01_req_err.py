import requests 
from loguru import logger
import csv

url = f'https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m'

try:
    logger.info('API call started!!!')
    response = requests.get(url)
# print(response.status_code)
# print(response.text)
    data = response.json()
    # print(data)

except Exception as e:
    logger.error(f'Something went wrong : {e}')


data = [data['longitude'], data['latitude'], data['generationtime_ms'], data['generationtime_ms'], data['elevation'], data['hourly']['time'], data['hourly']['temperature_2m']]

with open('Python_layer\weather_banglore.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    logger.info('file updated successfully!!!')

