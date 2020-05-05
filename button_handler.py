from machine import Pin
#Imports dictionary that defines what pins can be used for inputs
from gpioDicts import inputsDict

'''
Interface

init:
pushSwitch(input pin number)

external methods:
buttonPressed(no args) - checks state of pin, if high then returns true

NOTE: Only pins in the inputsDict can be assigned for buttons
'''

class pushButton:
  def __init__ (self, pin):
    self.pin = pin 
    try:
      #check if pin is available for Button by checking dictionary of GPIOs
      if pin in inputsDict :
        self.button = Pin(pin,Pin.IN,Pin.PULL_UP)
      else:
        raise OSError
    except OSError:      
      print('GPIO', pin,'not suitable for Input')
      print('Choose from:', inputsDict)
  
  def buttonPressed(self):
    pressed = False
    #using a pull-up resistor, so input is 1 by default and must test if is 0, which shows button is pressed
    if self.button.value() == 0:
      pressed = True
    return pressed
    
    
