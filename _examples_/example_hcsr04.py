from led_handler import ledClass
from hcsr04_sensor import HCSR04
from button_handler import pushButton
from machine import Pin
import time

'''
WARNING - the output of the HCSR04 is 5v, however most GPIOS accept 3.3v. Use a voltage divider (2:1 resistance) to redice the voltage
Example wiring: https://stevieb9.github.io/rpi-hcsr04/hcsr04.png
'''

#button assigned to pin 33
button1 = 33
button = pushButton(button1)

#leds assigned to pin 2 and 5
LED1 = 2
LED2 = 5
ledGreen = ledClass(LED1)
ledOrange = ledClass(LED2)

#trigger signal OUT on pin 18
#eho signal IN on pin 19
trig = 18
echo = 19
sensor = HCSR04(trig,echo)

#function for button interupt that checks distance
def buttonIRQ():
  button.button.irq(trigger = Pin.IRQ_FALLING, handler = interruptFalling)

#Interrupt when button pushed
def interruptFalling(pin):
  #trigger signal OUT on pin 18
  #eho signal IN on pin 19
  print ("Distance is", sensor.distance_cm(), "cm")


#function for a loop that constantly checks
def ultrasonicLoop():
  while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')
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