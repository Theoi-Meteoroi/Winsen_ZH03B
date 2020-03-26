# coding=utf-8
#
#  v0.5  9/1/2018   test_ZH03Blib.py
#
#  Released under GPL v3 License
#
# Modify PORT setting below for your specific device entry.
#
from ZH03B_lib import ReadSample, SetQA, QAReadSample, SetStream, DormantMode
import binascii
import serial
import time

test_status = 'run'

PM1, PM25, PM10 = ReadSample()
print ("ReadSample output - First iteration")
print (PM1)
print (PM25)
print (PM10)
time.sleep (.5)

loopcount = 0

while test_status is not "ERROR":

   print ("LoopCount=", loopcount)
   SetQA()
   print ("QA set")
   time.sleep(.05)
   PM1, PM25, PM10 = QAReadSample()
   print ("QA readsample", PM1, PM10, PM25)
   print (" Set back to stream ")
   SetStream()
   time.sleep(.05)
   PM1, PM25, PM10 = ReadSample()
   print ("Stream sample", PM1, PM10, PM25)


   print (" Set to QA, fan OFF, get return code and sleep 10 seconds ")
   test_status = DormantMode("sleep")
   print (test_status)

   time.sleep(10)

   print (" Set to QA, fan ON ,get return code and sleep 10 seconds  ")
   test_status = DormantMode("run")
   print (test_status)

   time.sleep(10)

   PM1, PM25, PM10 = QAReadSample()
   print( "Q&A take reading", PM1, PM10, PM25)
 
   time.sleep(2)

   PM1, PM25, PM10 = QAReadSample()
   print( "Q&A take reading", PM1, PM10, PM25)

   time.sleep(2)

   PM1, PM25, PM10 = QAReadSample()
   print( "Q&A take reading", PM1, PM10, PM25)

   SetStream()
   time.sleep(.1)
   PM1, PM25, PM10 = ReadSample()
   print ("ReadSample output - loop end", PM1, PM10, PM25)
   time.sleep (.5)

   loopcount = loopcount + 1
