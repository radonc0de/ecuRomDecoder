# ECU ROM Decoder

## Description

ECU ROMs are binary files that encode for constants that the vehicle uses to make decisions. Unfortunately, unless some ECU tuning software is being used, it is difficult to understand what exactly these files encode for. This is the start of a terminal app to read ECU binary files and output the tables that correspond to a particular parameter. By determining the locations where data is stored and the method used to encode it, I was able to start converting the raw memory saved in the ROM to easily readable tables.

## Features
### Primary Open Loop Fueling
Usage: `ecuRomDecoder.py --primary-ol-fueling [path to file]`

The Primary Open Loop Fueling feature will print a table of the Engine Speed (RPM) vs. Engine Load (g/rev) with corresponding Air/Fuel ratio values to the terminal. Getting this feature to work was the primary inspiration for creating this project as I'm currently working on [openEJ.io](https://openej.io) and this feature will make the process of scaling this table using [openEJ](https://openej.io) much simpler.

Sample Output:

```
ECU ID:  A4SG900C
---------  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
RPM\LOADS   0.22   0.4    0.58   0.76   0.9    1.04   1.17   1.3    1.44   1.58   1.68   1.78   1.9    1.98   2.06   2.14
800.0      14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7   14.7
1200.0     14.7   14.7   14.7   14.7   14.7   13.94  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54
1600.0     14.7   14.7   14.7   14.7   14.7   13.63  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54  13.54
2000.0     14.7   14.7   14.7   14.7   14.7   13.84  13.34  12.98  12.98  12.98  12.98  12.98  12.98  12.98  12.98  12.98
2400.0     14.7   14.7   14.7   14.7   14.7   13.73  13.54  13.34  13.16  13.16  12.89  12.54  12.46  12.46  12.46  12.46
2800.0     14.7   14.7   14.7   14.7   14.7   13.94  13.25  13.25  13.07  12.89  12.71  12.38  11.91  11.91  11.91  11.91
3200.0     14.7   14.7   14.7   14.7   14.7   13.84  13.34  13.34  13.25  12.8   12.46  12.14  11.61  11.61  11.61  11.61
3600.0     14.7   14.7   14.7   14.7   14.7   14.59  14.15  13.73  13.07  12.38  11.98  11.54  11.07  10.69  10.69  10.69
4000.0     14.7   14.7   14.7   14.7   14.36  13.84  13.54  13.07  12.46  11.61  11.2   10.81  10.63  10.51  10.51  10.51
4400.0     14.59  14.59  14.47  14.36  14.04  13.54  12.38  11.76  11.69  11     10.81  10.17  10.01  10.01  10.01  10.01
4800.0     14.47  14.47  13.34  12.71  11.83  11.54  11.54  11.13  10.75  10.69  10.34  10.17  10.01   9.6    9.6    9.6
5200.0     14.47  13.84  13.34  12.71  11.83  11.54  11.54  11.13  10.75  10.45  10.28  10.12   9.8    9.55   9.55   9.55
5600.0     14.15  13.54  13.16  12.38  11.83  11.54  11.54  11.13  10.75  10.4   10.12   9.9    9.7    9.7    9.7    9.7
6000.0     13.16  13.16  13.16  12.3   11.54  11.4   11.33  10.94  10.57  10.23   9.85   9.55   9.55   9.55   9.55   9.55
6400.0     13.84  12.63  12.38  11.83  11.4   11.07  11     10.69  10.4    9.9    9.6    9.6    9.6    9.6    9.6    9.6
6800.0     12.46  12.46  12.38  11.54  11.2   10.94  10.88  10.57  10.01  10.01  10.01  10.01  10.01  10.01  10.01  10.01
7200.0     12.46  12.46  12.38  11.54  11.2   10.94  10.88  10.57  10.01  10.01  10.01  10.01  10.01  10.01  10.01  10.01
7600.0     12.46  12.46  12.38  11.54  11.2   10.94  10.88  10.57  10.01  10.01  10.01  10.01  10.01  10.01  10.01  10.01
---------  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
```

## Supported Vehicles
- 2002 Subaru Impreza WRX
- 2003 Subaru Impreza WRX
- 2004 Subaru Impreza WRX
- 2005 Subaru Impreza WRX

If you'd like to use this tool for your Subaru, please create an issue with the year and model and I'll try to add the implementation.