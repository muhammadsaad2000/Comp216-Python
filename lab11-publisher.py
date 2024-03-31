import paho.mqtt.client as mqtt 
from random import uniform, randint
import time 


#https://eclipse.dev/files/paho.mqtt.python/html/client.html
BROKER = 'mqtt.eclipseprojects.io'
PORT = 1883


def on_connect(client, userdata, flags, reason, properties):
    print(f'Connection Reasn Code: {reason}')
     
    
client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id = 'COMP216-MS')

client_pub.on_connect = on_connect

client_pub.connect(BROKER, PORT)  # Connect to the MQTT broker

client_pub.loop_start()


for i in range (7):
    random_values = uniform  (10.0, 32.0)
    client_pub.publish ('Temperatre-COMP216', random_values)
    print(f'Publish {random_values} to Topic: Temperature-COMP216')
    time.sleep(2)
    
client_pub.loop_stop()