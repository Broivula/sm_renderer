from socketIO_client import SocketIO, LoggingNamespace
from queue import Queue
from threading import Thread
from renderer import Renderer 
import json


rend = Renderer()

def network_socket_thread(o_que):
	def on_connect():
		print('connected!')
		socketIO.emit('new_message')
		
	def on_disconnect():
		print('disconnected')
		
	def on_response(data):
		#print('incoming data! ' + str(data))
		o_que.put(data)

	 
	try:
		socketIO = SocketIO('https://localhost:3000', verify=False, transports='websocket')
		socketIO.on('connect', on_connect)
		socketIO.on('disconnect', on_disconnect)
		socketIO.on('response', on_response)
		socketIO.wait()
	except Exception as err:
		print('connection failed')
		print(str(err))


def rendering_thread(in_que):
	while True:
		data = in_que.get()
		parsed_data = json.loads(data)
		rend.update_rendered_data(parsed_data)

		

q = Queue()
thread_1 = Thread(target = network_socket_thread, args=(q, ))
thread_2 = Thread(target = rendering_thread, args=(q, ))

thread_1.start()
thread_2.start()


q.join()
	


