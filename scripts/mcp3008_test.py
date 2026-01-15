import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.maxSpeedHz = 1000000

def readADC(channel):
    resp = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((resp[1] & 3) << 8) | resp[2]

print("MCP3008 test running (CTRL+c to stop)")

try:
    while True:
        value = readADC(0)
        print("ADC value:", value)
        time.sleep(0.2)

except KeyboardInterrupt:
    spi.close()
    print("\nStopped.")