# Only runs src/main.py
import os
import machine
import time

os.chdir("src")

led = machine.Pin("LED", machine.Pin.OUT)

try:
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
    led.on()
    time.sleep(0.25)
    led.off()
    exec(open("main.py").read())
except Exception as ex:
    os.chdir("..")
    led.on()
    raise ex

os.chdir("..")
