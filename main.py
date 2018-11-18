#basic use of dht12 library with esp8266

import dht12
import machine

i2c = machine.I2C(sda = machine.Pin(4), scl = machine.Pin(5))

'''
confirm your device is present on the bus
it should return [92] for this particular sensor
if this returns nothing, check your wiring
then check the Pin GPIO numbers are correct 
'''

print(i2c.scan())

sensor = dht12.DHT12(i2c)

sensor.measure()

print(sensor.temperature())
print(sensor.humidity())
