import os
import json
import paho.mqtt.client as mqtt

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
mqtt_broker = config.get("mqttbroker", "broker.hivemq.com")
port = config.get("port", 1883)
topic = config.get("topic", "asim/farm1/demo")

# Define the MQTT client callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker at {mqtt_broker}:{port}")
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)
        print(f"Received message from {msg.topic}: {json.dumps(data, indent=2)}")
    except json.JSONDecodeError:
        print(f"Received invalid JSON message from {msg.topic}: {msg.payload}")

# Initialize MQTT client
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connect to the MQTT broker
    client.connect(mqtt_broker, port)
    client.loop_forever()  # Keep the client running to listen for messages
except KeyboardInterrupt:
    print("\nMonitoring interrupted by user.")
finally:
    client.disconnect()
    print("Disconnected from MQTT broker.")
