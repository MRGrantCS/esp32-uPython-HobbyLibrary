from pir_sensor import pirClass
from led_handler import ledClass
from machine import Pin

'''
Example code for using PIR sensor with esp32
- Interrupts 
- Loop
'''
pirRising = pirClass(4)
pirFalling = pirClass(33)
led1 = ledClass(2)

#Function using interupts
def pirIRQ ():
  pirRising.pir.irq(trigger = Pin.IRQ_RISING, handler = pirInterruptRising)

  pirFalling.pir.irq(trigger = Pin.IRQ_FALLING, handler = pirInterruptFalling)

#Interrupt when pir activated
def pirInterruptRising(pin):
  print ("PIR Activated")
  led1.ledOn()
#Interrupt when pir deactivates
def pirInterruptFalling(pin):
  print ("PIR Deactivated")
  led1.ledOff()


#Function using loop
def pirLoop():
  while True:
    if pirRising.movementDetected() == True:
      print ("PIR Activated")
      led1.ledOn()
    else:
      print ("PIR Deactivated")
      led1.ledOff()

