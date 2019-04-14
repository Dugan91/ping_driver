import pty
import serial
import os
import threading
import fcntl


master, slave = pty.openpty()
master_name = os.ttyname(master)
slave_name = os.ttyname(slave)
ser = serial.Serial(master_name, 115200, timeout = 2)

print("master: " + master_name)
print("slave: " + slave_name)

raw_input("Press enter to continue:")


while 1:
    s = ser.read(20) 
    
    print(s)


