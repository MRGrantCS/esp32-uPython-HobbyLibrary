from machine import Pin
#Imports dictionary that defines what pins can be used for outputs
from gpioDicts import outputsDict

import utime as time

'''
Relay Interface

init:
ledClass(output pin number)

external methods:
ledOn(no args) - sets pin for led object to High
ledOff(no args) - sets pin for led object to Low
ledBlink(time interval) - turns on then off led with a defined time interval
blinkHanlder(pin) - interrupt handler to activate ledBlink

NOTE: Only pins in the outputsDict can be assigned for leds
'''

from machine import Pin

class oneChnlRelay:
  def __init__(self,pin):
    self.pin = pin
    
    try:
      #check if pin is available for LED by checking dictionary of GPIOs
      if pin in outputsDict :
        self.relay = Pin(pin,Pin.OUT,Pin.PULL_DOWN)
        self.relayOff()
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', outputsDict)


  def relayOff (self):
    self.relay.value(0)

  def relayOn (self):
    self.relay.value(1)