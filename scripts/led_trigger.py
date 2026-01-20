import spidev
import time
from gpiozero import LED

#LED on GPIO27
led = LED(27)

#SPI setup
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def read_adc(channel):
    response = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((response[1] & 3) << 8) | response[2]

#Adjust this value
THRESHOLD = 400

print("IR + LED test running (CTRL+C to stop)")
print(f"Threshold set to {THRESHOLD}")

try:
    while True:
        value = read_adc(0)

        if value < THRESHOLD:
            led.on()
            print(f"OBJECT DETECTED | ADC={value}")
        else:
            led.off()
            print(f"Clear | ADC={value}")
        
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    led.off()
    spi.close()
    print("\nProgram terminated")