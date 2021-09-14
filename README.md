# Gen2 UHF RFID Reader
This is a Gen2 UHF RFID Reader. It is able to identify commercial Gen2 RFID Tags with FM0 line coding and 40kHz data rate (BLF), and extract their EPC. This project is a Work-in-Progress with LimeSDR and TBD components. 

The project is based on the RFID Gen2 Reader available at https://github.com/ransford/gen2_rfid. The reader borrows elements from the software developed by Buettner, i.e. Data flow: Gate -> Decoder -> Reader as well as the conception regarding the detection of the reader commands. CRC calculation and checking functions were also adapted from https://www.cgran.org/browser/projects/gen2_rfid/.

## Table of contents

* 1. [Implemented GNU Radio Blocks](#implemented-gnu-radio-blocks)
* 2. [Porting](#porting)
* 3. [Warning](#warning)
* 4. [Installation](#installation)
* 5. [Usage](#usage)
* 6. [Checking the installation](#checking-the-installation)
  <!-- * 6.1. [Check PYTHONPATH](#check-pythonpath)
  * 6.2. [Check SoapySDRUtil](#check-soapysdrutil) -->
* 7. [Configuration](#configuration)
* 8. [How to run](#how-to-run)
* 9. [Logging](#logging)
* 10. [Debugging](#debugging)



## Implemented GNU Radio Blocks:

- Gate : Responsible for reader command detection.  
- Tag decoder : Responsible for frame synchronization, channel estimation, symbol period estimation and detection.  
- Reader : Create/send reader commands.

## Porting
**The gr-rfid has been ported from GNU Radio 3.7 to 3.8, and reader.py has been ported from Python 2.7 to Python 3 using 2to3 library (https://docs.python.org/3/library/2to3.html).**

## Warning
**This script has been modified and only supports Ubuntu 18.04 / 20.04 LTS. Ubuntu versions below 18.04 LTS and other linux distros are not supported due to deprecation of Python 2.7, qt4 when upgrading to GNU Radio 3.8.x.**

**The build-script will require approximately 16GB of disk space in order to download, build and install all packages. If only gr-rfid is required, follow Step 1 and 2a.**

## Installation
The whole process may take up to two hours to complete, depending on the capabilities of your system. A faster CPU with more cores and threads will be quicker to compile. AMD Ryzen 5 1600 -j11 took \~45 minutes to complete, Intel i5-8250U -j7 took \~1 hour 6 minutes to complete, Intel i5-3230m -j3 took \~1 hour 30 minutes to complete.

- Log4cpp is installed on Ubuntu 20.04 LTS, Ubuntu 18.04 requires manaual installation here (http://log4cpp.sourceforge.net/)
- Using build-script will automatically fetch, build and install the following:

Package           | Branch
------------------|-----------------
GNU Radio         | maint-3.8
UHD 			  | 3.15 LTS
rtl-sdr 		  | master
gr-osmosdr 		  | gr3.8
gr-iqbal 		  | gr3.8
hackrf     		  | master
bladeRF           | master
airspyone_host    | master
SoapySDR          | master
LimeSuite 		  | stable

1. Grant permissions 
```sh
chmod a+x ./build-script
```

2. Execute with the following flags to install everything, refer to Usage below for more details.
```sh
./build-script -ja
```
- 2a. Execute with the following flag and function to install only G2RFID, requires GNU Radio 3.8 installed.
```sh
./build-script -ja G2RFID
```

3. Add PYTHONPATH to ~/.bashrc

- Ubuntu 20.04
```sh
echo 'export PYTHONPATH=/usr/local/lib/python3/dist-packages:/usr/local/lib/python3/site-packages:$PYTHONPATH' >> ~/.bashrc
```
- Ubuntu 18.04
```sh
echo 'export PYTHONPATH=/usr/local/lib/python3.6/dist-packages:/usr/local/lib/python3.6/site-packages:$PYTHONPATH' >> ~/.bashrc
```

4. Add LD Library to ~/.bashrc
```sh
echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
```

5. Source ~/.bashrc
```sh
source ~/.bashrc
```

6. Restart PC for mod_groups to take effect

## Usage
build-script [--help|-h] [-v|--verbose] [-jN] [-ja] [-l|--logfile logfile ] [-u|--users ulist] funcs

 Flags        |  Description                                             
--------------|----------------------------------------------------------
-v/--verbose  | Turn on verbose logging to stdout
-jN           | Have make use N concurrent jobs
-ja           | Have make use N concurrent jobs with auto setting of N (based on number of cpu cores on build system)
-u/--users ul | Add comma-separated users to 'usrp' group in addition to calling user ( $USER )
-l/--logfile lf | Log messages to 'lf'
-ut <tag>      | Set tag for UHD checkout to <tag>
-ucf <ucflags> | Set UHD CMake flags to <ucflags>
-gt <tag>      | Set tag for Gnu Radio checkout to <tag>
-gcf <gcflags> | Set Gnu Radio CMake flags to <gcflags>
-e/--extras    | Add an item to "extras" to be built after Gnu Radio/UHD/gs-osmosdr

Available funcs | Description
----------------|--------------------------------------------
all             | Do all functions (default)
prereqs         | Install prerequisites
gitfetch        | Use GIT to fetch all packages
uhd_build       | Build only UHD
firmware        | Fetch firmware/FPGA
gnuradio_build  | Build only GNU Radio
rtl_build       | Build rtl-sdr + gr-osmosdr + gr-iqbal + hackrf + bladeRF + airspyone_host
SoapySDR        | Build only SoapySDR
LimeSuite       | Build only LimeSuite
G2RFID          | Build Gen2 UHF RFID Reader
mod_groups      | Modify the /etc/groups and add user to group 'usrp'
mod_udev        | Add UDEV rule for USRP1
mod_sysctl      | Modify SYSCTL for larger net buffers
pythonpath		| Print out PYTHONPATH


## Checking the installation

1. Check PYTHONPATH
```sh
> echo $PYTHONPATH
/usr/local/lib/python3/dist-packages:/usr/local/lib/python3/site-packages:
```

2. Check SoapySDRUtil
```sh
> SoapySDRUtil --info
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Lib Version: v0.8.1-g1cf5a539
API Version: v0.8.0
ABI Version: v0.8
Install root: /usr/local
Search path:  /usr/local/lib/SoapySDR/modules0.8
Module found: /usr/local/lib/SoapySDR/modules0.8/libLMS7Support.so (20.10.0-1480bfea)
Available factories... lime
Available converters...
 -  CF32 -> [CF32, CS16, CS8, CU16, CU8]
 -  CS16 -> [CF32, CS16, CS8, CU16, CU8]
 -  CS32 -> [CS32]
 -   CS8 -> [CF32, CS16, CS8, CU16, CU8]
 -  CU16 -> [CF32, CS16, CS8]
 -   CU8 -> [CF32, CS16, CS8]
 -   CU8 -> [CF32, CS16, CS8]
 -   F32 -> [F32, S16, S8, U16, U8]
 -   S16 -> [F32, S16, S8, U16, U8]
 -   S32 -> [S32]
 -    S8 -> [F32, S16, S8, U16, U8]
 -   U16 -> [F32, S16, S8]
 -    U8 -> [F32, S16, S8]
```

Connect LimeSDR
```sh
> SoapySDRUtil --probe
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Probe device
[INFO] Make connection: 'LimeSDR-USB [USB3.0] 9072C00Dxxxxx'
[INFO] Reference clock 30.72 MHz
[INFO] Device name: LimeSDR-USB
[INFO] Reference: 30.72 MHz
[INFO] LMS70002M register cache: Disabled

---------------------------------------------------
-- Device identification
---------------------------------------------------
  driver=FX3
  hardware=LimeSDR-USB
  boardSerialNumber=0x9072C00Dxxxxx
  firmwareVersion=4
  gatewareVersion=2.23
  hardwareVersion=4
  protocolVersion=1
```

## Configuration

- Set USRPN200 address in apps/reader.py (default: 192.168.10.2)
- Set frequency in apps/reader.py (default: 910MHz)
- Set tx amplitude in apps/reader.py (default: 0.1)
- Set rx gain in apps/reader.py (default: 20)
- Set maximum number of queries in include/global_vars.h (default:1000)
- Set number of inventory round slots in include/global_vars.h (default: 0)

## How to run

- Real time execution:  
If you use an SBX daughterboard uncomment  #self.source.set_auto_dc_offset(False) in reader.py file
cd Gen2-UHF-RFID-Reader/gr-rfid/apps/    
sudo GR_SCHEDULER=STS nice -n -20 python ./reader.py     
After termination, part of EPC message (hex value of EPC[104:111]) of identified Tags is printed.  

- Offline:  
    Change DEBUG variable in apps/reader.py to TRUE (A test file already exists named file_source_test).  
    The reader works with offline traces without using a USRP.  
    The output after running the software with test file is:  
    
    | Number of queries/queryreps sent : 71  
    | Current Inventory round : 72  

    | Correctly decoded EPC : 70  
    | Number of unique tags : 1  
    | Tag ID : 27  Num of reads : 70  
 
## Logging

- Configuration file : /home/username/.gnuradio/config.conf  
    Edit the above file and add the following lines  

    [LOG]  
    debug_file = /PathToLogFile/Filename  
    debug_level = info  
    
    Logging may cause latency issues if it is enabled during real time execution!

## Debugging  

The reader may fail to decode a tag response for the following reasons

1) Latency: For real time execution you should disable the output on the terminal. If you see debug messages, you should either install log4cpp or comment the corresponding lines in the source code e.g., GR_LOG_INFO(d_debug_logger, "EPC FAIL TO DECODE");

2) Antenna placement. Place the antennas side by side with a distance of 50-100cm between them and the tag 2m (it can detect a tag up to 6m) away facing the antennas.

3) Parameter tuning. The most important is self.ampl which controls the power of the transmitted signal (takes values between 0 and 1).

If the reader still fails to decode tag responses, uncomment the following line in reader.py file

 #self.connect(self.source, self.file_sink_source)

Run the software for a few seconds (~5s). A file will be created in misc/data directory named source. This file contains the received samples. You can plot the amplitude of the received samples using the script located in misc/code folder. The figure should be similar to the .eps figure included in the folder. Plotting the figure can give some indication regarding the problem. You can also plot the output of any block by uncommenting the corresponding line in the reader.py file. Output files will be created in misc/data folder:

- /misc/data/source  
- /misc/data/matched_filter  
- /misc/data/gate 
- /misc/data/decoder  
- /misc/data/reader

Useful discussions on software issues:

https://github.com/nkargas/Gen2-UHF-RFID-Reader/issues/1

https://github.com/nkargas/Gen2-UHF-RFID-Reader/issues/4

https://github.com/nkargas/Gen2-UHF-RFID-Reader/issues/10

    
## Hardware:

  - 2x LimeSDR
  - 2x antennas?

## Tested on:
  Ubuntu 20.04 LTS 64-bit  
  GNU Radio 3.8.3.1
  
## If you use this software please cite:
N. Kargas, F. Mavromatis and A. Bletsas, "Fully-Coherent Reader with Commodity SDR for Gen2 FM0 and Computational RFID", IEEE Wireless Communications Letters (WCL), Vol. 4, No. 6, pp. 617-620, Dec. 2015. 

## Contact:
  Nikos Kargas (email: karga005@umn.edu)  

This research has been co-financed by the European Union (European Social Fund-ESF) and Greek national funds through the Operational Program Education and Lifelong Learning of the National Strategic Reference Framework (NSRF) - Research Funding Program: THALES-Investing in knowledge society through the European Social Fund.
