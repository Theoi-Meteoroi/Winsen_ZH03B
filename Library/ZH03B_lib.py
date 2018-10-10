#!/usr/bin/python3
#
#   v0.8  ZH03B_lib.py
#   9/7/2018  Dave Thompson
#
#   ZH03B Python3 Library
#
#   Caller needs to keep track of sleep, Q&A modes in use. No state stored.
#   Modify PORT setting below for your specific device entry.
#
#
import binascii
import serial
import time

ser = serial.Serial(
 port='/dev/ttyUSB1',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=10
)



ser.flushInput() #flush input buffer

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

def SetQA():
    """
    Set ZH03B Question and Answer mode
    Returns:  Nothing
    """
    ser.write( b"\xFF\x01\x78\x41\x00\x00\x00\x00\x46")
    return

def SetStream():
    """
    Set to default streaming mode of readings
    Returns: Nothing
    """
    ser.write( b"\xFF\x01\x78\x40\x00\x00\x00\x00\x47")
    return

def QAReadSample():
    """
    Q&A mode requires a command to obtain a reading sample
    Returns: int PM1, int PM25, int PM10
    """

    ser.flushInput() #flush input buffer
    ser.write( b"\xFF\x01\x86\x00\x00\x00\x00\x00\x79")
    reading = HexToByte( ((binascii.hexlify(ser.read(2))).hex()) )
    PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
    PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
    PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
    return( PM1, PM25, PM10 )

########

def DormantMode(pwr_status):
    """
    Turn dormant mode on or off. Must be on to measure.
    """
    #  Turn fan off
    #
    if pwr_status == "sleep":
       ser.write( b"\xFF\x01\xA7\x01\x00\x00\x00\x00\x57")
       response = HexToByte( ((binascii.hexlify(ser.read(3))).hex()) )
       if response == "ffa701":
          ser.flushInput() #flush input buffer
          return ("FanOFF")
       else:
          ser.flushInput() #flush input buffer
          return ("FanERROR")


    #  Turn fan on
    #
    if pwr_status == "run":
       ser.write( b"\xFF\x01\xA7\x00\x00\x00\x00\x00\x58")
       response = HexToByte( ((binascii.hexlify(ser.read(2))).hex()) )
       if response == "ffa701":
          ser.flushInput() #flush input buffer
          return ("FanON")
       else:
          ser.flushInput() #flush input buffer
          return ("FanERROR")


########

def ReadSample():
    """
    Read exactly one sample from the default mode streaming samples
    """
    ser.flushInput() #flush input buffer
    sampled = False
    while not sampled:
      reading = HexToByte( ((binascii.hexlify(ser.read(2))).hex()) )
      if reading == "424d":
          sampled = True
          status = ser.read(8)
          PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          return ( PM1, PM25, PM10 )
      else:
        continue

########
#
#  End File
#
