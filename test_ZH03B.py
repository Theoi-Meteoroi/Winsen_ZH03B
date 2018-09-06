# coding=utf-8
#
#  v0.2  9/1/2018   Winsen_ZH03B.py
#
#  Released under GPL v3 License
#
# Modify PORT setting below for your specific device entry.
#
from ZH03B_library import ReadSample
import binascii
import serial
import time

ser = serial.Serial(
 port='/dev/ttyUSB1',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
ser.flushInput() #flush input buffer

power_flag = "ON"

PM1, PM25, PM10 = ReadSample()

print (PM1)
print (PM25)
print (PM10)
time.sleep (5)


