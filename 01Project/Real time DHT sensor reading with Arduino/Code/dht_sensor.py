import serial
import time
from datetime import datetime
import csv

ser = serial.Serial('COM5', 9600, timeout=1)
# time.sleep(2)

def dht_data():
    for i in range(4):
        line = ser.readline().decode('utf-8')
        values = line.split(',')
        values = [i.strip() for i in values]
        if len(values) == 2:
            return values
    return None



while True:
    data = dht_data()
    if data is not None:
        humidity, temperature = data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('dht_readings.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([timestamp, humidity, temperature])

