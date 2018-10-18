# Winsen ZH03B Particle Detector 


This project is a Python3 program and function library to obtain sample readings of particle density from a ZH03B detector attached to a Raspberry Pi USB port.  The specific port is currently hard-coded to /dev/ttyUSB1. The code has only been tested over a USB bridge interface (CP2102) on Raspian Stretch and OSx High Sierra.   

### Manual / Datasheet 
### https://www.winsen-sensor.com/d/files/air-quality/zh03-series-laser-dust-module-v2_0.pdf

### USB-UART driver for CP2102
### https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

### Files

Winsen_ZH03B.py - obtain exactly one single sample reading from sensor running in default 'streaming readings' mode. 
                  To make readings continuous -  modify the while-loop to always be TRUE. This program is not compatible with 
                  Python2. This program does not utilize the function library and is standalone.
                  
Library/test_ZH03B_lib.py - Exercise the function library in a loop

Library/ZH03B_lib.py  - Complete function library for the ZH03B. Enable/Disable sample fan to save power. Not compatible with Python2
       
 ### Running the program -
 <prompt> python3 Winsen_ZH03B.py

Sample reading:

###   PM1 level:  60 PM2.5 level:  121 PM10 level:  149


See the [wiki](https://github.com/Theoi-Meteoroi/Winsen_ZH03B/wiki) for more information on the device and how to connect.

This project is licensed under the terms of the GPL v3 license

Sensors can be obtained here:

<a href="https://www.tindie.com/stores/CarbonCycle/?ref=offsite_badges&utm_source=sellers_CarbonCycle&utm_medium=badges&utm_campaign=badge_medium"><img src="https://d2ss6ovg47m0r5.cloudfront.net/badges/tindie-mediums.png" alt="I sell on Tindie" width="150" height="78"></a>
