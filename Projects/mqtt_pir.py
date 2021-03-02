from time import sleep
from simple import MQTTClient
from pir_sensor import pirClass
from led_handler import ledClass
from machine import Pin

import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("<SSID>", "<pass>")

SERVER = '192.168.1.6'  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'ESP32_PIR_Sensor'
TOPIC = b'pir/movement'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()   # Connect to MQTT broker

pirRising = pirClass(27)
pirFalling = pirClass(26)
led1 = ledClass(25)

#Function using interupts
def pirIRQ ():
  pirRising.pir.irq(trigger = Pin.IRQ_RISING, handler = pirInterruptRising)

  pirFalling.pir.irq(trigger = Pin.IRQ_FALLING, handler = pirInterruptFalling)

#Interrupt when pir activated
def pirInterruptRising(pin):
	led1.ledOn()
	msg = 'PIR Activated'
	client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
	print(msg)
#Interrupt when pir deactivates
def pirInterruptFalling(pin):
	led1.ledOff()
	msg = 'PIR Deactivated'
	client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
	print(msg)