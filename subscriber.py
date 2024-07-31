import paho.mqtt.client as mqtt
import json
import time
from collections import deque

# MQTT broker details
broker = "mqtt.thingsboard.cloud"
port = 1883
topic = "v1/devices/me/telemetry"

# Threshold value
threshold = 30

# Alarm duration (5 minutes)
alarm_duration = 5 * 60  # in seconds

# Create a dictionary to store sensor data and alarm status
sensor_data = {}

def on_message(client, userdata, message):
    # Parse the JSON payload
    payload = json.loads(message.payload.decode("utf-8"))

    # Extract the sensor ID and temperature value
    sensor_id = payload["sensor_id"]
    temperature = payload["temperature"]

    # Create a new entry for the sensor if it doesn't exist
    if sensor_id not in sensor_data:
        sensor_data[sensor_id] = {"data": deque(maxlen=5), "alarm": False}

    # Add the new data point to the sensor's data queue
    sensor_data[sensor_id]["data"].append((time.time(), temperature))

    # Check if the sensor has crossed the threshold continuously for 5 minutes
    if all(temp > threshold for _, temp in sensor_data[sensor_id]["data"]):
        if not sensor_data[sensor_id]["alarm"]:
            print(f"Alarm raised for sensor {sensor_id}! Temperature has been above {threshold} for 5 minutes.")
            sensor_data[sensor_id]["alarm"] = True
    else:
        sensor_data[sensor_id]["alarm"] = False

    # Save the data locally
    with open(f"sensor_data_{sensor_id}.log", "a") as f:
        for timestamp, temp in sensor_data[sensor_id]["data"]:
            f.write(f"{timestamp},{temp}\n")

client = mqtt.Client()
client.connect(broker, port, 60)
client.subscribe(topic)
client.on_message = on_message  # Correct way to set the callback

while True:
    client.loop()
    time.sleep(1)