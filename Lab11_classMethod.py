import paho.mqtt.client as mqtt 
from random import uniform, randint
import time 

class Publisher:
    broker = 'mqtt.eclipseprojects.io'
    port = 1883

def __init__(self, topic = 'Comp216-Test', delay= 0.75):
    self.pub_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id = str(randint(0,100)))
    self.topic = topic
    self.delay = delay
    self.pub_client.on_connect = self.on_connect 
    self.pub_client.on_publish = self.on_publish
    self.pub_client.on_disconnect = self.on_disconnect 
    
    def on_connect(client, userdata, flags, reason, properties):
     print(f'Connection Reasn Code: {reason}')
     
    def on_publish(self,userdata, mid, flags, reason, properties):
        print(f'Publish Reason Code:{reason} for message ID: {mid}') 
    
    def pub_connect(self):
     print(f'Connecting to brker @{Publisher.broker}') 
    self.pub_client.connect(Publisher.broker, prot=Publisher.port)
    self.pub_client.loop_start()
    self.pub_client.publish(self.topic, random_value)
    print(f'Value{random_value} is being published to TOpic:{self.topic}')
    time.sleep(self.delay)
    
    def publish_data(self, value1,value2):
        self.pub_client.loop()
        random_value = round(uniform(value1,value2),3)
    
    
    def on_disconnect(self, client, userdata, flags, reason, properties):
        print(f'Close connection Reason Code: {reason} ')
        self.pub_client.loop_stop()
    def pub_disconnect(self):
        self.pub_client.disconnect()
    
if __name__ == '__main__':
       test_publisher = Publisher()
       test_publisher.pub_connect()
       for i in range(7) :
        test_publisher.publish_data(12,32)

        
    