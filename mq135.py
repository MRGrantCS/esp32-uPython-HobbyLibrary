import machine
import math
import time

adc = machine.ADC(0)

# Define some constants for MQ135
RLOAD = 10.0  # Load resistance in kilo ohms
RLZERO = 76.63  # Resistance of the sensor in clean air

# Parameters for the Steinhart-Hart equation for temperature
A = 0.001129148
B = 0.000234125
C = 0.0000000876741

# Parameters for the linear equation for humidity
HUMIDITY_SLOPE = 0.0062
HUMIDITY_INTERCEPT = 0.16

def read_mq135():
    # Read the ADC value and convert to voltage
    adc_value = adc.read()
    voltage = adc_value * 3.3 / 65535.0

    # Calculate the resistance of the sensor
    rs = RLOAD * (3.3 - voltage) / voltage

    # Calculate the ratio of rs/ro (ro is the sensor resistance in clean air)
    ratio = rs / RLZERO

    # Calculate the temperature using the Steinhart-Hart equation
    resistance = 10000.0 * (1.0 / ratio - 1.0)
    temperature = 1.0 / (A + B * math.log(resistance) + C * math.pow(math.log(resistance), 3)) - 273.15

    # Calculate the humidity
    humidity = 50  # Replace with actual humidity value in percent

    # Calculate the correction factor for humidity
    corr_factor = 1.0 + HUMIDITY_SLOPE * (humidity - 33.0) + HUMIDITY_INTERCEPT

    # Calculate the corrected ratio
    ratio_corr = ratio * corr_factor

    # Calculate the ppm of CO2
    ppm = math.pow(10.0, ((math.log10(ratio_corr) - 2.986) / -0.401))

    return ppm

# Read the value from MQ135 sensor and print the ppm of CO2
while True:
    ppm = read_mq135()
    print("CO2 ppm: {:.2f}".format(ppm))
    time.sleep(1)
