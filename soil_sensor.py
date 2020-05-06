from machine import Pin, ADC
#Imports dictionary that defines what pins can be used for inputs
from gpioDicts import inputsDict, adcDict

'''
Soil Moisture Sensor sensor driver Interface

init:
pushSwitch(input pin number)

external methods:
movementDeteced(no args) - checks state of pin, if high then returns true

NOTE: Only pins in the inputsDict can be assigned for inputs
'''


class soilSensor:
  def __init__(self, pin):
    self.pin = pin

    try:
      #check if pin is available for input by checking dictionary of GPIOs
      if pin in inputsDict :
        self.soil = Pin(pin,Pin.IN,Pin.PULL_UP)
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', inputsDict)
  
  def moistureDetected(self):
    moisture = False
    if self.soil.value() == 0:
      moisture = True
    return moisture

class soilADC:
  def __init__(self, pin):
    self.pin = pin
    try:
      #check if pin is available for input by checking dictionary of GPIOs
      if pin in adcDict :
        self.soil = ADC(Pin(pin))
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for ADC')
      print('Choose from:', adcDict)
  
  def moistureLevel(self):
    moisture = self.soil.read()
    return moisture