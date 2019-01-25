# EID-Fall-2018-Project_2 - Remote WebSocket / Webpage UI
# DHT22 Temperature/Humidity Sensor, QT5, Python3.x, Raspberry Pi 3, WebSockets, HTML

## PROJECT WORK

This project is a combined effort of the following people:
### Sowmya Ramakrishnan - Server, Client side UI, Database, QT Script, calculations
### Vinayak Srivatsan Kovalam Mohan - Server-side script, Plot functions, calculations

## PROJECT DESCRIPTION

This project uses two Raspberry Pis - one is the sensor while other is the client running a remote web-based display. 
The sensor takes runs an interactive QT UI Interface that takes temperature/humidity values/readings using the read() function from a connected sensor (using the ADAFruit Library and GPIO Pin 4) at an interval of 5 seconds and displays in the QT 8 values - Maximum, Minimum, Current and Average Temperature and Humidity. Timestamp is also displayed. It also has a button that allows for change of unit from celcius (defaultly obtained) to fahrenheit.
All of this data from sensor is stored in a .csv (comma-separated value) file.
The sensor then runs a web server that allows the remote client to request and display data. 
WebSockets is used as the communication protocol, and Tornado is the Python Webserver. The webserver reads the csv database file and sends data to the webpage.
The client displays a HTML/Js/JQuery UI/webpage in a browser that talks to the sensor, gets and displays values and graphs, along with other functionalities. The webpage handles connection error by prompting user to try to connect again.

The Client side is implemented in HTML, CSS, JavaScript and JQuery.
The Server side is implemented in QT and Tornado.

Thus, all minimum requirements have been met. 

## PROJECT ADDITIONS (EXTRA CREDIT)

- A Login Screen on the Client side to secure the webpage application
- A HTML Webpage with a tasteful, appealing background and interactive buttons, as well as an appealing QT GUI
- A Logout button that re-directs the user to the Login page
- A Clear button that clears all data displayed
- Separate buttons for plots of temperature and humidity
- Temperature display in C and F (on both server and client)
- Temperature and Humidity Plots from data shown on webpage
- A Sensor State button on the QT GUI which tells if the sensor is connected/disconnected

## INSTALLATION/RUNNING INSTRUCTIONS

- Install tornado using the command : pip install tornado
- Install matplotlib using the command : sudo apt-get install python3 matplotlib'
- Change IP of the server as appropriate
- Clone this repository
### Server
- Run project2.py to open up the QT GUI and get and display data on the server side
- Run server.py to launch websocket server
### Client
- Open login.html, give username = username and password = psw to enable successful login
- The user is automatically re-directed to the HTML UI Webpage where values are displayed

## REFERENCES

https://www.w3schools.com/howto/howto_css_login_form.asp
https://www.geeksforgeeks.org/working-csv-files-python/
http://blog.glehmann.net/2014/12/23/Raspberry-Pi-as-a-temperature-logger/
https://stackoverflow.com/questions/24123715/degree-fahrenheit-celsius-symbols-ascii-nsstring
https://robots.thoughtbot.com/json-event-based-convention-websockets
https://os.mbed.com/cookbook/Websockets-Server#code
https://stackoverflow.com/questions/12839567/converting-string-to-number-in-javascript-jquery
https://www.w3schools.com/jsref/jsref_isnan_number.asp
https://www.w3schools.com/html/default.asp
https://www.w3schools.com/css/default.asp
https://www.w3schools.com/jquery/default.asp
https://www.w3schools.com/js/default.asp
https://github.com/adafruit/Adafruit_Python_DHT
