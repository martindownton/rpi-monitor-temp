import os
import time
from vcgencmd import Vcgencmd

def measure_temp():
        return Vcgencmd.measure_temp()

while True:
        os.system('clear')
        print(measure_temp())
        time.sleep(1)




