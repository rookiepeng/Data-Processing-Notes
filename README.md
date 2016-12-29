# RF Measurement Automation
Python Scripts for RF Measurement Automation.

## VNA
Obtain measurement data from Agilent 8722ES Vector Network Analyzer (VNA).

    ### Dependence
    - Python 3.X
    - PyVISA
    - National Instruments 488.2 driver
    - Agilent 8722ES Vector Network Analyzer

    ### File discription
    #### *VNA/S11.py*
    Obtain S11 data from VNA.
    #### *VNA/S12.py*
    Obtain S12 data from VNA.
    #### *VNA/S21.py*
    Obtain S21 data from VNA.
    #### *VNA/S22.py*
    Obtain S22 data from VNA.

## Antenna
Antenna pattern measurement by Agilent 8722ES Vector Network Analyzer.
- *Antenna/antenna_pattern.py*: Antenna pattern measurement (Antenna should be rotated by other equipment).

## VoltageControlled
2-port Voltage Controlled Component S-Parameter Measurement.
- *VoltageControlled/voltageControlledSweep_1Voltage.py*: Sweep a control voltage and obtain corresponding S21 data.
- *VoltageControlled/fullFreqSweep_2Voltages.py*: Sweep two control voltages and obtain S21 data of the whole frequency range set in the VNA.
- *VoltageControlled/multiPointSweep_2Voltages.py*: Sweep two control voltages and obtain S21 data of specificed frequency points.
- *VoltageControlled/multiPointSweep_2Voltages_1Supply.py*: Sweep two control voltages and obtain S21 data of specificed frequency points with automatic power supply.
