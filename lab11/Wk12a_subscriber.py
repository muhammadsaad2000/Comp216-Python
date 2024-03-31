# Wk12a_subscriber.py

import paho.mqtt.client as mqtt
import json
from Wk12a_util import print_data

def on_message(client, userdata, msg):
    print("Received message:", msg.payload)
    decoded_payload = json.loads(msg.payload)
    print_data(decoded_payload)

client = mqtt.Client()
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

topic = "health_data"
client.subscribe(topic)

print("Subscribed to topic:", topic)

client.loop_forever()
