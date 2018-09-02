## Winsen ZH03B Particle Detector 

This project is a Python3 program to obtain a single sample of particle density from a ZH03B detector attached to a Raspberry Pi USB port.  The specific port is currently hard-coded to /dev/ttyUSB1. The code has only been tested over a USB bridge interface (CP2102).  To make readings continuous - modify the while-loop to always be TRUE. This program is not compatible with Python2.

Sample reading:

###                      PM1 level:  60 PM2.5 level:  121 PM10 level:  149


See the wiki for more information on the device and how to connect.

This project is licensed under the terms of the GPL v3 license

Sensors can be obtained here:

https://www.ebay.com/str/winsenelectronics
