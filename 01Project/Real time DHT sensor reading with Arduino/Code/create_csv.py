import csv

with open('dht_readings.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Timestamp', 'Humidity', 'Temperature'])
