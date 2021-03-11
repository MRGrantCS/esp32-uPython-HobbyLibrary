from time import sleep
from machine import Pin
from dht import DHT11
import network
import urequests

import esp
esp.osdebug(None)

import gc
gc.collect()

SSID = ""
PASS = ""
api_key = ""

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, PASS)

while station.isconnected() == False:
	pass

print("Connection Complete")
print(station.ifconfig())

sensor = DHT11(Pin(26))

def getDHT11():
	sensor.measure() 
	temp = sensor.temperature()
	humid = sensor.humidity()

	sensor_reading = {"value1":temp, "value2":humid}
	print(sensor_reading)

	return sensor_reading

while True:
	try:
		sensor_reading = getDHT11()
		request_headers = {"Content-Type":"application/json"}

		request = urequests.post(
			"https://maker.ifttt.com/trigger/dht11/with/key/" + api_key,
			json=sensor_reading,
			headers = request_headers
		)
		print(request.text)
		request.close()

	except:
		print('process failed')
	#What 5 minutes
	sleep(300)

