from machine import Pin
#Imports dictionary that defines what pins can be used for inputs
from gpioDicts import inputsDict

'''
Rain/Water Sensor sensor driver Interface

init:
pushSwitch(input pin number)

external methods:
movementDeteced(no args) - checks state of pin, if high then returns true

NOTE: Only pins in the inputsDict can be assigned for inputs
'''


class MHRD:
  def __init__(self, pin):
    self.pin = pin

    try:
      #check if pin is available for input by checking dictionary of GPIOs
      if pin in inputsDict :
        self.mhrd = Pin(pin,Pin.IN,Pin.PULL_UP)
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', inputsDict)
  
  def waterDetected(self):
    water = False
    if self.mhrd.value() == 0:
      water = True
    return water