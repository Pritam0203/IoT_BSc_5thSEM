import threading
import time
from subprocess import Popen

# Start the DHT sensor data collection in a separate process
sensor_process = Popen(["python", "dht_sensor.py"])

# Start the Streamlit app
st_process = Popen(["streamlit", "run", "streamlit_app.py"])

# Wait for both processes to finish
sensor_process.wait()
st_process.wait()
