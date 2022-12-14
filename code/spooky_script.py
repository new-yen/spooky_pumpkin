import random, os
from subprocess import call
from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep
from bluetool import Bluetooth

b = Bluetooth()

pir = MotionSensor(4)
led = LED(17)

def rndmp3():
    randomfile = random.choice(os.listdir("/home/pi/spooky_pumpkin/sounds/"))
    file = '/home/pi/spooky_pumpkin/sounds/' + randomfile
    call(["aplay", file])

while True:
    if b.get_connected_devices() == []:
        print("no device connected, scanning for 5 sec")
        b.scan(5)
        b.connect("C9:50:76:E4:38:AC")      #MAC address of my bluetooth speaker;paired and trusted beforehand via terminal & "bluetoothctl"
        print("connected")
    
    else:
        pir.wait_for_motion()
        print("motion detected")
        led.blink(on_time=0.2, off_time=0.2, n=10, background=True)
        rndmp3()
        led.blink(on_time=1, off_time=1, n=5, background=False)
        led.blink(on_time=5, off_time=0, n=1, background=False)
        sleep(5)

