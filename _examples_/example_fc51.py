from fc51_sensor import FC51
from led_handler import ledClass
from machine import Pin

'''
NOTE - using interupts is problematic and may not lead to desired results without additional coding
'''

'''
Example code for using FC51 obstacle detection sensor with esp32
- Interrupts 
- Loop
'''

obstacleSensor = FC51(4)
led1 = ledClass(2)

#Function using interupts
def fc51IRQ ():
  obstacleSensor.fc51.irq(trigger = Pin.IRQ_RISING, handler = interruptRising)

#Interrupt when pir activated
def interruptRising(pin):
  print ("Obstacle detected")
  led1.ledChange()


#Function using loop
def fc51Loop():
  while True:
    if obstacleSensor.obstacleDetected() == True:
      print ("Obstacle Detected!")
      led1.ledOn()
    else:
      led1.ledOff()

