from gpiozero import DigitalInputDevice
import time

# DOUT connected to BCM GPIO17 (physical pin 11)
sensor = DigitalInputDevice(17, pull_up=True)

print("IR Proximity Sensor Test Started")
print("Press CTRL+C to stop\n")

try:
    while True:
        if sensor.value == 1:
            print("OBJECT DETECTED")
        else:
            print("Clear")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nStopped.")
