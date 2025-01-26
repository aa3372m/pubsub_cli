# Project Documentation

## Overview
PubSub-cli aims to generate a data that can be used to test the mqtt based application.

### Prerequisites
- make sure you have **python 3.10+** installed
- install paho-mqtt:
``` bash
  pip install paho-mqtt
  ```

### Steps   
1. Data Generation (1-gen-csv.py)
   - Lets you define the data range for each sensor.
   - simply run: 
   ``` bash
   python 1-gen-csv.py
   ```
   - Output: demo_data.csv

2. MQTT Publishing (2-publish-to-mqtt.py) 
   - Takes the generated CSV data and publishes it to an MQTT broker.   
   - simply run: 
   ``` bash
   python 2-publish-to-mqtt.py
   ```
   - Output: Messages published to MQTT broker 
3. Monitoring  (3-consume-from-mqtt.py)
   - Consumes the data from the MQTT broker and prints it to the console.
   - simply run: 
   ``` bash
   python 3-consume-from-mqtt.py
   ```
   - Output: Data printed to the console.

