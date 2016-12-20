#!/usr/bin/python

####
# Antenna Pattern Measurement
# Python 3.x
#
# Instruments:
#        1) Agilent 8722ES Vector Network Analyzer
#
# Required driver:
#        1) National Instruments 488.2 driver
#
# Required Python Library:
#        1) PyVISA
#
# Saved data file:
#        1) "Mag <startAngle>_<stopAngle>_<step>_<timestamp>": Magnitude data in dB
#                              angle1[amp(f1),amp(f2),...,amp(fn)]
#                              angle2[amp(f1),amp(f2),...,amp(fn)]
#                              ...
#                              angleN[amp(f1),amp(f2),...,amp(fn)]
#        2) "Phs <startAngle>_<stopAngle>_<step>_<timestamp>": Phase data in degree
#                              angle1[phs(f1),phs(f2),...,phs(fn)]
#                              angle2[phs(f1),phs(f2),...,phs(fn)]
#                              ...
#                              angleN[phs(f1),phs(f2),...,phs(fn)]
#
# Version 1
#
# By: Zhengyu Peng
#     zhengyu.peng@ttu.edu
#     Feb. 25, 2016
####

import datetime
import time
import visa

now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d %H%M%S")

rm = visa.ResourceManager()
res = rm.list_resources()
for x in range(0, len(res)):    # list all the GPIB devices
	print("{}. ".format(x) + res[x] + ", ", end="")
print("\n")

vnaNumber = input('Select the VNA Number --> ') # select the device in use
vna = rm.open_resource(res[int(vnaNumber)])
print(vna.query("*IDN?"))

vna.write("S21")    # select S21
vna.write("FORM4")  # select readout format

angleStart = int(input('Angle start from (Degree) --> '))   #
angleStop = int(input('Angle stop to (Degree) --> '))
angleStep = int(input('Angle rotating step (Degree) --> '))

megName='Mag ' + str(angleStart) + '_' + str(angleStop) + '_' + str(angleStep) + '_' + timestamp
phsName='Phs ' + str(angleStart) + '_' + str(angleStop) + '_' + str(angleStep) + '_' + timestamp

for angle in range (angleStart, angleStop+angleStep, angleStep):

    measure = input('Press enter to measure ' + str(angle) + '(Degree) --> ')
    
    print("-> Change to Log Mag View")
    vna.write("LOGM")
    time.sleep(1)	# 5s
    print("-> Read Log Mag Data")
    vna.write("OUTPFORM")
    meg = vna.read_raw()
    meg = meg.decode("utf-8")
    meg = meg.replace('0.000000000000000E+00\n', '')
    meg = meg.replace(' ', '')
    meg = meg[:len(meg)-1]

    print("-> Change to Phase View")
    vna.write("PHAS")
    time.sleep(1)	# 5s
    print("-> Read Phase Data\n")
    vna.write("OUTPFORM")
    phs = vna.read_raw()
    phs = phs.decode("utf-8")
    phs = phs.replace('0.000000000000000E+00\n', '')
    phs = phs.replace(' ', '')
    phs = phs[:len(phs)-1]

    famp = open(megName, 'a')
    famp.write(meg + "\n")
    famp.close()

    fphs = open(phsName, 'a')
    fphs.write(phs + "\n")
    fphs.close()

vna.close()
print("--Finish--")
