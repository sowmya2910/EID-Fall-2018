# EID-Fall-2018 Project 1 - Local QT-based UI
# DHT22 Temperature/Humidity Sensor, QT5, Python3.x, Raspberry Pi 3
# Sowmya Ramakrishnan - SID : 108684769

## INSTALLATION INSTRUCTIONS

- This project uses Python3 for software implementation and RPi3 flashed with the Stretch OS.
- Interface the DHT22 Temperature/Humidity Sensor with the RPi 3, install dependencies (sudo python3 setup.py install) and test an example program. (Connect at GPIO 4 - Pin 7)
- Install the necessary python libraries necessary using the "pip install" command.
- Install pyqt5 and pyqt5-tools using the following commands :
  sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
  sudo apt-get install qttools5-dev-tools
- Use the QT Designer tools to generate basic UI - EIDProject1.ui
- Command to obtain .py from .ui : pyuic5 -x EIDProject1.ui -o EIDProject-Sowmya.py
- Run python3 EIDProject-Sowmya.py from the command line for project execution. 

## PROJECT WORK 

- This project was solely my work - with help from below-mentioned reference links.
- A QT Application has been created that displays temperature/humidity upon users' requests, also weighing in the factor whether the sensor is actually connected to the Pi. Appropriate messages are printed. Date and Time are also printed and refreshed as the (time of) requests change(s). 

## PROJECT ADDITIONS

- It has been provisioned to provide Temperature values in both Celcius as well as Farenheit.
- A graphic Thermometer-like device has been used to depict the temperature level with each request.
- The user can set Threshold values for both Temperature as well as Humidity using two Sliders.
- The Project goes into an Alarm state if the Threshold value is less than the obtained/measured temperature values. 
- A Login Screen has been added which require the following credentials for successful login : Username: pi Password: maya
- If incorrect, the GUI is not displayed, hence securing the application.

## REFERENCES

- https://riverbankcomputing.com/software/pyqt/intro
- https://www.codementor.io/deepaksingh04/design-simple-dialog-using-pyqt5-designer-tool-ajskrd09n
- https://pythonspot.com/pyqt5/
- http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/
- https://cdn-learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf
- https://www.youtube.com/watch?v=GEfTw7N-k8I
- http://embeddedlaboratory.blogspot.com/2018/04/design-gui-using-pyqt5-on-raspberry-pi.html
- https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
- http://www.riptutorial.com/Download/pyqt5.pdf
- http://www.circuitbasics.com/raspberry-pi-basics-setup-without-monitor-keyboard-headless-mode/
- http://www.circuitbasics.com/how-to-set-up-wifi-on-the-raspberry-pi-3/
- https://www.youtube.com/watch?v=IHTnU1T8ETk
- https://www.youtube.com/playlist?list=PLS1QulWo1RIZiBcTr5urECberTITj7gjA
- https://stackoverflow.com/questions/52015269/displaying-numbers-with-qlcdnumber-display-with-pyqt
- https://stackoverflow.com/questions/11812000/login-dialog-pyqt









