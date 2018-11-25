# RF Test Scripts (Unmaintained)

Python Scripts for RF testing through GPIB.

## VNA

Obtain measurement data from Agilent 8722ES Vector Network Analyzer (VNA).

### Dependence

- Python 3.X
- PyVISA
- National Instruments 488.2 driver
- Agilent 8722ES Vector Network Analyzer

### File discription

- ```S11.py```: Obtain S11 data from VNA.
- ```S12.py```: Obtain S12 data from VNA.
- ```S21.py```: Obtain S21 data from VNA.  
- ```S22.py```: Obtain S22 data from VNA.

## Antenna

Antenna pattern measurement by Agilent 8722ES Vector Network Analyzer.

### Dependence

- Python 3.X
- PyVISA
- National Instruments 488.2 driver
- Agilent 8722ES Vector Network Analyzer

### File discription

- ```antenna_pattern.py```: Antenna pattern measurement (Antenna should be rotated by other equipment).

## VoltageControlled

2-port Voltage Controlled Component S-Parameter Measurement.

### Dependence

- Python 3.X
- PyVISA
- National Instruments 488.2 driver
- Agilent 8722ES Vector Network Analyzer
- Keysight B2962A Power Source
- Tektronix PS2520G Power Source (power supply for *VoltageControlled/multiPointSweep_2Voltages_1Supply.py*)

### File discription

- ```voltageControlledSweep_1Voltage.py```: Sweep a control voltage and obtain corresponding S21 data.
- ```fullFreqSweep_2Voltages.py```: Sweep two control voltages and obtain S21 data of the whole frequency range set in the VNA.
- ```multiPointSweep_2Voltages.py```: Sweep two control voltages and obtain S21 data of specificed frequency points.
- ```multiPointSweep_2Voltages_1Supply.py```: Sweep two control voltages and obtain S21 data of specificed frequency points with automatic power supply.

