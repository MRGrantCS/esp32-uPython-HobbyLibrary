from mhrd_sensor import MHRD
from led_handler import ledClass
from machine import Pin

'''
NOTE - using interupts is problematic and may not lead to desired results without additional coding
'''

'''
Example code for using mhrd water sensor with esp32
- Interrupts 
- Loop
'''

waterSensor = MHRD(4)
led1 = ledClass(2)

#Function using interupts
def mhrdIRQ ():
  waterSensor.mhrd.irq(trigger = Pin.IRQ_RISING, handler = interruptRising)

#Interrupt when pir activated
def interruptRising(pin):
  print ("Water detected")
  led1.ledChange()


#Function using loop
def mhrdLoop():
  while True:
    if waterSensor.waterDetected() == True:
      print ("Water Detected!")
      led1.ledOn()
    else:
      led1.ledOff()

