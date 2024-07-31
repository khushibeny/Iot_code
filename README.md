This repository contains code for a simple sensor data server that exposes sensor data on an HTTP endpoint. The server is implemented using Flask, and it uses an MQTT broker to receive sensor data from a subscriber. The subscriber listens for sensor data from a publisher and updates the server's sensor data dictionary.
The system is designed to raise an alarm if the temperature of a sensor is above a threshold value for a certain duration. The threshold and alarm duration can be configured in the subscriber code.
> Requirements:
Python 3.x
Flask
Paho-MQTT
> Setup
Install the required packages using pip:
pip install Flask paho-mqtt
Modify the MQTT broker details in the publisher.py, subscriber.py, and server.py files to match your MQTT broker.
> Running the Code
Start the MQTT broker.
Run the publisher code to start publishing sensor data to the MQTT broker:
publisher.py
Run the subscriber code to start receiving sensor data from the MQTT broker and updating the server's sensor data dictionary:
subscriber.py
Run the server code to start the Flask server and expose the sensor data on an HTTP endpoint:
server.py
Access the sensor data by making an HTTP GET request to the /sensor/<sensor_id> endpoint, where <sensor_id> is the ID of the sensor you want to retrieve data for. For example, if you have a sensor with ID sensor_1, you can retrieve its last data point by visiting http://localhost:5000/sensor/sensor_1 in your web browser or using a tool like curl:
bash
curl http://localhost:5000/sensor/sensor_1
The server will return a JSON object with the sensor ID, timestamp, and temperature value. If the sensor ID is not found, the server will return a 404 error.

>Alarm Notification
The subscriber code will raise an alarm if the temperature of a sensor is above a threshold value for a certain duration. The threshold and alarm duration can be configured in the subscriber code. When an alarm is raised, the subscriber will print a message to the console.
