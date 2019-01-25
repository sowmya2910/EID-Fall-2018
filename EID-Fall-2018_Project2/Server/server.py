# Function to run WebSocket Server on the mentioned IP
#
# Authors: Sowmya Ramakrishnan and Vinayak Srivatsan Kovalam Mohan
#

#Importing Libraries
import tornado.httpserver
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import matplotlib
import csv
import datetime

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it receives.
Messages are output to the terminal for debugging purposes.
'''
#WebSocket Initialization and Status
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')

    def on_message(self, message):
        print ('message received:  %s' % message)
        # Reverse Message and send it back
        print ('sending back message: %s' % message)
        self.write_message(message + '-' + str(get_data(message)))

    def on_close(self):
        print ('connection closed')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
    #To display temperature and humidity plots, we send them as images to the server
    (r"/(tempgraph.jpg)", tornado.web.StaticFileHandler, {'path':'./'}),
    (r"/(humidgraph.jpg)", tornado.web.StaticFileHandler, {'path':'./'})
])

#Reading obtained .csv file and returning appropriate data according to user's choice
def get_data(message):
    csvfile = open('data.csv', 'r')
    line = csvfile.readlines()[-1]
    data = line.split(",")
    if (data[0]==0 or data[1]==0 or data[2]==0 or data[3]==0 or data[4]==0 or data[5]==0 or data[6]==0 or data[7]==0):
        return 'No data obtained from sensor'
    if (message == 'current_temp'):
        return data[0] + '-' + data[8]
    elif (message == 'max_temp'):
        return data[1] + '-' + data[8] 
    elif (message == 'min_temp'):
        return data[2] + '-' + data[8]
    elif (message == 'avg_temp'):
        return data[3] + '-' + data[8] 
    elif (message == 'current_hum'):
        return data[4] + '-' + data[8]
    elif (message == 'max_hum'):
        return data[5] + '-' + data[8] 
    elif (message == 'min_hum'):
        return data[6] + '-' + data[8] 
    elif (message == 'avg_hum'):
        return data[7] + '-' + data[8]
    elif (message == 'graph_temp'):
        return tempgraphurl
    elif (message == 'graph_hum'):
        return humidgraphurl
    else:
        return 'Invalid Data. Please Try Again!'

#main
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    port = 8888
    #URLs for plots(images)
    tempgraphurl = 'http://10.0.0.37' + ':' + str(port) + '/tempgraph.jpg'
    humidgraphurl = 'http://10.0.0.37' + ':' + str(port) + '/humidgraph.jpg'
    #my RPi's IP
    http_server.listen(8888, address='10.0.0.37')
    #Starting WebServer
    print ('*** Starting WebSocket Server at 10.0.0.37 ***')
    tornado.ioloop.IOLoop.instance().start()
