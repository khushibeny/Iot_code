import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT broker details
broker = "mqtt.thingsboard.cloud"
port = 1883
topic = "v1/devices/me/telemetry"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port, 60)

while True:
    # Simulate a temperature value
    temperature = random.uniform(20, 30)  # Generate a random temperature between 20 and 30

    # Add your own temperature value
    temperature += 5  # You can adjust this value as needed

    # Publish data to MQTT broker
    payload = {"temperature": temperature}
    client.publish(topic, json.dumps(payload), qos=1)
    print(f"Published: {payload}")

    # Wait for 60 second before publishing again
    time.sleep(60)