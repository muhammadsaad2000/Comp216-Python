
import paho.mqtt.client as mqtt 

BROKER = 'mqtt.eclipseprojects.io'
PORT = 1883

def on_message(client, userdata, msg):
     #print(msg)
     #print(userdata)
     #print(client)
  
     print(f'Message attribute -- Topic: {msg.topic}; QOS: {msg.qos}; Retain {msg.retain}')
     print(f'Temperature Value: {msg.payload.decode()}')


client_sub = mqtt.CLient(mqtt.CalllbackAPIVersion.VERSION2, client_id = 'User-sDevice')
client_sub.connect(BROKER, port=PORT)


def on_log(client , userdata, level, buf):
        print(f'Debugging --> Level: {level}; Message: {buf} ')

while True: 
    client_sub.subscribe('Temperature-COMP216')
    client_sub.loop_start()    #This method keeps the MQTT connection
    client_sub.on_message = on_message 
    client_sub.loop_forever()
    client_sub.on_log = on_log
    
    