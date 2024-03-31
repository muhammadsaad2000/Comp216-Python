# Wk12a_publisher.py

import paho.mqtt.client as mqtt
import json
import time
from Wk12a_util import create_data

def on_publish(client, userdata, mid):
    print("Message Published")

client = mqtt.Client()
client.connect("mqtt.eclipse.org", 1883, 60)

topic = "health_data"

while True:
    data = create_data("John Doe")
    payload = json.dumps(data)
    client.on_publish = on_publish
    client.publish(topic, payload)
    print("Published:", payload)
    time.sleep(5)

client.disconnect()
