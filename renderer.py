from socketIO_client import SocketIO, LoggingNamespace

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



