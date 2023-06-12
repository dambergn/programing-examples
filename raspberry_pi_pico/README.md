# Raspberry Pi Pico
- https://www.raspberrypi.com/documentation/microcontrollers/
- https://www.youtube.com/watch?v=Zy64kZEM_bg&list=PLWNDWPAClRVoo0Z-QtCkXuM15jdb2Q54N
Raspberry pi Pico and Pico W  
The Raspberry Pi Pico operates on 3.3v logic but can run on 2-5 volts.  
Can be programmed with either Micro Python or C like arduino  

## Specifications
RP2040
- Dual ARM Cortex-M0+ @ 133MHz
- 264kB on-chip SRAM in six independent banks
- Support for up to 16MB of off-chip Flash memory via dedicated QSPI bus
- DMA controller
- Fully-connected AHB crossbar
- Interpolator and integer divider peripherals
- On-chip programmable LDO to generate core voltage
- 2 on-chip PLLs to generate USB and core clocks
- 30 GPIO pins, 4 of which can be used as analogue inputs
- Peripherals
  - 2 UARTs
  - 2 SPI controllers
  - 2 I2C controllers
  - 16 PWM channels
  - USB 1.1 controller and PHY, with host and device support
  - 8 PIO state machines  

Pico W
- Wireless (802.11n), single-band (2.4 GHz)
- WPA3
- Soft access point supporting up to four clients

## Setup
Hold down the bootsel button while connecting the pi to the computer.  
The pi will show up as a media device, open it and go to the html file.  
This will take you to the pico web page, click on micro python.  
Download the file for the pico, the w file for the w variant.  
Drag and drop the downloaded file into the pico device, this will reset the device.  
Using VSCode install the Pymakr extension.  
use Thony IDE for programing Pico.  
save file as main.py to the pico to run indipendently.  