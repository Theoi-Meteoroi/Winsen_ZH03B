# CircuitPython example code
# v0.1  
# Tested with CircuitPython 5.0 on ItsyBitsy M4
# +5v (USB) pin used to power sensor.
# requires install of the adafruit_binascii library.

import board
import busio
import digitalio
from adafruit_binascii import hexlify

uart = busio.UART(board.TX, board.RX, baudrate=9600)

while True:
 sampled = False
 while not sampled:
  sample = uart.read(2)

#blank line check filter
  if sample != None:
    reading = sample
    if reading == b'BM':            # Start of data frame
       sampled = True                # Sample will be captured
       status = uart.read(8)          # Discard internal status bytes
       PM1 = int((hexlify(uart.read(2))),16)
       PM25 = int((hexlify(uart.read(2))),16)
       PM10 = int((hexlify(uart.read(2))),16)
       print ("PM1 level: ", PM1, end="")
       print (" PM2.5 level: ", PM25, end="")
       print (" PM10 level: ", PM10 )
  else:
    continue
