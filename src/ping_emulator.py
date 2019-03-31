import pty
import serial
import os

master, slave = pty.openpty()
master_name = os.ttyname(master)
slave_name = os.ttyname(slave)
ser = serial.Serial(slave_name, 115200, timeout = 0)

print(master_name)
raw_input("Press enter to continue:")

while 1:
    s = ser.read(20)
    print(s)

