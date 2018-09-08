#!/usr/bin/python3
# coding=utf-8
#
#  v0.1  9/1/2018   Winsen_ZH03B.py
# 
#  Released under GPL v3 License
#
# Modify PORT setting below for your specific device entry.
#
import serial
import binascii

ser = serial.Serial(
 port='/dev/ttyUSB1',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)

def HexToByte( hexStr ):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )

    bytes = []

    hexStr = ''.join( hexStr.split(" ") )

    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

    return ''.join( bytes )

ser.flushInput() #flush input buffer

sampled = False

while not sampled:

  sample = ser.read(2)

#blank line check filter
  if sample != b'':
    reading = HexToByte( ((binascii.hexlify(sample)).hex()) )
    if reading == "424d":            # Start of data frame
       sampled = True                # Sample will be captured
       status = ser.read(8)          # Discard internal status bytes
       PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
       PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
       PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
       print ("PM1 level: ", PM1, end="")
       print (" PM2.5 level: ", PM25, end="")
       print (" PM10 level: ", PM10 )
  else:
    continue

