import socket, ssl
import requests
import time
import logging
from socketIO_client import SocketIO, LoggingNamespace

HOST = "127.0.0.1"
PORT = 3000

def on_connect():
	print('connected!')
	socketIO.emit('new_message')
	
def on_disconnect():
	print('disconnected')
	
def on_response(data):
	print('incoming data! ' + str(data))

 
	

try:
	socketIO = SocketIO('https://localhost:3000', verify=False, transports='websocket')
	socketIO.on('connect', on_connect)
	socketIO.on('disconnect', on_disconnect)
	socketIO.on('response', on_response)
	socketIO.wait()
except Exception as err:
	print('connection failed')
	print(str(err))

#r = requests.get("https://127.0.0.1:3000", "test", verify="./ssl_certs/ca.crt")

'''
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = False
context.load_verify_locations("./ssl_certs/ca.pem")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock = context.wrap_socket(s)
s_sock.connect((HOST, PORT))
time.sleep(2)
s_sock.send(b"hello");
data = s_sock.recv(2048)

while True:
	
	if len(data) < 1 :
		break
	else:
		print(repr(data))
'''

