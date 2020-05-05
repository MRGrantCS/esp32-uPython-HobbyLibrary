from machine import Pin
#Imports dictionary that defines what pins can be used for outputs
from gpioDicts import outputsDict

import utime as time

'''
LED Interface

init:
ledClass(output pin number)

external methods:
ledOn(no args) - sets pin for led object to High
ledOff(no args) - sets pin for led object to Low
ledBlink(time interval) - turns on then off led with a defined time interval
blinkHanlder(pin) - interrupt handler to activate ledBlink

NOTE: Only pins in the outputsDict can be assigned for leds
'''

class ledClass:
  def __init__ (self, pin):
    self.pin = pin
    
    try:
      #check if pin is available for LED by checking dictionary of GPIOs
      if pin in outputsDict :
        self.led = Pin(pin,Pin.OUT,Pin.PULL_DOWN)
        self.ledOff()
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', outputsDict)
    
  def ledOn(self):
    self.led.value(1)

  def ledOff(self):
      self.led.value(0)
  
  def ledBlink(self, interval):
    self.led.value(1)
    time.sleep(interval)
    self.led.value(0)
    time.sleep(interval)

  def blinkHandler(self,pinObj):
    self.ledBlink(0.5)
    