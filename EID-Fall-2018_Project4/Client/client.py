# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EIDProject3Client.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

# Function to display QT GUI and run a weather-monitoring application on the Client-side, to request and receive data from AWS SQS, display and plot Temperature and Humidity Plots (Last 10 values)
#
# Authors: Sowmya Ramakrishnan and Vinayak Srivatsan Kovalam Mohan
#

#Import libraries
import json
import sys
import time
import datetime
import matplotlib.pyplot as plt
import boto3
import ast
import decimal
from PyQt5 import QtCore, QtGui, QtWidgets
from websocket import create_connection
import paho.mqtt.client as mqtt
from aiocoap import * 
import matplotlib
import pika #for rabbitmq
import threading
import asyncio

#A class for login
class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'pi' and
            self.textPass.text() == 'maya'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Wrong username or password. Try Again!')
            
#Main Class    
class Ui_MainWindow(object):

    #Initialization of variables
    def __init__(self):
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='EIDProject4_Queue') #get queue by name
        self.curr_temp_list=[]
        self.curr_humid_list=[]
        self.max_temp_list=[]
        self.max_humid_list=[]
        self.min_temp_list=[]
        self.min_humid_list=[]
        self.avg_temp_list=[]
        self.avg_humid_list=[]
        self.readings = 0
        self.multiplication_indicator = 1.0
        self.addition_indicator = 0.0
        self.unit = " C \n"
        self.websockets_time=[]
        self.output=""
        self.coap_time=[]
        self.mqtt_time=[]
        self.message_num=[]
        self.rabbitmq_time=[]

    #UI     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("EIDProject4 - Client")
        MainWindow.resize(1316, 671)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.getdata_3 = QtWidgets.QPushButton(self.centralWidget)
        self.getdata_3.setGeometry(QtCore.QRect(330, 200, 181, 121))
        self.getdata_3.setObjectName("getdata_3")               
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 211, 131))
        self.label.setObjectName("label")
        self.MessageBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MessageBox.setGeometry(QtCore.QRect(760, 0, 540, 801))
        self.MessageBox.setObjectName("MessageBox")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(630, 260, 67, 21))
        self.label_2.setObjectName("label_2")
        self.ClearMessage = QtWidgets.QPushButton(self.centralWidget)
        self.ClearMessage.setGeometry(QtCore.QRect(210, 520, 121, 31))
        self.ClearMessage.setObjectName("ClearMessage")
        self.Close = QtWidgets.QPushButton(self.centralWidget)
        self.Close.setGeometry(QtCore.QRect(600, 520, 151, 29))
        self.Close.setObjectName("Close")
        self.getdata = QtWidgets.QPushButton(self.centralWidget)
        self.getdata.setGeometry(QtCore.QRect(330, 150, 180, 40))
        self.getdata.setObjectName("getdata")
        self.getdata1 = QtWidgets.QPushButton(self.centralWidget)
        self.getdata1.setGeometry(QtCore.QRect(130, 150, 180, 40))
        self.getdata1.setObjectName("getdata1")
        self.getdata_2 = QtWidgets.QPushButton(self.centralWidget)
        self.getdata_2.setGeometry(QtCore.QRect(330, 330, 180, 40))
        self.getdata_2.setObjectName("getdata_2")
        MainWindow.setCentralWidget(self.centralWidget)

        #Function Declarations
        self.retranslateUi(MainWindow)
        self.Close.clicked.connect(MainWindow.close)
        self.ClearMessage.clicked.connect(self.MessageBox.clear)
        self.getdata_3.clicked.connect(self.get_data)
        self.getdata.clicked.connect(self.plottempGraph)
        self.getdata1.clicked.connect(self.plothumGraph)
        self.getdata_2.clicked.connect(self.time_protocols)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EIDProject4 - Client"))
        self.getdata_3.setText(_translate("MainWindow", "Get Data"))
        self.label.setText(_translate("MainWindow", " Weather Data"))
        self.label_2.setText(_translate("MainWindow", "Data"))
        self.ClearMessage.setText(_translate("MainWindow", "Clear Data"))
        self.Close.setText(_translate("MainWindow", "Exit"))
        self.getdata.setText(_translate("MainWindow", "Temp Graph"))
        self.getdata1.setText(_translate("MainWindow", "Humid Graph"))
        self.getdata_2.setText(_translate("MainWindow", "Execute Protocol Test"))
        
    #function to get data       
    def get_data(self):
        queue_list = []
        for i in range(3):
            list_val = self.queue.receive_messages(MaxNumberOfMessages=10) # Receive 10 messages
            if not list_val:
                break
            for msg in list_val:
                msgbody = ast.literal_eval(msg.body)  # Appending of data
                queue_list.append(msgbody)
                msg.delete()  
                self.readings += 1
        if queue_list:
            for mesg in queue_list:
                self.curr_temp_list.append(mesg["curr_temp"])
                self.curr_humid_list.append(mesg["curr_humid"])
                self.max_temp_list.append(mesg["max_temp"])
                self.max_humid_list.append(mesg["max_humid"])
                self.min_temp_list.append(mesg["min_temp"])
                self.min_humid_list.append(mesg["min_humid"])
                self.avg_temp_list.append(mesg["avg_temp"])
                self.avg_humid_list.append(mesg["avg_humid"])
            for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(self.max_temp_list,\
                self.min_temp_list,self.curr_temp_list, self.avg_temp_list, self.max_humid_list,\
                self.min_humid_list, self.curr_humid_list, self.avg_humid_list):
                self.output+= "Last Temp: {0:.2f}".format((curr_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n"+ \
                                "Last Hum: "+ str(curr_h) + " %\n" + \
                                "Max Temp: {0:.2f}".format((max_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n"+ \
                                "Max Hum: "+ str(max_h) + " %\n" + \
                                "Min Temp: {0:.2f}".format((min_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n" + \
                                "Min_Hum: "+str(min_h) + "%\n" + \
                                "Avg Temp: {0:.2f}".format((avg_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n" + \
                                "Avg Hum: "+ str(avg_h) + " %\n\n"
            self.MessageBox.setText("Obtained Data:\n"  + self.output + "\nTimestamp: " + str(datetime.datetime.now()))
        else:
            self.MessageBox.setText("Error Fetching Data \n")
            
    #Protocol roundtrip execution time calculation
    def time_protocols(self): 
        self.get_data()
        print("\n CoAP Data:\n")
        coapthread = threading.Thread(target=self.coap_collect)
        coap_time1 = time.time()
        coapthread.start()
        coapthread.join()
        coap_time2 = time.time()
        coap_execution_time = (coap_time2 - coap_time1)
        self.coap_time.append(coap_execution_time)
        print('\nThe roundtrip time for CoAP is: %s'% coap_execution_time)
        print('\nNumber of messages: %d'% self.readings)
        print("\n MQTT Data:\n")
        mqtt_time1 = time.time()
        client.publish(up_topic, self.output)
        mqtt_msgevent.wait()
        mqtt_time2 = time.time()
        mqtt_execution_time = (mqtt_time2 - mqtt_time1)
        mqtt_msgevent.clear()
        self.mqtt_time.append(mqtt_execution_time)
        print('\nThe roundtrip time for MQTT is: %s seconds'% mqtt_execution_time)
        print('\nNumber of messages: %d'% self.readings)
        print("\n WebSockets Data:\n")
        web_time1 = time.time()
        self.web_client()
        web_time2 = time.time()
        web_execution_time = web_time2 - web_time1
        self.websockets_time.append(web_execution_time)
        print('\nThe roundtrip time for WebSockets is: %s'% web_execution_time)
        print('\nNumber of messages: %d'% self.readings)
        print("\n AMQP Data:\n")
        rabbit_time1 = time.time()
        self.rabbitmq_publish()
        rabbit_time2 = time.time()
        rabbit_execution_time = rabbit_time2 - rabbit_time1
        self.rabbitmq_time.append(rabbit_execution_time)
        print('The roundtrip time for AMQP is: %s'% rabbit_execution_time)
        print('\nNumber of messages: %d'% self.readings)
        self.message_num.append(self.readings)
        self.plotoutputprotocol()
  
    # Function for plotting graph of humidity and temperature separately
    def plottempGraph(self):
        self.get_data()
        plt.plot(range(self.readings), self.max_temp_list, 'r-', label='Max Temp')  #red
        plt.plot(range(self.readings), self.min_temp_list, 'c-', label='Min Temp')  #blue
        plt.plot(range(self.readings), self.curr_temp_list, 'm-', label='Last Temp')  #green
        plt.plot(range(self.readings), self.avg_temp_list, 'y-', label='Avg Temp')  #yellow
        plt.legend(loc='best')
        plt.title('Temperature Graph')
        plt.ylabel('Temperature Celsius')
        plt.xlabel('readings')
        plt.show()
        
    def plothumGraph(self):
        self.get_data()
        plt.plot(range(self.readings), self.max_humid_list, 'r-', label='Max Hum')  #red
        plt.plot(range(self.readings), self.min_humid_list, 'c-', label='Min Hum')  #blue
        plt.plot(range(self.readings), self.curr_humid_list, 'm-', label='Last Hum') #green
        plt.plot(range(self.readings), self.avg_humid_list, 'y-', label='Avg Hum') #yellow
        plt.legend(loc='best')
        plt.title('Humidity Graph')
        plt.ylabel('Humidity %')
        plt.xlabel('Number of readings')
        plt.show()
        
    #Protocol plot
    def plotoutputprotocol(self): 
        plt.plot(self.message_num, self.mqtt_time, 'g-', label='MQTT')
        plt.plot(self.message_num, self.coap_time, 'y-', label='CoAP')
        plt.plot(self.message_num, self.websockets_time, 'r-', label='Websockets')
        plt.plot(self.message_num, self.rabbitmq_time, 'm-', label='RabbitMQ')
        plt.legend(loc='best')
        plt.title('Protocol comparison')
        plt.ylabel('Transfer time')
        plt.xlabel('Messages')
        plt.show()
    
    async def coapPUT(self, data):
        context = await Context.create_client_context()
        await asyncio.sleep(1)
        request = Message(code=PUT, payload=bytes(data, 'utf-8'))
        request.opt.uri_host = "10.0.0.83"
        request.opt.uri_path = ("other", "block")
        response = await context.request(request).response
        print('The response output is: %s\n%r'%(response.code, response.payload))
    
    def coap_collect(self):
        loop_func = asyncio.new_event_loop()
        asyncio.set_event_loop(loop_func)
        loop_func = asyncio.get_event_loop()
        loop_func.run_until_complete(self.coapPUT(self.output))
        return 0
        
    def web_client(self): #websocket client
        ws.send(self.output)
        websocket_output =  ws.recv()
        print(websocket_output)
    
    def rabbitmq_publish(self): 
        channel.queue_declare(queue='up_queue')
        channel.basic_publish(exchange='', routing_key='up_queue', body= self.output)
        return 0

def rabbitmq_subscribe():
    channel.queue_declare(queue='down_queue')
    channel.basic_consume(callback,queue='down_queue', no_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    print("\nAMQP Data:\n%r" % body)
    rabbit_msgevent.set()
            
def func_mqtt(): 
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(down_topic)

def on_message(client, userdata, msg):
    print(str(msg.payload))
    mqtt_msgevent.set()

#Main
if __name__ == "__main__":
    ws = create_connection("ws://10.0.0.83:8888/ws")
    ip = "10.0.0.83" 
    mqtt_msgevent = threading.Event()
    rabbit_msgevent =threading.Event()
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    up_topic = 'mqtt_upstream'
    down_topic = 'mqtt_downstream'
    client = mqtt.Client()
    client.connect('test.mosquitto.org',1883,60) 
    calcthread = [] 
    mqttthread = threading.Thread(target=func_mqtt) 
    calcthread.append(mqttthread)
    mqttthread.daemon = True
    mqttthread.start()
    rabbitmqthread = threading.Thread(target=rabbitmq_subscribe)
    calcthread.append(rabbitmqthread)
    rabbitmqthread.daemon = True
    rabbitmqthread.start() 
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

