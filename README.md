# CuRe software
## Installation
### Raspberry configuration
You can get the instruction for configuring your raspberry here 
```
https://www.raspberrypi.org/documentation/computers/getting-started.html
```
Download Raspberry Pi Imager and install
```Raspberry Pi OS (32 bits)``` on it. Make sure you take a version 
``With the raspberry pi dekstop``. \
Our GUI needs a working version of Chrome/Chromium (included in ```Raspberry Pi OS (32 bits) with desktop```) and it wont work otherwise.
We tested it on Rasberry Pi 3b+.

### Installing CuRe software
If not done yet please install the latest version of python
```
sudo apt-get install python
```
Then install the required libraries
```
pip install selenium
pip install adafruit-circuitpython-lps35hw
```
Get CuRe software
```
git clone https://github.com/rombirli/CuRe
```
Run CuRe software
```
cd CuRe
python main.py
```
## Python scripts
Python scripts manage the different sensors and motors. 
They are able to measure datas and send it in real time to the GUI, act the motors, or catching events thrown by the GUI.
Don't care to start the GUI manually, the scripts will do it for you !
## GUI
The GUI is programmed in HTML / CSS / JS and is displayed by Chrome thanks to the Selenium library. \
The ```tools.js``` file contains a function ```throw_event(event)``` that will throw an event to the main script runing in background. \
The main script has the ability to execute a piece of javascript inside the GUI  for example to plot a chart. 


