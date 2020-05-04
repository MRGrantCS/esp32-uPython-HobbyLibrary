from led_handler import ledClass
from hcsr04_sensor import HCSR04
from button_handler import buttonClass
import time

trig = 18
echo = 19

LED1 = 2
LED2 = 5

button1 = 33

button = buttonClass(button1)

ledGreen = ledClass(LED1)
ledOrange = ledClass(LED2)

sensor = HCSR04(trig,echo)

while True:
  distance = sensor.distance_cm()
  print('Distance:', distance, 'cm')
  #time.sleep(1)
  if distance <= 5:
    ledGreen.ledOff()
    ledOrange.ledOn()
  elif distance > 5 and distance <= 10:
    ledGreen.ledOn()
    ledOrange.ledOn()
  else:
    ledGreen.ledOn()
    ledOrange.ledOff()
  
  if button.buttonPressed() == True:
    for i in 3:
      ledGreen.ledBlink()
      ledOrange.ledBlink()
  