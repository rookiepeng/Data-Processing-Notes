%% example MATLAB code to plot data saved by "voltageControlledSweep_1Voltage.py"
% By Z. Peng
% Sep. 19, 2015

%%
close all;
clear;

%% configuration
targetF=23.6e9; % The frequency to be ploted 
strAmp1='SampleData_voltageControlledSweep_1Voltage/amp 20160908 104125';
strPhs1='SampleData_voltageControlledSweep_1Voltage/phs 20160908 104125';

%%
startF=20e9;    % should be the same as the setup of the VNA
stopF=30e9;     % should be the same as the setup of the VNA
deltaF=(stopF-startF)/1600;
Freq=startF:deltaF:stopF;
Voltage=0:1:800;

amp1=importdata(strAmp1);
phs1=importdata(strPhs1);

[r,c]=size(amp1);

%% Plot all the amplitude data, Amplitude v.s. Frequency
figure;
for i=1:r
    plot(Freq,amp1(i,:));
    hold on;
end
hold off;
xlabel('Frequency (Hz)');
ylabel('Amplitude (dB)');

%% Plot all the phase data, Phase v.s. Frequency
figure;
for i=1:r
    plot(Freq,phs1(i,:));
    hold on;
end
hold off;
xlabel('Frequency (Hz)');
ylabel('Phase (degree)');

%% Plot the amplitude data at targetF, Amplitude v.s. Bias voltage
figure;
fNum=fix((targetF-startF)/deltaF)+1;
plot(Voltage,amp1(:,fNum));
xlabel('Bias voltage (mV)');
ylabel('Amplitude (dB)');

%% Plot the phase data at targetF, Phase v.s. Bias voltage
figure;
fNum=fix((targetF-startF)/deltaF)+1;
phs1c=phs1(:,fNum);
plot(Voltage,phs1c-min(phs1c));
hold off;
xlabel('Bias voltage (mV)');
ylabel('Phase (degree)');
