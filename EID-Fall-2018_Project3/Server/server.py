# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EIDProject2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

# Function to display QT GUI and run a weather-monitoring application on the Server-side, also to send data to AWS IoT through MQTT in json format
#
# Authors: Sowmya Ramakrishnan and Vinayak Srivatsan Kovalam Mohan
#

#import libraries
import AWSIoTPythonSDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import Adafruit_DHT 
import datetime
import matplotlib.pyplot as plt
import csv
import sys
import time
import socket
import ssl
import os
import json

#A class for Login
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

    #Login function with parameter checking
    def handleLogin(self):
        if (self.textName.text() == 'pi' and
            self.textPass.text() == 'maya'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Wrong username or password. Try Again!')

#Main class
class Ui_DHT22SensorData(object):

    #Initialization variables
    def __init__(self):
        self.maximumtemperature = 0
        self.minimumtemperature = 50
        self.maximumhumidity = 0
        self.minimumhumidity = 50
        self.temperaturesum = 0
        self.humiditysum = 0
        self.count = 1
        myAWSIoTMQTClient = None
        self.mqttSetup()
    
    #Setting up MQTT for data transfer to AWS, Connecting and Subscribing to Topic/Thing
    def mqttSetup(self):
        self.myAWSIoTMQTTClient = AWSIoTMQTTClient("clientId")
        self.myAWSIoTMQTTClient.configureEndpoint("a31pa84ob6kseu-ats.iot.us-east-1.amazonaws.com", 8883)
        self.myAWSIoTMQTTClient.configureCredentials("/home/pi/EID-Fall-2018_Project3/Certificates/CA-cert.pem","/home/pi/EID-Fall-2018_Project3/Certificates/a4ce7d3179-private.pem.key", "/home/pi/EID-Fall-2018_Project3/Certificates/a4ce7d3179-certificate.pem.crt")
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
        self.myAWSIoTMQTTClient.connect()
        print ("MQTT Conn Success")
        self.myAWSIoTMQTTClient.subscribe('EIDProject3', 1, None)
	
    #UI Parameters
    def setupUi(self, DHT22SensorData):
        DHT22SensorData.setObjectName("DHT22SensorData")
        DHT22SensorData.resize(547, 400)
        DHT22SensorData.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(128, 138, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(DHT22SensorData)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-30, -50, 551, 440))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("main-image.jpg"))
        self.Background.setObjectName("Background")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 141, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 141, 21))
        self.label_8.setObjectName("label_8")
        self.TempPlotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TempPlotPushButton.setGeometry(QtCore.QRect(20, 280, 81, 21))
        self.TempPlotPushButton.setObjectName("TempPlotPushButton")
        self.HumidityPlotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumidityPlotPushButton.setGeometry(QtCore.QRect(20, 340, 81, 21))
        self.HumidityPlotPushButton.setObjectName("HumidityPlotPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 190, 111, 21))
        self.label.setObjectName("label")
        self.SensorState = QtWidgets.QLabel(self.centralwidget)
        self.SensorState.setGeometry(QtCore.QRect(20, 220, 131, 21))
        self.SensorState.setText("")
        self.SensorState.setObjectName("SensorState")
        self.Datelabel = QtWidgets.QLabel(self.centralwidget)
        self.Datelabel.setGeometry(QtCore.QRect(20, 110, 121, 21))
        self.Datelabel.setObjectName("Datelabel")
        self.Timelabel = QtWidgets.QLabel(self.centralwidget)
        self.Timelabel.setGeometry(QtCore.QRect(20, 140, 180, 40))
        self.Timelabel.setText("")
        self.Timelabel.setObjectName("Timelabel")
        self.Humidity = QtWidgets.QLabel(self.centralwidget)
        self.Humidity.setGeometry(QtCore.QRect(390, 20, 44, 41))
        self.Humidity.setText("")
        self.Humidity.setPixmap(QtGui.QPixmap("rsz_1humidity.jpg"))
        self.Humidity.setObjectName("Humidity")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(200, 20, 21, 61))
        self.Temp.setText("")
        self.Temp.setPixmap(QtGui.QPixmap("rsz_therm.jpg"))
        self.Temp.setObjectName("Temp")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 91))
        self.label_6.setStyleSheet("font: 75 18pt \"PibotoLt\";")
        self.label_6.setObjectName("label_6")
        self.CelciusRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CelciusRadioButton.setGeometry(QtCore.QRect(220, 80, 101, 21))
        self.CelciusRadioButton.setObjectName("CelciusRadioButton")
        self.FarenheitRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.FarenheitRadioButton.setGeometry(QtCore.QRect(220, 100, 101, 21))
        self.FarenheitRadioButton.setObjectName("FarenheitRadioButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 190, 77, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Datelabel_3 = QtWidgets.QLabel(self.layoutWidget)
        self.Datelabel_3.setObjectName("Datelabel_3")
        self.verticalLayout_2.addWidget(self.Datelabel_3)
        self.TempMaxValue = QtWidgets.QLabel(self.layoutWidget)
        self.TempMaxValue.setText("")
        self.TempMaxValue.setObjectName("TempMaxValue")
        self.verticalLayout_2.addWidget(self.TempMaxValue)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(220, 250, 77, 50))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Datelabel_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.Datelabel_4.setObjectName("Datelabel_4")
        self.verticalLayout_3.addWidget(self.Datelabel_4)
        self.TempMinValue = QtWidgets.QLabel(self.layoutWidget_2)
        self.TempMinValue.setText("")
        self.TempMinValue.setObjectName("TempMinValue")
        self.verticalLayout_3.addWidget(self.TempMinValue)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(220, 320, 77, 50))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Datelabel_5 = QtWidgets.QLabel(self.layoutWidget_3)
        self.Datelabel_5.setObjectName("Datelabel_5")
        self.verticalLayout_4.addWidget(self.Datelabel_5)
        self.TempAverageValue = QtWidgets.QLabel(self.layoutWidget_3)
        self.TempAverageValue.setText("")
        self.TempAverageValue.setObjectName("TempAverageValue")
        self.verticalLayout_4.addWidget(self.TempAverageValue)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(370, 130, 77, 50))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Datelabel_6 = QtWidgets.QLabel(self.layoutWidget_4)
        self.Datelabel_6.setObjectName("Datelabel_6")
        self.verticalLayout_5.addWidget(self.Datelabel_6)
        self.HumLastValue = QtWidgets.QLabel(self.layoutWidget_4)
        self.HumLastValue.setText("")
        self.HumLastValue.setObjectName("HumLastValue")
        self.verticalLayout_5.addWidget(self.HumLastValue)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(370, 190, 77, 50))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Datelabel_7 = QtWidgets.QLabel(self.layoutWidget_5)
        self.Datelabel_7.setObjectName("Datelabel_7")
        self.verticalLayout_6.addWidget(self.Datelabel_7)
        self.HumMaxValue = QtWidgets.QLabel(self.layoutWidget_5)
        self.HumMaxValue.setText("")
        self.HumMaxValue.setObjectName("HumMaxValue")
        self.verticalLayout_6.addWidget(self.HumMaxValue)
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(370, 250, 77, 50))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Datelabel_8 = QtWidgets.QLabel(self.layoutWidget_6)
        self.Datelabel_8.setObjectName("Datelabel_8")
        self.verticalLayout_7.addWidget(self.Datelabel_8)
        self.HumMinValue = QtWidgets.QLabel(self.layoutWidget_6)
        self.HumMinValue.setText("")
        self.HumMinValue.setObjectName("HumMinValue")
        self.verticalLayout_7.addWidget(self.HumMinValue)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(370, 320, 77, 50))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Datelabel_9 = QtWidgets.QLabel(self.layoutWidget_7)
        self.Datelabel_9.setObjectName("Datelabel_9")
        self.verticalLayout_8.addWidget(self.Datelabel_9)
        self.HumAverageValue = QtWidgets.QLabel(self.layoutWidget_7)
        self.HumAverageValue.setText("")
        self.HumAverageValue.setObjectName("HumAverageValue")
        self.verticalLayout_8.addWidget(self.HumAverageValue)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 130, 77, 50))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Datelabel_2 = QtWidgets.QLabel(self.widget)
        self.Datelabel_2.setObjectName("Datelabel_2")
        self.verticalLayout.addWidget(self.Datelabel_2)
        self.TempLastValue = QtWidgets.QLabel(self.widget)
        self.TempLastValue.setText("")
        self.TempLastValue.setObjectName("TempLastValue")
        self.verticalLayout.addWidget(self.TempLastValue)
        DHT22SensorData.setCentralWidget(self.centralwidget)

	#Functions
        self.retranslateUi(DHT22SensorData)
        self.getTime()
        self.CelciusRadioButton.click()
        self.FarenheitRadioButton.clicked.connect(self.getDataFahrenheit)
        self.CelciusRadioButton.clicked.connect(self.getDataCelcius)
        self.timer = QTimer()
        self.timer.timeout.connect(self.getDataCelcius)
        self.timer.start(5000)
        self.TempPlotPushButton.clicked.connect(self.plotGraph)
        self.HumidityPlotPushButton.clicked.connect(self.plotGraph)
        QtCore.QMetaObject.connectSlotsByName(DHT22SensorData)

    def retranslateUi(self, DHT22SensorData):
        _translate = QtCore.QCoreApplication.translate
        DHT22SensorData.setWindowTitle(_translate("DHT22SensorData", "DHT22 Sensor Data "))
        self.label_7.setText(_translate("DHT22SensorData", "Temperature Graph"))
        self.label_8.setText(_translate("DHT22SensorData", "Humidity Graph"))
        self.TempPlotPushButton.setText(_translate("DHT22SensorData", "PLOT!"))
        self.HumidityPlotPushButton.setText(_translate("DHT22SensorData", "PLOT!"))
        self.label.setText(_translate("DHT22SensorData", "Sensor State : "))
        self.Datelabel.setText(_translate("DHT22SensorData", "Date and Time:"))
        self.label_6.setText(_translate("DHT22SensorData", "Welcome!"))
        self.CelciusRadioButton.setText(_translate("DHT22SensorData", "Celcius"))
        self.FarenheitRadioButton.setText(_translate("DHT22SensorData", "Farenheit"))
        self.Datelabel_3.setText(_translate("DHT22SensorData", "Maximum"))
        self.Datelabel_4.setText(_translate("DHT22SensorData", "Minimum"))
        self.Datelabel_5.setText(_translate("DHT22SensorData", "Average"))
        self.Datelabel_6.setText(_translate("DHT22SensorData", "Last value:"))
        self.Datelabel_7.setText(_translate("DHT22SensorData", "Maximum"))
        self.Datelabel_8.setText(_translate("DHT22SensorData", "Minimum"))
        self.Datelabel_9.setText(_translate("DHT22SensorData", "Average"))
        self.Datelabel_2.setText(_translate("DHT22SensorData", "Last value:"))

    #Function to get current humidity and temperature data (in celcius), send them to AWS in json format via MQTT Publish, calculate max,min,avg, and write them to a csv file
    def getDataCelcius(self):
        global count
        humidity, temperature = Adafruit_DHT.read(22,4)
        if humidity and temperature is None:
            self.SensorState.setText("Disconnected")
        if humidity and temperature is not None:
            self.SensorState.setText("Connected")
            temp_data = '{0:.2f}'.format(temperature)
            humid_data = '{0:.2f}'.format(humidity)
            pydict = {'Temperature': temp_data, 'Humidity': humid_data}
            jsondict = json.dumps(pydict)
            self.myAWSIoTMQTTClient.publish('EIDProject3', jsondict, 1)
			
            self.TempLastValue.setText(temp_data)
            self.HumLastValue.setText(humid_data + '%')		
            self.humiditysum += float(humidity)
            self.temperaturesum += float(temperature)
            averagehumidity = (self.humiditysum/float(self.count))
            averagetemperature = (self.temperaturesum/float(self.count))
            average_humid_data = '{0:.2f}'.format(averagehumidity)
            average_temp_data = '{0:.2f}'.format(averagetemperature)
            self.HumAverageValue.setText('{0:.2f}'.format(averagehumidity) + '%')
            self.TempAverageValue.setText('{0:.2f}'.format((averagetemperature)) + 'degC')
            self.count += 1
            if (temperature > self.maximumtemperature):
                self.maximumtemperature = temperature
            if (humidity > self.maximumhumidity):
                self.maximumhumidity = humidity
            if (temperature < self.minimumtemperature):
                self.minimumtemperature = temperature
            if (humidity < self.minimumhumidity):
                self.minimumhumidity = humidity
            max_temp_data = '{0:.2f}'.format(self.maximumtemperature)
            min_temp_data = '{0:.2f}'.format(self.minimumtemperature)
            max_humid_data = '{0:.2f}'.format(self.maximumhumidity)
            min_humid_data = '{0:.2f}'.format(self.minimumhumidity)
            self.TempMaxValue.setText('{0:.2f}'.format((self.maximumtemperature)) + 'degC')
            self.HumMaxValue.setText('{0:.2f}'.format(self.maximumhumidity)+'%')
            self.TempMinValue.setText('{0:.2f}'.format((self.minimumtemperature)) + 'degC')
            self.HumMinValue.setText('{0:.2f}'.format(self.minimumhumidity)+'%')
            with open('data.csv','a',newline = '') as datafile:
                file_write = csv.writer(datafile, delimiter = ',')
                file_write.writerow([temp_data, max_temp_data, min_temp_data, average_temp_data, humid_data, max_humid_data, min_humid_data, average_humid_data, self.getTime()])
				
        else:
            with open('data.csv','a',newline = '') as datafile:
                file_write = csv.writer(datafile, delimiter = ',')
                file_write.writerow([0, 0, 0, 0, 0, 0, 0, 0, self.getTime()])
                print("No Data Sensed")
	
    #Function to get current humidity and temperature data (in fahrenheit),  send them to AWS in json format via MQTT Publish, calculate max,min,avg and write them to a csv file
    def getDataFahrenheit(self):
        global count
        humidity, temperature = Adafruit_DHT.read(22,4)
        if humidity and temperature is None:
            self.SensorState.setText("Disconnected")
        if humidity and temperature is not None:
            self.SensorState.setText("Connected")
            tempf = (float(temperature) * (9/5.0)) + 32
            temp_data = '{0:.2f}'.format(tempf)
            humid_data = '{0:.2f}'.format(humidity)
            pydict = {'Temperature': temp_data, 'Humidity': humid_data}
            jsondict = json.dumps(pydict)
            self.myAWSIoTMQTTClient.publish('EIDProject3', jsondict, 1)
            self.TempLastValue.setText(temp_data)
            self.HumLastValue.setText(humid_data + '%')
            self.humiditysum += float(humidity)
            self.temperaturesum += float(tempf)
            averagehumidity = (self.humiditysum/float(self.count))
            averagetemperature = (self.temperaturesum/float(self.count))
            average_humid_data = '{0:.2f}'.format(averagehumidity)
            average_temp_data = '{0:.2f}'.format(averagetemperature)
            self.HumAverageValue.setText('{0:.2f}'.format(averagehumidity) + '%')
            self.TempAverageValue.setText('{0:.2f}'.format((averagetemperature)) + 'degF')
            self.count += 1
            if (tempf > self.maximumtemperature):
                self.maximumtemperature = tempf
            if (humidity > self.maximumhumidity):
                self.maximumhumidity = humidity
            if (tempf < self.minimumtemperature):
                self.minimumtemperature = tempf
            if (humidity < self.minimumhumidity):
                self.minimumhumidity = humidity
            max_temp_data = '{0:.2f}'.format(self.maximumtemperature)
            min_temp_data = '{0:.2f}'.format(self.minimumtemperature)
            max_humid_data = '{0:.2f}'.format(self.maximumhumidity)
            min_humid_data = '{0:.2f}'.format(self.minimumhumidity)
            self.TempMaxValue.setText('{0:.2f}'.format((self.maximumtemperature)) + 'degF')
            self.HumMaxValue.setText('{0:.2f}'.format(self.maximumhumidity)+'%')
            self.TempMinValue.setText('{0:.2f}'.format((self.minimumtemperature)) + 'degF')
            self.HumMinValue.setText('{0:.2f}'.format(self.minimumhumidity)+'%')
            with open('data.csv','a',newline = '') as datafile:
                file_write = csv.writer(datafile, delimiter = ',')
                file_write.writerow([temp_data, max_temp_data, min_temp_data, average_temp_data, humid_data, max_humid_data, min_humid_data, average_humid_data, self.getTime()])
    	
        else:
            with open('data.csv','a',newline = '') as datafile:
                file_write = csv.writer(datafile, delimiter = ',')
                file_write.writerow([0, 0, 0, 0, 0, 0, 0, 0, self.getTime()])
                print("No Data Sensed")
	
    #Function to get timestamp value
    def getTime(self):
        currenttime = datetime.datetime.now()
        now = currenttime.strftime("%m/%d/%Y %H:%M")
        self.Timelabel.setText(now)
        return now
	
    #Function to plot temperature and humidity graphs based on readings from csv file
    def plotGraph(self):
        x = []
        y = []
        with open('data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(float(row[0]))
                y.append(float(row[1]))
        i = range(0,len(x))
        fig1 = plt.figure(1)
        plt.plot(i,x,'b')
        plt.title('Humidity Variation Graph')
        fig1.savefig('humidgraph.jpg')

        fig2 = plt.figure(2)
        plt.plot(i,y,'r')
        plt.title('Temperature Variation Graph')
        fig2.savefig('tempgraph.jpg')
		
#main
if __name__ == "__main__":
    import sys
	
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        DHT22SensorData = QtWidgets.QMainWindow()
        ui = Ui_DHT22SensorData()
        ui.setupUi(DHT22SensorData)
        DHT22SensorData.show()
        sys.exit(app.exec_())
