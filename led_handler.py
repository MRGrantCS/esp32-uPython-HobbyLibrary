from machine import Pin
#Imports dictionary that defines what pins can be used for outputs
from gpioDicts import outputsDict

'''
Interface

init:
ledClass(output pin number)

external methods:
ledOn(no args) - sets pin for led object to High
ledOff(no args) - sets pin for led object to Low

NOTE: Only pins in the outputsDict can be assigned for leds
'''

class ledClass:
  def __init__ (self, pin):


    self.pin = pin
    
    try:
      #check if pin is available for LED by checking dictionary of GPIOs
      if pin in outputsDict :
        self.led = Pin(pin,Pin.OUT,pull=None)
        self.ledOff()
      else:
        raise OSError
    except OSError:      
      print('GPIO not suitable for LED')
      print('Choose from:', gpioDict)
    
  def ledOn(self):
    self.led.value(1)

  def ledOff(self):
      self.led.value(0)