print("Start")
from UI import*
#from physical import*
import time
import random
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["button1","button2"]
AIO_USERNAME = "nguyentu1402"
AIO_KEY = "aio_QLTS638yGtVtkSakhUXhjWzsPjRM"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
   

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed: " + feed_id)
    
def randomValue(type):
    value = 0
    if type == 0:
        value = round(random.randint(20, 80)/30, 2)
    elif type == 1:
        value = round(random.randint(1, 1500), 0)
    else:
        value = round(random.randint(100, 1400) / 100, 2)
    return value

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_background()
counter_sensor = 10
sensor_type = 0
counter_sensor = 10
sensor_type = 0


# def bat():
#     global client
#     client.publish("button1", "1")

# def tat():
#     global client
#     client.publish("button1", "0")
    
def bat():
    global client
    client.publish("button2", "1")

def tat():
    global client
    client.publish("button2", "0")    

ButtonON.config(command=bat)
ButtonOFF.config(command=tat)

while True:
    #print(readMoisture())  
    counter_sensor -= 1
    if counter_sensor <= 0:
        counter_sensor = 10
        if sensor_type == 0:
            labelAMONIAValue.config(text=str(randomValue(0)))   
            sensor_type = 1
        elif sensor_type == 1:
            labelTDSValue["text"] = str(randomValue(1))
            sensor_type = 2
        else:
            labelPHValue.config(text=str(randomValue(2)))
            sensor_type = 0    
        

    window.update()  
    time.sleep(0.1)
