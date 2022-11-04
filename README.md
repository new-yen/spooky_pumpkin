# spooky_pumpkin
Rpi0 - Pumpkin with PIR sensor, triggering LEDs + sounds via Bluetooth speaker

Bluetool API used for controlling Bluetooth connection via Python script.
Taken from: https://github.com/emlid/bluetool

I only used "bluetool.py" and "bluezutils.py" as I only needed to check for an existing connection and in case of no connection, establish a connection with my Bluetooth speaker with known MAC address.
