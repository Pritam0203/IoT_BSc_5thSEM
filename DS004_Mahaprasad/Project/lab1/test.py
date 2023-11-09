import paho.mqtt.client as mqtt

# Define the MQTT broker's address and port
broker_address = "172.16.51.203"
broker_port = 1883  # Default MQTT port

# Define the topic you want to subscribe to
topic_to_subscribe = "sensors/data"

# Define the callback function for message reception
def on_message(client, userdata, message):
    # This function is called when a message is received on the subscribed topic
    received_data = message.payload.decode("utf-8")
    print("Received data:", received_data)

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback function for message reception
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the MQTT topic
client.subscribe(topic_to_subscribe)

# Start the MQTT client loop to continuously listen for messages
client.loop_forever()
