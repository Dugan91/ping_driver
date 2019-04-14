import pty
import serial
import os



ser = serial.Serial('/dev/ptmx',115200)
while 1:
    ser.write(b'Hello world')

ser.close()


