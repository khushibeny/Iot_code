from flask import Flask, jsonify
import json
from collections import deque

app = Flask(__name__)

# Create a dictionary to store sensor data
sensor_data = {}

@app.route("/sensor/<string:sensor_id>")
def get_sensor_data(sensor_id):
    if sensor_id not in sensor_data:
        return jsonify({"error": "Sensor not found"}), 404

    # Access the last data point (if it exists)
    if sensor_data[sensor_id]["data"]:
        last_data = sensor_data[sensor_id]["data"][0]
        return jsonify({"sensor_id": sensor_id, "timestamp": last_data[0], "temperature": last_data[1]})
    else:
        return jsonify({"error": "No data available for this sensor"}), 404

if __name__ == "__main__":
    app.run(debug=True)