import os
import json
import csv
import time
import paho.mqtt.client as mqtt # pip install paho-mqtt


# Load configuration
config_file = "publish-mqtt.json"

# Check if config file exists
if not os.path.exists(config_file):
    print(f"Configuration file '{config_file}' not found.")
    exit(1)

# Read configuration
with open(config_file, "r") as f:
    config = json.load(f)

# Extract configuration values
csv_filepath = config.get("csvfilepath")
mqtt_broker = config.get("mqttbroker", "broker.hivemq.com")
port = config.get("port", 1883)
topic = config.get("topic", "asim/farm1/demo")
delay = config.get("delay", 3)

# Check if CSV file exists
if not os.path.exists(csv_filepath):
    print(f"CSV file '{csv_filepath}' not found.")
    exit(1)

# Read CSV file and check if it has rows
with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    rows = list(reader)

if not rows:
    print("CSV file is empty or contains no rows.")
    exit(1)

# Initialize MQTT client
client = mqtt.Client()

try:
    # Connect to the MQTT broker
    client.connect(mqtt_broker, port)
    print(f"Connected to MQTT broker at {mqtt_broker}:{port}")
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Publish rows to MQTT
try:
    for row in rows:
        payload = json.dumps(row)  # Convert CSV row to JSON payload
        client.publish(topic, payload)  # Publish payload to topic
        print(f"Published to {topic}: {payload}")
        time.sleep(delay)  # Wait for the specified delay
except KeyboardInterrupt:
    print("\nPublishing interrupted by user.")
finally:
    client.disconnect()
    print("Disconnected from MQTT broker.")
