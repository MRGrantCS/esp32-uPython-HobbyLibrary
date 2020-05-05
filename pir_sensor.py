from machine import Pin
#Imports dictionary that defines what pins can be used for inputs
from gpioDicts import inputsDict
'''
PIR sensor driver Interface

init:
pushSwitch(input pin number)

external methods:
movementDeteced(no args) - checks state of pin, if high then returns true

NOTE: Only pins in the inputsDict can be assigned for inputs
'''


class pirClass:
  def __init__(self, pin):
    self.pin = pin

    try:
      #check if pin is available for input by checking dictionary of GPIOs
      if pin in inputsDict :
        self.pir = Pin(pin,Pin.IN,Pin.PULL_UP)
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', inputsDict)
  
  def movementDetected(self):
    movement = False
    if self.pir.value() == 1:
      movement = True
    return movement