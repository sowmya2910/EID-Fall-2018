# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EIDProject1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

# -*- Python3 -*-

# Functions to support UI and for project deliverables
#
# Created by: Python Editor on the Raspbian
# Author: Sowmya Ramakrishnan
#

#Import files to handle dependencies

import sys
import time
import datetime
import Adafruit_DHT
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#A class for Login Application
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
                self, 'Error', 'Bad user or password')
            
#A class to open up the Login Window            
class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
from PyQt5 import QtCore, QtGui, QtWidgets

#Main class got from GUI Main Window, depicting various parts of it and their properties 
class Ui_DHT22SensorData(object):
    
    #Initialization values
    def __init__(self):
        self.temperature=0
        self.humidity=0
        self.thresholdtemperature=30
        self.thresholdhumidity=30
        self.count=0
        
    #Auto-generated QT Code for GUI
    def setupUi(self, DHT22SensorData):
        DHT22SensorData.setObjectName("DHT22SensorData")
        DHT22SensorData.resize(515, 388)
        DHT22SensorData.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(128, 138, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(DHT22SensorData)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-30, -50, 551, 440))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("main-image.jpg"))
        self.Background.setObjectName("Background")
        self.HumidityDisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.HumidityDisplay.setGeometry(QtCore.QRect(390, 110, 64, 23))
        self.HumidityDisplay.setObjectName("HumidityDisplay")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(210, 110, 101, 60))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TemperatureDisplayC = QtWidgets.QLCDNumber(self.layoutWidget_2)
        self.TemperatureDisplayC.setObjectName("TemperatureDisplayC")
        self.verticalLayout_3.addWidget(self.TemperatureDisplayC)
        self.GraphicTempBarC = QtWidgets.QProgressBar(self.layoutWidget_2)
        self.GraphicTempBarC.setProperty("value", 24)
        self.GraphicTempBarC.setObjectName("GraphicTempBarC")
        self.verticalLayout_3.addWidget(self.GraphicTempBarC)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 21, 21))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 110, 101, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TemperatureDisplay = QtWidgets.QLCDNumber(self.layoutWidget)
        self.TemperatureDisplay.setObjectName("TemperatureDisplay")
        self.verticalLayout_2.addWidget(self.TemperatureDisplay)
        self.GraphicTempBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.GraphicTempBar.setProperty("value", 24)
        self.GraphicTempBar.setObjectName("GraphicTempBar")
        self.verticalLayout_2.addWidget(self.GraphicTempBar)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(210, 190, 101, 60))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TemperatureDisplayF = QtWidgets.QLCDNumber(self.layoutWidget_3)
        self.TemperatureDisplayF.setObjectName("TemperatureDisplayF")
        self.verticalLayout_4.addWidget(self.TemperatureDisplayF)
        self.GraphicTempBarF = QtWidgets.QProgressBar(self.layoutWidget_3)
        self.GraphicTempBarF.setProperty("value", 24)
        self.GraphicTempBarF.setObjectName("GraphicTempBarF")
        self.verticalLayout_4.addWidget(self.GraphicTempBarF)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 200, 21, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 141, 21))
        self.label_4.setStyleSheet("font: 75 8pt \"PibotoLt\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 151, 21))
        self.label_5.setStyleSheet("font: 75 8pt \"PibotoLt\";")
        self.label_5.setObjectName("label_5")
        self.Alarmpic1 = QtWidgets.QLabel(self.centralwidget)
        self.Alarmpic1.setGeometry(QtCore.QRect(20, 310, 51, 41))
        self.Alarmpic1.setText("")
        self.Alarmpic1.setPixmap(QtGui.QPixmap("rsz_alarmlatest.jpg"))
        self.Alarmpic1.setObjectName("Alarmpic1")
        self.Alarmpic1_2 = QtWidgets.QLabel(self.centralwidget)
        self.Alarmpic1_2.setGeometry(QtCore.QRect(110, 310, 51, 41))
        self.Alarmpic1_2.setText("")
        self.Alarmpic1_2.setPixmap(QtGui.QPixmap("rsz_alarmlatest.jpg"))
        self.Alarmpic1_2.setObjectName("Alarmpic1_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 270, 141, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 320, 141, 21))
        self.label_8.setObjectName("label_8")
        self.TempPlotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TempPlotPushButton.setGeometry(QtCore.QRect(230, 300, 81, 21))
        self.TempPlotPushButton.setObjectName("TempPlotPushButton")
        self.HumidityPlotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumidityPlotPushButton.setGeometry(QtCore.QRect(390, 360, 81, 21))
        self.HumidityPlotPushButton.setObjectName("HumidityPlotPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 150, 111, 21))
        self.label.setObjectName("label")
        self.SensorState = QtWidgets.QLabel(self.centralwidget)
        self.SensorState.setGeometry(QtCore.QRect(376, 180, 131, 21))
        self.SensorState.setText("")
        self.SensorState.setObjectName("SensorState")
        self.TempSlider = QtWidgets.QSlider(self.centralwidget)
        self.TempSlider.setGeometry(QtCore.QRect(10, 280, 81, 26))
        self.TempSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TempSlider.setObjectName("TempSlider")
        self.HumiditySlider = QtWidgets.QSlider(self.centralwidget)
        self.HumiditySlider.setGeometry(QtCore.QRect(100, 280, 81, 26))
        self.HumiditySlider.setOrientation(QtCore.Qt.Horizontal)
        self.HumiditySlider.setObjectName("HumiditySlider")
        self.Datelabel = QtWidgets.QLabel(self.centralwidget)
        self.Datelabel.setGeometry(QtCore.QRect(20, 150, 121, 21))
        self.Datelabel.setObjectName("Datelabel")
        self.Timelabel = QtWidgets.QLabel(self.centralwidget)
        self.Timelabel.setGeometry(QtCore.QRect(20, 180, 180, 40))
        self.Timelabel.setText("")
        self.Timelabel.setObjectName("Timelabel")
        self.Humidity = QtWidgets.QLabel(self.centralwidget)
        self.Humidity.setGeometry(QtCore.QRect(390, 20, 41, 41))
        self.Humidity.setText("")
        self.Humidity.setPixmap(QtGui.QPixmap("rsz_1humidity.jpg"))
        self.Humidity.setObjectName("Humidity")
        self.HumidityPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumidityPushButton.setGeometry(QtCore.QRect(350, 70, 128, 25))
        self.HumidityPushButton.setStyleSheet("font: 75 8pt \"PibotoLt\";")
        self.HumidityPushButton.setObjectName("HumidityPushButton")
        self.TemperaturePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TemperaturePushButton.setGeometry(QtCore.QRect(230, 40, 97, 25))
        self.TemperaturePushButton.setStyleSheet("font: 75 8pt \"PibotoLt\";")
        self.TemperaturePushButton.setObjectName("TemperaturePushButton")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(200, 20, 21, 61))
        self.Temp.setText("")
        self.Temp.setPixmap(QtGui.QPixmap("rsz_therm.jpg"))
        self.Temp.setObjectName("Temp")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 360, 67, 21))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 360, 67, 21))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 131, 91))
        self.label_6.setStyleSheet("font: 75 18pt \"PibotoLt\";")
        self.label_6.setObjectName("label_6")
        self.Background.raise_()
        self.layoutWidget.raise_()
        self.HumidityDisplay.raise_()
        self.layoutWidget_2.raise_()
        self.label_2.raise_()
        self.layoutWidget_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Alarmpic1.raise_()
        self.Alarmpic1_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.TempPlotPushButton.raise_()
        self.HumidityPlotPushButton.raise_()
        self.label.raise_()
        self.SensorState.raise_()
        self.TempSlider.raise_()
        self.HumiditySlider.raise_()
        self.Datelabel.raise_()
        self.Timelabel.raise_()
        self.Humidity.raise_()
        self.HumidityPushButton.raise_()
        self.TemperaturePushButton.raise_()
        self.Temp.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        DHT22SensorData.setCentralWidget(self.centralwidget)
        
        #Functions to be executed on running the code
        self.retranslateUi(DHT22SensorData)
        self.HumidityPushButton.clicked.connect(self.readanddisplayH)
        self.TemperaturePushButton.clicked.connect(self.readanddisplayT)
        QtCore.QMetaObject.connectSlotsByName(DHT22SensorData)

    #Auto-generated QT Code for GUI - Naming the Boxes
    def retranslateUi(self, DHT22SensorData):
        _translate = QtCore.QCoreApplication.translate
        DHT22SensorData.setWindowTitle(_translate("DHT22SensorData", "DHT22 Sensor Data "))
        self.label_2.setText(_translate("DHT22SensorData", "C"))
        self.label_3.setText(_translate("DHT22SensorData", "F"))
        self.label_4.setText(_translate("DHT22SensorData", "Threshold Values"))
        self.label_5.setText(_translate("DHT22SensorData", "Temperature          Humidity"))
        self.label_7.setText(_translate("DHT22SensorData", "Temperature Graph"))
        self.label_8.setText(_translate("DHT22SensorData", "Humidity Graph"))
        self.TempPlotPushButton.setText(_translate("DHT22SensorData", "PLOT!"))
        self.HumidityPlotPushButton.setText(_translate("DHT22SensorData", "PLOT!"))
        self.label.setText(_translate("DHT22SensorData", "Sensor State : "))
        self.Datelabel.setText(_translate("DHT22SensorData", "Date and Time:"))
        self.HumidityPushButton.setText(_translate("DHT22SensorData", "Get Humidity!"))
        self.TemperaturePushButton.setText(_translate("DHT22SensorData", "Get Temperature!"))
        self.label_6.setText(_translate("DHT22SensorData", "Welcome!"))
        
    #Function to read and display Humidity on press of Request button, also to take in threshold value from the user, compare with obtained/measured value and send out approriate alarm messages.
    def readanddisplayH(self):
        now=datetime.datetime.now()
        self.Timelabel.setText(now.strftime("%m/%d/%Y %H:%M:%S"))
        humidity, temperature = Adafruit_DHT.read(22,4)
        if humidity == None:
            self.SensorState.setText("Disconnected")
        else:
            self.SensorState.setText("Connected")
            humidity_data = '{0:.2f}'.format(humidity)
            self.HumidityDisplay.display(humidity_data)
            thresholdhumidity=self.HumiditySlider.value()
            if float(humidity_data) > thresholdhumidity:
                self.label_10.setText("ALARM!")
            else:
                self.label_10.setText("Safe!")
            
     #Function to read and display Temperature (in C and F) on press of Request button, also to take in threshold value from the user, compare with obtained/measured value and send out approriate alarm messages.        
    def readanddisplayT(self):
        now=datetime.datetime.now()
        self.Timelabel.setText(now.strftime("%m/%d/%Y %H:%M:%S"))
        humidity, temperature = Adafruit_DHT.read(22,4)
        if temperature == None:
            self.SensorState.setText("Disconnected")
        else:
            self.SensorState.setText("Connected")
            temp_data = '{0:.2f}'.format(temperature)
            self.TemperatureDisplayC.display(temp_data)
            self.GraphicTempBarC.setValue(float(temp_data))
            tempf=(float(temp_data) * (9/5.0)) + 32
            self.TemperatureDisplayF.display(tempf)
            self.GraphicTempBarF.setValue(float(tempf))
            thresholdtemperature=self.TempSlider.value()
            if float(temp_data) > thresholdtemperature:
                self.label_9.setText("ALARM!")
            else:
                self.label_9.setText("Safe!")

#Main
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



