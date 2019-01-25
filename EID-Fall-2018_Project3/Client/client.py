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
import matplotlib.pyplot as plt
import sys
import time
import datetime
import json
import boto3
import ast
from PyQt5 import QtCore, QtGui, QtWidgets

#Define count as global variable
global count

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
	#Invoking boto3 resource and specifying SQS Queue name for access/to enable data pulling
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='EIDProject3_Queue')
        self.count = 0
        self.currenttemperature=[]
        self.minimumtemperature=[]
        self.maximumtemperature=[]
        self.averagetemperature=[]
        self.currenthumidity=[]
        self.minimumhumidity=[]
        self.maximumhumidity=[]
        self.averagehumidity=[]
        self.multiplier = 1
        self.adder = 0
        self.unit = " C\n"

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
        self.Background.setPixmap(QtGui.QPixmap("/home/pi/EID-Fall-2018_Project3/Client/main-image.jpg"))
        self.Background.setObjectName("Background")
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
        self.Humidity.setGeometry(QtCore.QRect(190, 80, 41, 41))
        self.Humidity.setText("")
        self.Humidity.setPixmap(QtGui.QPixmap("/home/pi/EID-Fall-2018_Project3/Client/rsz_1humidity.jpg"))
        self.Humidity.setObjectName("Humidity")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(200, 10, 21, 61))
        self.Temp.setText("")
        self.Temp.setPixmap(QtGui.QPixmap("/home/pi/EID-Fall-2018_Project3/Client/rsz_therm.jpg"))
        self.Temp.setObjectName("Temp")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 91))
        self.label_6.setStyleSheet("font: 75 18pt \"PibotoLt\";")
        self.label_6.setObjectName("label_6")
        self.CelciusRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.CelciusRadioButton.setGeometry(QtCore.QRect(230, 10, 101, 21))
        self.CelciusRadioButton.setObjectName("CelciusRadioButton")
        self.FarenheitRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.FarenheitRadioButton.setGeometry(QtCore.QRect(230, 40, 101, 21))
        self.FarenheitRadioButton.setObjectName("FarenheitRadioButton")
        self.GetDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetDataButton.setGeometry(QtCore.QRect(360, 10, 101, 31))
        self.GetDataButton.setObjectName("GetDataButton")
        self.MessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MessageLabel.setGeometry(QtCore.QRect(240, 120, 271, 251))
        self.MessageLabel.setText("")
        self.MessageLabel.setObjectName("MessageLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 67, 21))
        self.label_2.setObjectName("label_2")
        self.ClearDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearDataButton.setGeometry(QtCore.QRect(110, 260, 101, 31))
        self.ClearDataButton.setObjectName("ClearDataButton")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(110, 300, 101, 31))
        self.CloseButton.setObjectName("CloseButton")
        DHT22SensorData.setCentralWidget(self.centralwidget)
        
	#Functions
        self.retranslateUi(DHT22SensorData)
        self.getTime()
        self.CloseButton.clicked.connect(DHT22SensorData.close)
        self.ClearDataButton.clicked.connect(self.MessageLabel.clear)
        self.GetDataButton.clicked.connect(self.get_data)
        self.CelciusRadioButton.clicked.connect(self.FtoC)
        self.FarenheitRadioButton.clicked.connect(self.CtoF)
        QtCore.QMetaObject.connectSlotsByName(DHT22SensorData)
        
    def retranslateUi(self, DHT22SensorData):
        _translate = QtCore.QCoreApplication.translate
        DHT22SensorData.setWindowTitle(_translate("DHT22SensorData", "DHT22 Sensor Data "))
        self.label.setText(_translate("DHT22SensorData", "Sensor State : "))
        self.Datelabel.setText(_translate("DHT22SensorData", "Date and Time:"))
        self.label_6.setText(_translate("DHT22SensorData", "Welcome!"))
        self.CelciusRadioButton.setText(_translate("DHT22SensorData", "Celcius"))
        self.FarenheitRadioButton.setText(_translate("DHT22SensorData", "Farenheit"))
        self.GetDataButton.setText(_translate("DHT22SensorData", "GET DATA!"))
        self.label_2.setText(_translate("DHT22SensorData", "Message"))
        self.ClearDataButton.setText(_translate("DHT22SensorData", "Clear Data"))
        self.CloseButton.setText(_translate("DHT22SensorData", "Close"))
	
    #Function to get and display Date and Time
    def getTime(self):
        currenttime = datetime.datetime.now()
        now = currenttime.strftime("%m/%d/%Y %H:%M")
        self.Timelabel.setText(now)
        return now

    global count 
	
    #Function to get data from SQS Queue
    def get_data(self):
        #global count
        count = 0
        self.SensorState.setText("Connected")
        queuelist = []
        for i in range(3):
	    #Receive 10 messages max
            valueslist = self.queue.receive_messages(MaxNumberOfMessages=10)
            if not valueslist:
                break
            for msg in valueslist:
                msgbody = ast.literal_eval(msg.body)
                queuelist.append(msgbody)
                msg.delete()
                count += 1
                if queuelist:
                    for mesg in queuelist:
                        self.currenttemperature.append(mesg["curr_temp"])
                        self.currenthumidity.append(mesg["curr_humid"])
                        self.maximumtemperature.append(mesg["max_temp"])
                        self.maximumhumidity.append(mesg["max_humid"])
                        self.minimumtemperature.append(mesg["min_temp"])
                        self.minimumhumidity.append(mesg["min_humid"])
                        self.averagetemperature.append(mesg["avg_temp"])
                        self.averagehumidity.append(mesg["avg_humid"])
                        final_mesg=""
                        for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(self.maximumtemperature,\
                    self.minimumtemperature,self.currenttemperature, self.averagetemperature, self.maximumhumidity,\
                self.minimumhumidity, self.currenthumidity, self.averagehumidity):
                            final_mesg +=   "Max Temp: {0:.2f}".format((max_t*self.multiplier)+self.adder) + self.unit + \
                                "Min Temp: {0:.2f}".format((min_t*self.multiplier)+self.adder) + self.unit + \
                                "Last Temp: {0:.2f}".format((curr_t*self.multiplier)+self.adder) + self.unit + \
                                "Avg Temp: {0:.2f}".format((avg_t*self.multiplier)+self.adder) + self.unit + \
                                "Max Hum: "+ str(max_h) + " %\n" + \
                                "Min Hum: "+ str(min_h) + " %\n" + \
                                "Last Hum: "+ str(curr_h) + " %\n" + \
                                "Avg Hum: "+ str(avg_h) + " %\n\n"
                            self.MessageLabel.setText("Fetched Data:\n"  + final_mesg + "\nTimestamp: " + str(datetime.datetime.now()))
                            self.plotGraph()
                        else:
				#In case of error/no values
                                self.MessageLabel.setText("Error Fetching Data \n")
  #Function to plot graphs				
  def plotGraph(self):
	#Temperature Graph
        plt.plot(range(self.count), self.maximumtemperature, 'b-', label='Maximum Temperature')
        plt.plot(range(self.count), self.minimumtemperature, 'r-', label='Minimum Temperature')
        plt.plot(range(self.count), self.currenttemperature, 'y-', label='Current Temperature')
        plt.plot(range(self.count), self.averagetemperature, 'g-', label='Average Temperature')
        plt.legend(loc='best')
        plt.title('Temperature Graph')
        plt.ylabel('Temperature in C')
        plt.xlabel('count')
        plt.show()
	#Humidity Graph
        plt.plot(range(self.count), self.maximumhumidity, 'b-', label='Maximum Humidity')
        plt.plot(range(self.count), self.minimumhumidity, 'r-', label='Minimum Humidity')
        plt.plot(range(self.count), self.currenthumidity, 'y-', label='Current Humidity')
        plt.plot(range(self.count), self.averagehumidity, 'g-', label='Average Humidity')
        plt.legend(loc='best')
        plt.title('Humidity Graph')
        plt.ylabel('Humidity in %')
        plt.xlabel('count')
        plt.show()		

    #Setting parameters for C to F conversion		
    def CtoF(self):
        self.multiplier = 1.8
        self.adder = 32.0
        self.unit = " F\n"
	
    #Setting parameters for F to C conversion
    def FtoC(self):
        self.multiplier = 1.0
        self.adder = 0.0
        self.unit = " C\n"

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

