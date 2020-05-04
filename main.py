from led_Handler import ledClass
from hcsr04_Sensor import HCSR04
import time

trig = 18
echo = 19

LED1 = 2
LED2 = 5

ledGreen = ledClass(LED1)
ledOrange = ledClass(LED2)

sensor = HCSR04(trig,echo)

while True:
  distance = sensor.distance_cm()
  print('Distance:', distance, 'cm')
  time.sleep(1)
  if distance <= 5:
    ledGreen.ledOff()
    ledOrange.ledOn()
  elif distance > 5 and distance <= 10:
    ledGreen.ledOn()
    ledOrange.ledOn()
  else:
    ledGreen.ledOn()
    ledOrange.ledOff()