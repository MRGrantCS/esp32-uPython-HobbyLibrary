from machine import Pin
#Imports dictionary that defines what pins can be used for inputs
from gpioDicts import inputsDict

class buttonClass:
  def __init__ (self, pin):
  self.pin = pin 
  try:
    #check if pin is available for Button by checking dictionary of GPIOs
    if pin in inputsDict :
      self.button = Pin(pin,Pin.OUT,Pin.PULL_UP)
    else:
      raise OSError
  except OSError:      
    print('GPIO not suitable for Button')
    print('Choose from:', inputsDict)
  
  def buttonPress(self):
    pressed = False
    if button.value(1) == True:
      pressed = True
    return pressed