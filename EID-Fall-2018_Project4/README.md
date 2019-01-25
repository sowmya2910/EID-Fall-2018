## EID-Fall-2018-Project_4 - Multiple Protocols & Comparison
## DHT22 Temperature/Humidity Sensor, QT5, Python3.x, Raspberry Pi 3, AWS, MQTT, CoAP, WebSockets, AMQP (RabbitMQ), Node.js, Boto3

### PROJECT WORK

This project is a combined effort of the following people:
#### Sowmya Ramakrishnan - Server, Client side UI, Database, QT Script, calculations, AWS Lambda, SQS, MQTT Protocol
#### Vinayak Srivatsan Kovalam Mohan - Server-side script, Plot functions, calculations, AWS IoT Setup, CoAP, WebSockets, AMQP

#### PROJECT DESCRIPTION

This project uses two Raspberry Pis - one is the server while other is the client, both running QT UIs.
The server takes runs an interactive QT UI Interface that takes temperature/humidity values/readings using the read() function from a connected sensor (using the ADAFruit Library and GPIO Pin 4) at an interval of 5 seconds, sends the temperature and humidity values to AWS IoT Thing (EIDProject3) using MQTT in json format every 5 seconds, and displays in the QT 8 values - Maximum, Minimum, Current and Average Temperature and Humidity. Timestamp is also displayed. It also has a button that allows for change of unit from celcius (defaultly obtained) to fahrenheit.
All of this data from sensor is stored in a .csv (comma-separated value) file.
The sensor then runs an interactive QT UI that allows the remote client to request and display data as well as plot graphs. (Client)
In the middle, the data in AWS IoT is handled by a Lambda Function that uses Node JS to calculate various parameters and put all data in an AWS SQS Queue as 8-value messages.
The Client, requesting data, gets it from the AWS Queue (10 or less at a time, upto 30) using Boto3 resource. It also indicates communication failures/data not present error. The Client has a button to change between temperature units (C and F).
The Client and Server sides are implemented in QT.
AWS is the middleman between the client and the server.

The data from the SQS Queue is now exchanged with the server directly using four protocols - MQTT (Using a broker), CoAP, WebSockets and AMQP (Using a Queue) using multiple threads. The data for each protocol is published on the client-side numerically and graphically, as well as profiled.

#### PROJECT ADDITIONS (EXTRA CREDIT)

- Protocol data transfer using AMQP (RabbitMQ) has been attempted.

#### INSTALLATION/RUNNING INSTRUCTIONS

#### Pre-requisites
- Have an AWS account set up (IAM does not work in Starter Accounts!)
- Configure aws on Raspbian (aws configure - Enter Access Key ID, Secret Access Key and Region) - In order to use boto3
- Create an IoT Thing, attach policy and certificates as appropriate
- Create Lambda function (with appropriate permissions) and set it as a rule for IoT Thing
- Create an SQS Queue.
#### Main
- Install AWSIoTPythonSDK using the command : pip install AWSIoTPythonSDK
- Install boto3 using the command : pip install boto3
- Install aws-cli using the command : sudo pip3 install aws-cli
- Install matplotlib using the command : sudo apt-get install python3 matplotlib\
- Install aiocoap, asyncio, websocket-client, paho-mqtt, mosquitto, pika, rabbitmq libraries
- Clone this repository
#### Server
- EID-Fall-2018_Project3/Server/
- Run server.py to open up the QT GUI and get and display data on the server side
#### Client
- EID-Fall-2018_Project3.Client/
- Run client.py to open up QT GUI to request data from SQS Queue and plot graphs
- Click on the 'Execute Protocol Test' button to start data transfer and profiling using the protocols

#### REFERENCES

- https://docs.aws.amazon.com/index.html
- https://www.w3schools.com/howto/howto_css_login_form.asp
- https://www.geeksforgeeks.org/working-csv-files-python/
- http://blog.glehmann.net/2014/12/23/Raspberry-Pi-as-a-temperature-logger/
- https://stackoverflow.com/questions/24123715/degree-fahrenheit-celsius-symbols-ascii-nsstring
- https://www.w3schools.com/js/default.asp
- https://github.com/adafruit/Adafruit_Python_DHT
- https://www.tutorialspoint.com/nodejs/
- https://us-east-2.console.aws.amazon.com/iotv2/home?region=us-east-2#/learnHub
- http://boto3.readthedocs.io/en/latest/guide/sqs.html
- https://github.com/aws/aws-iot-device-sdk-python
- https://github.com/tornadoweb/tornado/issues/2352
- https://pypi.org/project/paho-mqtt/
- https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- https://pika.readthedocs.io/en/0.11.2/examples/asynchronous_consumer_example.html
- https://pika.readthedocs.io/en/0.11.2/examples/asynchronous_publisher_example.html
- https://os.mbed.com/cookbook/Websockets-Server
- https://aiocoap.readthedocs.io/en/latest/examples.html



