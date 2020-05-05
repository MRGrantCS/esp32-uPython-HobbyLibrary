from led_handler import ledClass
from ky037_sensor import KY037
from machine import Pin
import time

'''
NOTE - using IRQ for KY037 can lead to unexpected interrupts as it may detect multiple interrupts and then queue them up
'''

#button assigned to pin 33
mic = 33
micSensor = KY037(mic)

#leds assigned to pin 2 and 5
LED1 = 2
ledGreen = ledClass(LED1)

#function for button interupt that checks distance
def micIRQ():
  micSensor.mic.irq(trigger = Pin.IRQ_RISING, handler = interruptRising)

#Interrupt when button pushed
def interruptRising(pin):
  ledGreen.ledChange()
  time.sleep(1)


#function for a loop that constantly checks
def micLoop():
  while True:
    if micSensor.soundDetected() == True:
      ledGreen.ledChange()
      time.sleep(1)