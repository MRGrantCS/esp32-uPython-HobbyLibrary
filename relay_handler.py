from machine import Pin
#Imports dictionary that defines what pins can be used for outputs
from gpioDicts import outputsDict

'''
Relay Interface

init:
oneChnlRelay(output pin number)

external methods:
relayOn(no args) - sets pin for relay object to High
relayOff(no args) - sets pin for relay object to Low

NOTE: Only pins in the outputsDict can be assigned for leds
'''

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

  #Relay is on when V is low
  def relayOn (self):
    self.relay.value(0)
  #Relay is off when V is high
  def relayOff (self):
    self.relay.value(1)
