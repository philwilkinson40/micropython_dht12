#basic use of dht12 library with esp8266

import dht12
import machine

i2c = machine.I2C(sda = machine.Pin(4), scl = machine.Pin(5))
sensor = dht12.DHT12(i2c)

sensor.measure()

print(sensor.temperature())
print(sensor.humidity())
