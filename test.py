import time
from ina_219_smbus import ina219_i2c

ina219=ina219_i2c()

#ina219.set_cal(4096)
while(True):
	print(ina219.get_bus_voltage(),ina219.get_current(mA=False),ina219.get_power(mW=False))
	time.sleep(1)
