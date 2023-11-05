import paho.mqtt.client as mqttClient
import time
  
Connected = False #global variable for the state of the connection
  
broker_address= "localhost"
port = 1883
user = "user1"
password = "IDSSolarBench"

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:

        print("Connection failed")
  
def on_message(client, userdata, message):
    
    print("Message received: "  + str(message.payload))

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message  

client.connect(broker_address, port=port)  #connect to broker
client.loop_start()                        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("python/test")

try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()