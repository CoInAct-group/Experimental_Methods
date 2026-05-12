

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

if not ports:
    print("No serial ports found.") 
else:
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

#%%