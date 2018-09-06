#!/usr/bin/python3
#
#   v0.2  ZH03B_library.py
#   9/5/2018  Dave Thompson
#
#   ZH03B Python3 Library
#
#   Caller needs to keep track of Q&A mode in use. No state stored.
#
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
 timeout=1
)
#  ser.flushInput() #flush input buffer

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

    ser.write( b'0xFF, 0x01, 0x78, 0x41, 0x00, 0x00, 0x00, 0x00, 0x46')
    return

def SetStream():
    """
    Set to default streaming mode of readings
    Returns: Nothing
    """

    ser.write( b'0xFF, 0x01, 0x78, 0x40, 0x00, 0x00, 0x00, 0x00, 0x47')
    return

def QAgetsample():
    """
    Q&A mode requires a command to obtain a reading sample
    Returns: int PM1, int PM25, int PM10
    Fail immediately if we cannot turn on the fan if we are dormant.
    """

    if pwr-flag == "ERROR":
       return (pwr-flag)

    if pwr-flag == "OFF":
       DormantMode( "ON" )
       time.sleep(1)
       ser.write( b'0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79')
       sampled = False
       while sampled != True:
         sample = ser.read(2)
         if sample != b'':             # blank line check filter
            reading = HexToByte( ((binascii.hexlify(sample)).hex()) )
            if reading == "FF86":
              sampled = True
              status = ser.read(8)
              PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              print ("PM1 level: ", PM1, end="")
              print (" PM2.5 level: ", PM25, end="")
              print (" PM10 level: ", PM10 )
              DormantMode( "OFF" )
              return ( PM1, PM25, PM10 )
         else:
          continue
    else:
       ser.write( b'0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79')
       sampled = False
       while sampled != True:
         sample = ser.read(2)
         if sample != b'':             # blank line check filter
            reading = HexToByte( ((binascii.hexlify(sample)).hex()) )
            if reading == "FF86":
              sampled = True
              status = ser.read(8)
              PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
              print ("PM1 level: ", PM1, end="")
              print (" PM2.5 level: ", PM25, end="")
              print (" PM10 level: ", PM10 )
              sampled = false
              return ( PM1, PM25, PM10 )

         else:
             continue

def DormantMode(pwr_status):
    """
    Turn dormant mode on or off. Must be on to measure.
    """

    if pwr_status == "ON":
       ser.write( b'0xFF, 0x01, 0xA7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x56')
       sampled = False
       while sampled != "True":
         status = ser.read(2)
         if status != b'':
           status =  HexToByte( ((binascii.hexlify(status)).hex()) )
           if status == "FFA7":
            sampled = "True"
            status = int(HexToByte( ((binascii.hexlify(ser.read(1))).hex()) ),16)
           if status == "1":
            pwr_status = "ON"
           if status == "0":
            pwr_status = "ERROR"
            return (pwr_status)
         else:
           continue
    if pwr_status == "OFF":
       ser.write( b'0xFF, 0x01, 0xA7, 0x01, 0x00, 0x00, 0x00, 0x00, 0x57')
       sampled = False
       while sampled != "True":
         status = ser.read(2)
         if status != b'':
           status =  HexToByte( ((binascii.hexlify(status)).hex()) )
           if status == "FFA7":
             sampled = "True"
             status = int(HexToByte( ((binascii.hexlify(ser.read(1))).hex()) ),16)
           if status == "1":
             pwr_status = "OFF"
           if status == "0":
             pwr_status = "ERROR"
             return (pwr_status)
         else:
            continue

def ReadSample():
    """
    Read exactly one sample from the default mode streaming samples
    """
    ser.flushInput() #flush input buffer
    sampled = False
    while not sampled:
      sample = ser.read(2)
    #blank line check filter
      if sample != b'':
        reading = HexToByte( ((binascii.hexlify(sample)).hex()) )
        if reading == "424d":
          sampled = True
          status = ser.read(8)
          PM1 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          PM25 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          PM10 = int(HexToByte( ((binascii.hexlify(ser.read(2))).hex()) ),16)
          return  PM1, PM25, PM10
      else:
        continue
#
#  End File
#
