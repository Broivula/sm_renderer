import time
from queue import Queue
from threading import Thread
from mirror_renderer import Renderer
from data_processing import D_Processing
from mirror_networking import Networking
import json

socket_port = 8928
rend = Renderer()
d_processor = D_Processing()

def networking_thread(p_que):
	# do networking stuff
	# some data arrives
	net = Networking()
	p_que.put("dataa")

def data_processing_thread(p_que, r_que):
	while True:
		data = p_que.get()
		# process the incoming data
		# spit out the processed data to be rendered
		r_que.put(d_processor.process(data))

def rendering_thread(r_que):
	global rend
	while True:
		data = r_que.get()
		rend.draw_label(data)

rendering_que = Queue()
processing_que = Queue()
thread_1 = Thread(target = networking_thread, args=(processing_que, ))
thread_2 = Thread(target = rendering_thread, args=(rendering_que,))
#thread_3 = Thread(target = data_processing_thread, args=(processing_que,rendering_que ))
thread_1.start()
thread_2.start()
rendering_que.join()
processing_que
rend.draw_label("kikkel")
time.sleep(3)
rendering_que.put("kikel man")
rend.__start__()
